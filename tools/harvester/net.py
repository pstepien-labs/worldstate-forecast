"""Polite HTTP fetching: identifying User-Agent, robots.txt, per-host delay,
conditional GET, size cap, retries left to the scheduler (backoff per source)."""
import gzip
import io
import os
import socket
import ssl
import time
import urllib.error
import urllib.request
import urllib.robotparser
import zlib
from urllib.parse import urlparse

from . import HARVESTER_VERSION

# Hosts that ask for slower request rates (seconds between requests).
HOST_DELAYS = {'api.gdeltproject.org': 10.0, 't.me': 5.0, 'www.sec.gov': 1.0}
# After HTTP 429/503 a host is paused for this long (doubled on each repeat, max 6 h) unless it sends Retry-After.
COOLDOWN_START_S = 900
COOLDOWN_MAX_S = 6 * 3600


class FetchResult:
    def __init__(self, url, status=None, body=b'', headers=None, error=None, not_modified=False, skipped=None,
                 throttled_until=None):
        self.url = url
        self.status = status
        self.body = body
        self.headers = headers or {}
        self.error = error
        self.not_modified = not_modified
        self.skipped = skipped  # reason when the request was deliberately not made
        self.throttled_until = throttled_until  # epoch seconds: host asked us to slow down

    @property
    def ok(self):
        return self.error is None and self.skipped is None and (self.not_modified or (self.status and 200 <= self.status < 300))

    def text(self):
        ctype = self.headers.get('content-type', '')
        enc = None
        if 'charset=' in ctype:
            enc = ctype.split('charset=', 1)[1].split(';')[0].strip().strip('"')
        for e in [enc, 'utf-8', 'cp1251', 'latin-1']:
            if not e:
                continue
            try:
                return self.body.decode(e)
            except (LookupError, UnicodeDecodeError):
                continue
        return self.body.decode('utf-8', 'replace')


class Fetcher:
    def __init__(self, min_delay=None, timeout=30, max_bytes=8_000_000, respect_robots=True, log=None):
        contact = os.environ.get('HARVEST_CONTACT', 'no-contact-set')
        self.ua = os.environ.get('HARVEST_USER_AGENT') or (
            f'worldstate-forecast-harvester/{HARVESTER_VERSION} (research; +https://github.com/pstepien-labs/worldstate-forecast; contact: {contact})')
        self.robots_token = 'worldstate-forecast-harvester'
        self.min_delay = float(os.environ.get('HARVEST_MIN_DELAY', '3') if min_delay is None else min_delay)
        self.timeout = timeout
        self.max_bytes = max_bytes
        self.respect_robots = respect_robots and os.environ.get('HARVEST_IGNORE_ROBOTS', '') != '1'
        self.log = log or (lambda *a, **k: None)
        self._last = {}
        self._robots = {}
        self._cooldown = {}   # host -> (until_epoch, current_cooldown_seconds)
        cafile = os.environ.get('HARVEST_CA_BUNDLE')
        self.ctx = ssl.create_default_context(cafile=cafile) if cafile else ssl.create_default_context()

    def _wait(self, host):
        last = self._last.get(host)
        delay = max(self.min_delay, HOST_DELAYS.get(host, 0)) if self.min_delay > 0 else 0
        if last is not None:
            gap = time.time() - last
            if gap < delay:
                time.sleep(delay - gap)
        self._last[host] = time.time()

    def _open(self, url, headers):
        req = urllib.request.Request(url, headers=headers)
        https = urllib.request.HTTPSHandler(context=self.ctx)
        opener = urllib.request.build_opener(https)
        return opener.open(req, timeout=self.timeout)

    def allowed(self, url):
        if not self.respect_robots:
            return True
        p = urlparse(url)
        base = f'{p.scheme}://{p.netloc}'
        cached = self._robots.get(base)
        if cached and time.time() - cached[1] < 86400:
            return cached[0].can_fetch(self.robots_token, url)
        rp = urllib.robotparser.RobotFileParser()
        try:
            self._wait(p.netloc)
            with self._open(base + '/robots.txt', {'User-Agent': self.ua}) as r:
                raw = r.read(500_000)
            rp.parse(self._decode(raw, r.headers).decode('utf-8', 'replace').splitlines())
        except urllib.error.HTTPError as e:
            # 4xx: no robots rules -> allowed; 5xx: treat as temporarily allowed, log it.
            rp.parse([])
            if e.code >= 500:
                self.log('robots_unavailable', url=base, status=e.code)
        except Exception as e:  # network problems: do not block, but record
            rp.parse([])
            self.log('robots_unavailable', url=base, error=str(e)[:200])
        self._robots[base] = (rp, time.time())
        return rp.can_fetch(self.robots_token, url)

    @staticmethod
    def _decode(raw, headers):
        enc = (headers.get('Content-Encoding') or '').lower()
        try:
            if enc == 'gzip' or raw[:2] == b'\x1f\x8b':
                return gzip.GzipFile(fileobj=io.BytesIO(raw)).read()
            if enc == 'deflate':
                return zlib.decompress(raw)
        except Exception:
            return raw
        return raw

    def cooling(self, host):
        until = self._cooldown.get(host, (0, 0))[0]
        return until if until > time.time() else None

    def _throttle(self, host, retry_after):
        prev = self._cooldown.get(host, (0, 0))[1]
        secs = None
        if retry_after:
            try:
                secs = int(retry_after)
            except ValueError:
                secs = None
        if secs is None:
            secs = min(COOLDOWN_MAX_S, prev * 2 if prev else COOLDOWN_START_S)
        until = time.time() + secs
        self._cooldown[host] = (until, secs)
        self.log('host_throttled', host=host, pause_min=round(secs / 60))
        return until

    def get(self, url, headers=None, etag=None, last_modified=None, check_robots=True):
        host = urlparse(url).netloc
        until = self.cooling(host)
        if until:
            return FetchResult(url, skipped='host paused after rate limiting', throttled_until=until)
        if check_robots and not self.allowed(url):
            return FetchResult(url, skipped='robots.txt disallows')
        h = {'User-Agent': self.ua, 'Accept-Encoding': 'gzip', 'Accept': '*/*'}
        if etag:
            h['If-None-Match'] = etag
        if last_modified:
            h['If-Modified-Since'] = last_modified
        h.update(headers or {})
        self._wait(urlparse(url).netloc)
        try:
            with self._open(url, h) as r:
                raw = r.read(self.max_bytes + 1)
                hdrs = {k.lower(): v for k, v in r.headers.items()}
                if len(raw) > self.max_bytes:
                    raw = raw[:self.max_bytes]
                    hdrs['x-truncated'] = '1'
                self._cooldown.pop(host, None)
                return FetchResult(url, r.status, self._decode(raw, r.headers), hdrs)
        except urllib.error.HTTPError as e:
            if e.code == 304:
                return FetchResult(url, 304, not_modified=True)
            if e.code in (429, 503):
                until = self._throttle(host, e.headers.get('Retry-After') if e.headers else None)
                return FetchResult(url, e.code, skipped=f'rate limited (HTTP {e.code})', throttled_until=until)
            return FetchResult(url, e.code, error=f'HTTP {e.code}')
        except (urllib.error.URLError, socket.timeout, ConnectionError, ssl.SSLError, OSError) as e:
            reason = getattr(e, 'reason', e)
            return FetchResult(url, error=f'{type(e).__name__}: {str(reason)[:200]}')
