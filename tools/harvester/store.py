"""On-disk layout, atomic writes, append-only corpus, event log, run lock.

data/harvest/
  items/YYYY-MM/YYYY-MM-DD.jsonl     text items (by publication day, UTC)
  datasets/observations.jsonl        numeric observations from primary datasets
  datasets/raw/<source_id>/...       raw snapshots (kept when content changes)
  pages/<source_id>/last.txt         last text of watched pages (for diffs)
  state/sources.json                 per-source schedule and health (checkpoint)
  state/seen.txt                     ids of stored items (deduplication)
  state/harvester.lock               pid of the running harvester
  state/STOP                         create this file to stop a running watch
  logs/events-YYYY-MM-DD.jsonl       structured event log
  status.json, STATUS.md             live progress (rewritten after each source)
"""
import hashlib
import json
import os
import re
import tempfile
from urllib.parse import parse_qsl, urlencode, urlparse, urlunparse

from .config import data_dir, iso, now


def path(*parts):
    p = os.path.join(data_dir(), *parts)
    os.makedirs(os.path.dirname(p), exist_ok=True)
    return p


def write_atomic(p, text):
    os.makedirs(os.path.dirname(p), exist_ok=True)
    fd, tmp = tempfile.mkstemp(dir=os.path.dirname(p), prefix='.tmp-')
    with os.fdopen(fd, 'w', encoding='utf-8') as f:
        f.write(text)
        f.flush()
        os.fsync(f.fileno())
    os.replace(tmp, p)


def read_json(p, default):
    try:
        with open(p, encoding='utf-8') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return default


def append_lines(p, lines):
    if not lines:
        return
    os.makedirs(os.path.dirname(p), exist_ok=True)
    with open(p, 'a', encoding='utf-8') as f:
        for line in lines:
            f.write(line + '\n')
        f.flush()
        os.fsync(f.fileno())


_TRACKING = re.compile(r'^(utm_|fbclid|gclid|mc_|at_|cmpid|ocid)', re.I)


def canonical_url(url):
    try:
        p = urlparse(url.strip())
        q = [(k, v) for k, v in parse_qsl(p.query, keep_blank_values=True) if not _TRACKING.match(k)]
        host = p.netloc.lower()
        host = host[4:] if host.startswith('www.') else host
        return urlunparse((p.scheme.lower() or 'https', host, p.path.rstrip('/') or '/', '', urlencode(q), ''))
    except Exception:
        return url.strip()


def item_id(url, fallback=''):
    key = canonical_url(url) if url else fallback
    return hashlib.sha1(key.encode('utf-8')).hexdigest()[:16]


class Seen:
    def __init__(self):
        self.p = path('state', 'seen.txt')
        self.ids = set()
        if os.path.exists(self.p):
            with open(self.p, encoding='utf-8') as f:
                self.ids = {line.strip() for line in f if line.strip()}

    def __contains__(self, i):
        return i in self.ids

    def add_many(self, ids):
        new = [i for i in ids if i not in self.ids]
        self.ids.update(new)
        append_lines(self.p, new)


def store_items(items, seen):
    """Append new items to the day files. Returns the number of new items."""
    by_file = {}
    new_ids = []
    for it in items:
        if it['id'] in seen or it['id'] in new_ids:
            continue
        day = (it.get('published') or it['fetched'])[:10]
        by_file.setdefault(path('items', day[:7], day + '.jsonl'), []).append(json.dumps(it, ensure_ascii=False))
        new_ids.append(it['id'])
    for p, lines in by_file.items():
        append_lines(p, lines)
    seen.add_many(new_ids)
    return len(new_ids)


class EventLog:
    def __init__(self, echo=True):
        self.echo = echo

    def __call__(self, event, level='info', **fields):
        rec = {'ts': iso(now()), 'level': level, 'event': event}
        rec.update(fields)
        append_lines(path('logs', f"events-{rec['ts'][:10]}.jsonl"), [json.dumps(rec, ensure_ascii=False)])
        if self.echo and (level != 'debug'):
            extra = ' '.join(f'{k}={v}' for k, v in fields.items() if k not in ('ts',))
            print(f"{rec['ts']} {level.upper():5} {event} {extra}", flush=True)


def pid_alive(pid):
    try:
        os.kill(pid, 0)
    except ProcessLookupError:
        return False
    except PermissionError:
        return True
    except OSError:
        return False
    return True


class Lock:
    """One harvester process at a time. A stale lock (dead pid) is taken over."""

    def __init__(self, log):
        self.p = path('state', 'harvester.lock')
        self.log = log

    def acquire(self):
        info = read_json(self.p, None)
        if info and pid_alive(int(info.get('pid', 0))) and int(info['pid']) != os.getpid():
            raise SystemExit(f"Another harvester is running (pid {info['pid']}, since {info.get('started')}). "
                             f"Use `python3 -m tools.harvester status`, or stop it with `python3 -m tools.harvester stop`.")
        if info:
            self.log('stale_lock_removed', level='warn', pid=info.get('pid'), started=info.get('started'))
        write_atomic(self.p, json.dumps({'pid': os.getpid(), 'started': iso(now())}))

    def release(self):
        info = read_json(self.p, None)
        if info and int(info.get('pid', 0)) == os.getpid():
            os.remove(self.p)
