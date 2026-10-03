"""Source adapters. Each adapter takes a task (a row of feeds.csv / datasets.csv)
and returns items (text) and/or observations (numbers).

Adapters never raise for ordinary failures: they return an `error` string, and
the scheduler records it and backs off. Only programming errors propagate.
"""
import csv
import email.utils
import hashlib
import html
import io
import json
import math
import os
import re
import xml.etree.ElementTree as ET
from datetime import datetime, timedelta, timezone
from urllib.parse import quote, urlencode

from . import store
from .config import (ROOT, is_forbidden, iso, now, read_csv, split_list, window_start_for)


class Result:
    def __init__(self):
        self.items = []
        self.observations = []
        self.state = {}      # values persisted in the source's state entry
        self.error = None
        self.skipped = None
        self.note = ''
        self.http_status = None


# ---------- helpers ----------

_TAG = re.compile(r'<[^>]+>')
_WS = re.compile(r'\s+')


def clean_text(s, limit=600):
    if not s:
        return ''
    s = html.unescape(_TAG.sub(' ', s))
    s = _WS.sub(' ', s).strip()
    return s[:limit]


def parse_date(s):
    if not s:
        return None
    s = s.strip()
    try:
        dt = email.utils.parsedate_to_datetime(s)
        if dt is not None:
            return dt if dt.tzinfo else dt.replace(tzinfo=timezone.utc)
    except (TypeError, ValueError, IndexError):
        pass
    try:
        dt = datetime.fromisoformat(s.replace('Z', '+00:00'))
        return dt if dt.tzinfo else dt.replace(tzinfo=timezone.utc)
    except ValueError:
        pass
    m = re.match(r'^(\d{4})(\d{2})(\d{2})T?(\d{2})(\d{2})(\d{2})Z?$', s)
    if m:
        return datetime(*map(int, m.groups()), tzinfo=timezone.utc)
    return None


def make_item(task, url, title, summary='', published=None, **extra):
    pub = parse_date(published) if isinstance(published, str) else published
    fetched = now()
    if pub and pub > fetched + timedelta(days=1):
        pub = None  # nonsense future dates
    it = {
        'id': store.item_id(url, fallback=f"{task['id']}|{title}|{published}"),
        'source_id': task['id'],
        'source_name': task.get('name', ''),
        'kind': task.get('kind', ''),
        'lang': task.get('lang', ''),
        'country': task.get('country', ''),
        'actor': task.get('actor', ''),
        'role': task.get('role', ''),
        'tier': task.get('tier', ''),
        'groups': task.get('groups', ''),
        'url': url,
        'title': clean_text(title, 300),
        'summary': clean_text(summary, 600),
        'published': iso(pub) if pub else None,
        'fetched': iso(fetched),
    }
    if extra:
        it['extra'] = {k: v for k, v in extra.items() if v not in (None, '')}
    return it


def expand(template, task, entry, ctx):
    """Placeholders: {start} {end} {start_compact} {end_compact} {date_ddmmyyyy} {days} {key:ENV}."""
    start = window_start_for(entry)
    end = now().date()
    if (end - start).days > 92 and '{start}' in template and 'nbp.pl' in template:
        start = end - timedelta(days=92)  # NBP API range limit
    days = max(1, min(10, (end - start).days or 1))
    missing = []

    def key(m):
        v = os.environ.get(m.group(1), '')
        if not v:
            missing.append(m.group(1))
        return quote(v, safe='')
    out = re.sub(r'\{key:([A-Z0-9_]+)\}', key, template)
    out = (out.replace('{start}', start.isoformat()).replace('{end}', end.isoformat())
              .replace('{start_compact}', start.strftime('%Y%m%d') + '000000')
              .replace('{end_compact}', end.strftime('%Y%m%d') + '235959')
              .replace('{date_ddmmyyyy}', end.strftime('%d/%m/%Y'))
              .replace('{days}', str(days)))
    return out, missing


def params(task):
    out = {}
    for part in split_list(task.get('params', '')):
        if '=' in part:
            k, v = part.split('=', 1)
            out[k.strip()] = v.strip()
    return out


def fetch(fetcher, url, entry, res, conditional=True, headers=None):
    r = fetcher.get(url, headers=headers,
                    etag=entry.get('etag') if conditional else None,
                    last_modified=entry.get('last_modified') if conditional else None)
    res.http_status = r.status
    if r.skipped:
        res.skipped = r.skipped
        return None
    if r.error:
        res.error = r.error
        return None
    if r.not_modified:
        res.note = 'not modified'
        return None
    if conditional:
        if r.headers.get('etag'):
            res.state['etag'] = r.headers['etag']
        if r.headers.get('last-modified'):
            res.state['last_modified'] = r.headers['last-modified']
    return r


# ---------- RSS / Atom / RDF ----------

def _local(tag):
    return tag.rsplit('}', 1)[-1].lower() if isinstance(tag, str) else ''


def _child_text(el, *names):
    for c in el:
        if _local(c.tag) in names:
            if _local(c.tag) == 'link' and c.get('href'):
                if c.get('rel') in (None, 'alternate'):
                    return c.get('href')
                continue
            if (c.text or '').strip():
                return c.text.strip()
            inner = ''.join(c.itertext()).strip()
            if inner:
                return inner
    return ''


def _sanitize_xml(text):
    text = re.sub(r'[\x00-\x08\x0b\x0c\x0e-\x1f]', '', text)
    text = re.sub(r'&(?!(?:[a-zA-Z]+|#\d+|#x[0-9a-fA-F]+);)', '&amp;', text)
    return text


def parse_feed(text):
    """Return a list of dicts: title, link, summary, published. Tolerant of broken XML."""
    root = None
    for attempt in (text, _sanitize_xml(text)):
        try:
            root = ET.fromstring(attempt.encode('utf-8') if isinstance(attempt, str) else attempt)
            break
        except ET.ParseError:
            continue
    entries = []
    if root is not None:
        for el in root.iter():
            if _local(el.tag) in ('item', 'entry'):
                entries.append({
                    'title': _child_text(el, 'title'),
                    'link': _child_text(el, 'link') or _child_text(el, 'guid', 'id'),
                    'summary': _child_text(el, 'description', 'summary', 'content', 'encoded'),
                    'published': _child_text(el, 'pubdate', 'published', 'updated', 'date', 'issued'),
                })
        return entries
    # Last resort: regex extraction from malformed feeds
    for block in re.findall(r'<item\b.*?</item>|<entry\b.*?</entry>', text, re.S | re.I):
        def g(name):
            m = re.search(rf'<{name}\b[^>]*>(.*?)</{name}>', block, re.S | re.I)
            return re.sub(r'^<!\[CDATA\[|\]\]>$', '', m.group(1).strip()) if m else ''
        link = g('link')
        if not link:
            m = re.search(r'<link[^>]+href="([^"]+)"', block)
            link = m.group(1) if m else ''
        entries.append({'title': g('title'), 'link': link, 'summary': g('description') or g('summary'),
                        'published': g('pubDate') or g('published') or g('updated') or g('dc:date')})
    return entries


def run_rss(task, fetcher, entry, ctx):
    res = Result()
    r = fetch(fetcher, task['url'], entry, res)
    if not r:
        return res
    entries = parse_feed(r.text())
    if not entries:
        res.error = 'no items parsed (not a feed? check the URL)'
        return res
    for e in entries:
        link = (e['link'] or '').strip()
        if not link or is_forbidden(link, ctx['forbidden']):
            continue
        res.items.append(make_item(task, link, e['title'], e['summary'], e['published']))
    return res


# ---------- Telegram public web preview (t.me/s/<channel>) ----------

def run_telegram(task, fetcher, entry, ctx):
    res = Result()
    url = task['url'] if task['url'].startswith('http') else f"https://t.me/s/{task['url'].lstrip('@')}"
    r = fetch(fetcher, url, entry, res, conditional=False)
    if not r:
        return res
    page = r.text()
    blocks = re.split(r'<div class="tgme_widget_message_wrap', page)[1:]
    for b in blocks:
        post = re.search(r'data-post="([^"]+)"', b)
        when = re.search(r'<time[^>]+datetime="([^"]+)"', b)
        body = re.search(r'<div class="tgme_widget_message_text[^"]*"[^>]*>(.*?)</div>', b, re.S)
        if not post or not body:
            continue
        text = clean_text(body.group(1).replace('<br/>', ' ').replace('<br>', ' '), 800)
        if not text:
            continue
        link = f'https://t.me/{post.group(1)}'
        res.items.append(make_item(task, link, text[:160], text, when.group(1) if when else None))
    if not blocks:
        res.error = 'no messages found (channel private, renamed, or preview disabled)'
    return res


# ---------- watched pages (official pages without feeds): text diff ----------

class _TextExtractor:
    SKIP = re.compile(r'<(script|style|noscript|svg|head)\b.*?</\1>', re.S | re.I)
    BLOCK = re.compile(r'</?(p|div|li|tr|h[1-6]|br|td|section|article|dd|dt)\b[^>]*>', re.I)

    @classmethod
    def lines(cls, page):
        page = cls.SKIP.sub(' ', page)
        page = cls.BLOCK.sub('\n', page)
        text = html.unescape(_TAG.sub(' ', page))
        out = []
        for line in text.split('\n'):
            line = _WS.sub(' ', line).strip()
            if len(line) >= 20:
                out.append(line)
        return out


def run_page(task, fetcher, entry, ctx):
    res = Result()
    r = fetch(fetcher, task['url'], entry, res, conditional=False)
    if not r:
        return res
    lines = _TextExtractor.lines(r.text())
    if not lines:
        res.error = 'page has no readable text (JavaScript-only page?)'
        return res
    prev_path = store.path('pages', task['id'], 'last.txt')
    prev = set()
    if os.path.exists(prev_path):
        with open(prev_path, encoding='utf-8') as f:
            prev = set(f.read().split('\n'))
    new = [ln for ln in lines if ln not in prev]
    store.write_atomic(prev_path, '\n'.join(lines))
    if prev and new:
        text = ' / '.join(new[:25])
        digest = hashlib.sha1('\n'.join(new).encode()).hexdigest()[:10]
        res.items.append(make_item(task, f"{task['url']}#change-{digest}",
                                   f"[page update] {task.get('name', '')}: {new[0][:150]}", text, now(),
                                   new_lines=len(new)))
    res.note = f'{len(new)} new lines' if prev else 'baseline stored'
    return res


# ---------- GDELT DOC 2.0 article lists (multilingual discovery) ----------

GDELT_LANG = {
    'english': 'en', 'russian': 'ru', 'ukrainian': 'uk', 'chinese': 'zh', 'arabic': 'ar', 'persian': 'fa',
    'turkish': 'tr', 'french': 'fr', 'german': 'de', 'spanish': 'es', 'portuguese': 'pt', 'polish': 'pl',
    'japanese': 'ja', 'korean': 'ko', 'hebrew': 'he', 'hindi': 'hi', 'urdu': 'ur', 'italian': 'it',
    'dutch': 'nl', 'swedish': 'sv', 'finnish': 'fi', 'danish': 'da', 'norwegian': 'no', 'czech': 'cs',
    'romanian': 'ro', 'hungarian': 'hu', 'greek': 'el', 'serbian': 'sr', 'croatian': 'hr', 'bulgarian': 'bg',
    'lithuanian': 'lt', 'latvian': 'lv', 'estonian': 'et', 'indonesian': 'id', 'malay': 'ms', 'vietnamese': 'vi',
    'thai': 'th', 'bengali': 'bn', 'tamil': 'ta', 'armenian': 'hy', 'azerbaijani': 'az', 'georgian': 'ka',
    'kazakh': 'kk', 'swahili': 'sw', 'amharic': 'am', 'somali': 'so', 'hausa': 'ha',
}


def country_code(name):
    table = ctx_country_table()
    return table.get((name or '').strip().lower(), (name or '').strip())


_COUNTRIES = None


def ctx_country_table():
    global _COUNTRIES
    if _COUNTRIES is None:
        _COUNTRIES = {}
        for r in read_csv('countries.csv'):
            for alias in split_list(r.get('names', '')):
                _COUNTRIES[alias.lower()] = r['code']
    return _COUNTRIES


def run_gdelt(task, fetcher, entry, ctx):
    res = Result()
    start = datetime.combine(window_start_for(entry), datetime.min.time(), timezone.utc)
    last = entry.get('gdelt_last_seen')
    if last:
        start = max(start, (parse_date(last) or start) - timedelta(hours=2))
    q = {'query': task['url'], 'mode': 'ArtList', 'format': 'json', 'maxrecords': params(task).get('max', '250'),
         'sort': 'DateDesc', 'startdatetime': start.strftime('%Y%m%d%H%M%S'),
         'enddatetime': now().strftime('%Y%m%d%H%M%S')}
    url = 'https://api.gdeltproject.org/api/v2/doc/doc?' + urlencode(q)
    r = fetch(fetcher, url, entry, res, conditional=False)
    if not r:
        return res
    body = r.text().strip()
    if not body.startswith('{'):
        res.error = 'GDELT returned a non-JSON answer: ' + body[:150]
        return res
    try:
        data = json.loads(body)
    except json.JSONDecodeError as e:
        res.error = f'GDELT JSON error: {e}'
        return res
    newest = last
    for a in data.get('articles', []) or []:
        link = a.get('url', '')
        if not link or is_forbidden(link, ctx['forbidden']):
            continue
        it = make_item(task, link, a.get('title', ''), '', a.get('seendate'),
                       publisher=a.get('domain'), source_country=a.get('sourcecountry'))
        lang = GDELT_LANG.get((a.get('language') or '').lower(), (a.get('language') or '').lower()[:2])
        it['lang'] = lang or it['lang']
        it['country'] = country_code(a.get('sourcecountry')) or ''
        it['role'] = 'discovered'
        it['source_name'] = a.get('domain') or it['source_name']
        res.items.append(it)
        if a.get('seendate') and (not newest or a['seendate'] > newest):
            newest = a['seendate']
    if newest:
        res.state['gdelt_last_seen'] = newest
    return res


# ---------- numeric datasets ----------

def obs(task, indicator, day, value, unit='', **extra):
    try:
        v = float(str(value).replace(',', '.'))
    except (TypeError, ValueError):
        return None
    if math.isnan(v):
        return None
    o = {'source_id': task['id'], 'indicator': indicator, 'date': str(day)[:10], 'value': v,
         'unit': unit or task.get('unit', ''), 'fetched': iso(now())}
    if extra:
        o['extra'] = extra
    return o


def _save_raw(task, body, ext, res):
    h = hashlib.sha256(body).hexdigest()[:16]
    if h == task.get('_entry', {}).get('raw_hash'):
        return False
    stamp = now().strftime('%Y%m%dT%H%M%SZ')
    p = store.path('datasets', 'raw', task['id'], f'{stamp}.{ext}')
    with open(p, 'wb') as f:
        f.write(body)
    res.state['raw_hash'] = h
    folder = os.path.dirname(p)
    files = sorted(os.listdir(folder))
    for old in files[:-30]:  # keep the last 30 snapshots
        os.remove(os.path.join(folder, old))
    return True


def _get_dataset(task, fetcher, entry, ctx, res, headers=None):
    url, missing = expand(task['url'], task, entry, ctx)
    hdrs = {}
    for k, v in (headers or {}).items():
        v2, miss2 = expand(v, task, entry, ctx)
        hdrs[k] = v2
        missing += miss2
    if missing:
        res.skipped = 'missing API key: ' + ', '.join(sorted(set(missing))) + ' (set it in .env)'
        return None
    task['_entry'] = entry
    return fetch(fetcher, url, entry, res, conditional=False, headers=hdrs)


def ds_nbp(task, fetcher, entry, ctx):
    res = Result()
    r = _get_dataset(task, fetcher, entry, ctx, res)
    if not r:
        return res
    _save_raw(task, r.body, 'json', res)
    data = json.loads(r.text())
    for rate in data.get('rates', []):
        o = obs(task, task['indicator'], rate.get('effectiveDate'), rate.get('mid'))
        if o:
            res.observations.append(o)
    return res


def ds_sdmx_csv(task, fetcher, entry, ctx):
    """ECB data API (format=csvdata) and other SDMX CSV: TIME_PERIOD, OBS_VALUE."""
    res = Result()
    r = _get_dataset(task, fetcher, entry, ctx, res)
    if not r:
        return res
    _save_raw(task, r.body, 'csv', res)
    for row in csv.DictReader(io.StringIO(r.text())):
        o = obs(task, task['indicator'], row.get('TIME_PERIOD'), row.get('OBS_VALUE'))
        if o:
            res.observations.append(o)
    if not res.observations:
        res.error = 'no observations in SDMX answer'
    return res


def ds_fred_csv(task, fetcher, entry, ctx):
    """FRED graph CSV (no key): columns observation_date|DATE, <SERIES>."""
    res = Result()
    r = _get_dataset(task, fetcher, entry, ctx, res)
    if not r:
        return res
    _save_raw(task, r.body, 'csv', res)
    rows = list(csv.reader(io.StringIO(r.text())))
    if len(rows) < 2:
        res.error = 'empty FRED answer'
        return res
    for row in rows[1:]:
        if len(row) >= 2 and row[1] not in ('.', ''):
            o = obs(task, task['indicator'], row[0], row[1])
            if o:
                res.observations.append(o)
    return res


def ds_cbr_xml(task, fetcher, entry, ctx):
    res = Result()
    r = _get_dataset(task, fetcher, entry, ctx, res)
    if not r:
        return res
    _save_raw(task, r.body, 'xml', res)
    root = ET.fromstring(r.body)
    day = datetime.strptime(root.get('Date'), '%d.%m.%Y').date() if root.get('Date') else now().date()
    wanted = set(split_list(params(task).get('codes', 'USD,EUR,CNY'), ','))
    for v in root.iter('Valute'):
        code = (v.findtext('CharCode') or '').strip()
        if code in wanted:
            nominal = float((v.findtext('Nominal') or '1').replace(',', '.'))
            value = float((v.findtext('Value') or '0').replace(',', '.')) / nominal
            o = obs(task, f'{code}/RUB', day, value, 'RUB')
            if o:
                res.observations.append(o)
    return res


def ds_arcgis(task, fetcher, entry, ctx):
    """ArcGIS FeatureServer query (IMF PortWatch). Params: date_field, name_field, value_fields."""
    res = Result()
    r = _get_dataset(task, fetcher, entry, ctx, res)
    if not r:
        return res
    _save_raw(task, r.body, 'json', res)
    data = json.loads(r.text())
    if 'error' in data:
        res.error = f"ArcGIS error: {str(data['error'])[:200]}"
        return res
    p = params(task)
    dfield, nfield = p.get('date_field', 'date'), p.get('name_field', 'portname')
    vfields = split_list(p.get('value_fields', 'n_total'), ',')
    for f in data.get('features', []):
        a = f.get('attributes', {})
        d = a.get(dfield)
        if isinstance(d, (int, float)):
            d = datetime.fromtimestamp(d / 1000, timezone.utc).date()
        for vf in vfields:
            if vf in a:
                o = obs(task, f"{task['indicator']}:{a.get(nfield)}:{vf}", d, a[vf], 'count')
                if o:
                    res.observations.append(o)
    if data.get('features') and not res.observations:
        res.error = f'fields {vfields} not found; available: {sorted(data["features"][0].get("attributes", {}))[:20]}'
    return res


def ds_agsi(task, fetcher, entry, ctx):
    res = Result()
    r = _get_dataset(task, fetcher, entry, ctx, res, headers={'x-key': '{key:AGSI_API_KEY}'})
    if not r:
        return res
    _save_raw(task, r.body, 'json', res)
    data = json.loads(r.text())
    for row in data.get('data', []):
        o = obs(task, task['indicator'], row.get('gasDayStart'), row.get('full'), '%')
        if o:
            res.observations.append(o)
    if not res.observations:
        res.error = 'no rows in AGSI answer (check params / key)'
    return res


def ds_eia(task, fetcher, entry, ctx):
    res = Result()
    r = _get_dataset(task, fetcher, entry, ctx, res)
    if not r:
        return res
    _save_raw(task, r.body, 'json', res)
    data = json.loads(r.text())
    for row in (data.get('response') or {}).get('data', []):
        o = obs(task, task['indicator'], row.get('period'), row.get('value'))
        if o:
            res.observations.append(o)
    return res


def _haversine_km(lat1, lon1, lat2, lon2):
    r = 6371.0
    p1, p2 = math.radians(lat1), math.radians(lat2)
    dp, dl = p2 - p1, math.radians(lon2 - lon1)
    a = math.sin(dp / 2) ** 2 + math.cos(p1) * math.cos(p2) * math.sin(dl / 2) ** 2
    return 2 * r * math.asin(math.sqrt(a))


def ds_firms(task, fetcher, entry, ctx):
    """NASA FIRMS area CSV: count fire detections near key sites (sites.csv) per day."""
    res = Result()
    r = _get_dataset(task, fetcher, entry, ctx, res)
    if not r:
        return res
    _save_raw(task, r.body, 'csv', res)
    text = r.text()
    if 'latitude' not in text[:300]:
        res.error = 'unexpected FIRMS answer: ' + text[:150]
        return res
    sites = [s for s in read_csv('sites.csv') if s.get('lat') and s.get('lon')]
    counts = {}
    total = {}
    for row in csv.DictReader(io.StringIO(text)):
        try:
            lat, lon = float(row['latitude']), float(row['longitude'])
        except (KeyError, ValueError):
            continue
        day = row.get('acq_date', '')
        total[day] = total.get(day, 0) + 1
        for s in sites:
            radius = float(s.get('radius_km') or 8)
            if _haversine_km(lat, lon, float(s['lat']), float(s['lon'])) <= radius:
                counts[(s['id'], day)] = counts.get((s['id'], day), 0) + 1
    for day, n in total.items():
        o = obs(task, f"{task['indicator']}:area_total", day, n, 'detections')
        if o:
            res.observations.append(o)
    for (site, day), n in counts.items():
        o = obs(task, f'fire_near_site:{site}', day, n, 'detections')
        if o:
            res.observations.append(o)
    return res


def ds_csv_diff(task, fetcher, entry, ctx):
    """Snapshot a list (e.g. OFAC SDN CSV) and report rows added since the last snapshot."""
    res = Result()
    r = _get_dataset(task, fetcher, entry, ctx, res)
    if not r:
        return res
    rows = r.text().splitlines()
    prev_path = store.path('datasets', 'raw', task['id'], 'last_rows.txt')
    prev = None
    if os.path.exists(prev_path):
        with open(prev_path, encoding='utf-8') as f:
            prev = set(f.read().splitlines())
    store.write_atomic(prev_path, '\n'.join(rows))
    if prev is None:
        res.note = f'baseline stored ({len(rows)} rows)'
        return res
    added = [x for x in rows if x not in prev]
    removed = len(prev) - (len(rows) - len(added))
    day = now().date()
    for o in (obs(task, f"{task['indicator']}:added", day, len(added), 'rows'),
              obs(task, f"{task['indicator']}:removed", day, max(0, removed), 'rows')):
        if o:
            res.observations.append(o)
    if added:
        text = ' || '.join(clean_text(a, 200) for a in added[:40])
        res.items.append(make_item(task, f"{task['url']}#added-{day}-{len(added)}",
                                   f"[{task.get('name', '')}] {len(added)} rows added, {max(0, removed)} removed", text, now()))
    return res


def ds_snapshot(task, fetcher, entry, ctx):
    """Keep a raw copy when the content changes (for Claude to read); no parsing."""
    res = Result()
    r = _get_dataset(task, fetcher, entry, ctx, res)
    if not r:
        return res
    ext = params(task).get('ext', 'bin')
    res.note = 'changed' if _save_raw(task, r.body, ext, res) else 'unchanged'
    return res


TEXT_ADAPTERS = {'rss': run_rss, 'telegram': run_telegram, 'page': run_page, 'gdelt': run_gdelt}
DATASET_ADAPTERS = {'nbp': ds_nbp, 'sdmx_csv': ds_sdmx_csv, 'fred_csv': ds_fred_csv, 'cbr_xml': ds_cbr_xml,
                    'arcgis': ds_arcgis, 'agsi': ds_agsi, 'eia': ds_eia, 'firms': ds_firms,
                    'csv_diff': ds_csv_diff, 'snapshot': ds_snapshot}


def run_task(task, fetcher, entry, ctx):
    if task.get('kind') == 'dataset':
        fn = DATASET_ADAPTERS.get(task.get('adapter'))
    else:
        fn = TEXT_ADAPTERS.get(task.get('kind'))
    if not fn:
        res = Result()
        res.error = f"unknown kind/adapter: {task.get('kind')}/{task.get('adapter')}"
        return res
    try:
        return fn(task, fetcher, entry, ctx)
    except (ValueError, KeyError, ET.ParseError, json.JSONDecodeError, UnicodeError) as e:
        res = Result()
        res.error = f'parse error: {type(e).__name__}: {str(e)[:200]}'
        return res
