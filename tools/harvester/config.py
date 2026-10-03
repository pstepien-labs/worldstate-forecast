"""Paths, configuration files and environment for the harvester."""
import csv
import hashlib
import os
import re
from datetime import date, datetime, timedelta, timezone

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
CONFIG_DIR = os.path.join(ROOT, 'sources', 'harvest')

# Countries treated as the "Western" (W) perspective when describing coverage.
# Whether a non-Western outlet is the actor's side (A) or a third party (T)
# depends on the event and is decided in stage 02, not here.
WESTERN = set('US GB CA AU NZ IE NO CH IS AT BE BG HR CY CZ DK EE FI FR DE GR HU IT LV LT LU MT NL PL PT RO SK SI ES SE'.split())


def data_dir():
    return os.path.abspath(os.environ.get('HARVEST_DATA') or os.path.join(ROOT, 'data', 'harvest'))


def config_dir():
    return os.path.abspath(os.environ.get('HARVEST_CONFIG') or CONFIG_DIR)


def load_env(path=None):
    """Load KEY=VALUE lines from .env into os.environ (existing variables win)."""
    path = path or os.path.join(ROOT, '.env')
    if not os.path.exists(path):
        return
    with open(path, encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith('#') or '=' not in line:
                continue
            k, v = line.split('=', 1)
            k, v = k.strip(), v.strip().strip('"').strip("'")
            if k and k not in os.environ:
                os.environ[k] = v


def read_csv(name):
    path = os.path.join(config_dir(), name)
    if not os.path.exists(path):
        return []
    with open(path, encoding='utf-8-sig', newline='') as f:
        rows = []
        for r in csv.DictReader(f, delimiter=';'):
            if not any((v or '').strip() for v in r.values()):
                continue
            if (r.get(next(iter(r))) or '').startswith('#'):
                continue
            rows.append({k.strip(): (v or '').strip() for k, v in r.items() if k})
        return rows


def file_hash(name):
    path = os.path.join(config_dir(), name)
    if not os.path.exists(path):
        return None
    with open(path, 'rb') as f:
        return hashlib.sha256(f.read()).hexdigest()[:16]


def split_list(value, sep='|'):
    return [x.strip() for x in (value or '').split(sep) if x.strip()]


def truthy(value):
    return (value or '').strip().lower() in ('1', 'y', 'yes', 'true')


def load_sources():
    """All harvest tasks: feeds.csv (text sources) + datasets.csv (numeric/primary)."""
    tasks = []
    for r in read_csv('feeds.csv'):
        r['_file'] = 'feeds.csv'
        r.setdefault('interval_h', '')
        tasks.append(r)
    for r in read_csv('datasets.csv'):
        r['_file'] = 'datasets.csv'
        r['kind'] = 'dataset'
        tasks.append(r)
    seen = set()
    for t in tasks:
        if t['id'] in seen:
            raise SystemExit(f"duplicate source id in config: {t['id']}")
        seen.add(t['id'])
    return tasks


DEFAULT_INTERVAL_H = {'rss': 6, 'telegram': 6, 'page': 12, 'gdelt': 12, 'dataset': 24}


def interval_hours(task):
    try:
        return float(task.get('interval_h') or DEFAULT_INTERVAL_H.get(task.get('kind'), 12))
    except ValueError:
        return DEFAULT_INTERVAL_H.get(task.get('kind'), 12)


def forbidden_domains():
    path = os.path.join(config_dir(), 'forbidden_domains.txt')
    out = set()
    if os.path.exists(path):
        with open(path, encoding='utf-8') as f:
            for line in f:
                line = line.split('#', 1)[0].strip().lower()
                if line:
                    out.add(line)
    return out


def is_forbidden(url_or_domain, forbidden):
    d = url_or_domain.lower()
    m = re.match(r'^[a-z]+://([^/:?#]+)', d)
    if m:
        d = m.group(1)
    d = d[4:] if d.startswith('www.') else d
    return any(d == f or d.endswith('.' + f) for f in forbidden)


def read_current():
    """Parameters of the current edition from editions/CURRENT.md (KEY=VALUE lines)."""
    path = os.path.join(ROOT, 'editions', 'CURRENT.md')
    out = {}
    if os.path.exists(path):
        with open(path, encoding='utf-8') as f:
            for line in f:
                m = re.match(r'^([A-Z_]+)=(.*)$', line.strip())
                if m:
                    out[m.group(1)] = m.group(2).strip()
    return out


def now():
    return datetime.now(timezone.utc)


def iso(dt):
    return dt.astimezone(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ') if dt else None


def parse_iso(s):
    if not s:
        return None
    try:
        return datetime.fromisoformat(s.replace('Z', '+00:00'))
    except ValueError:
        return None


def parse_day(s):
    return date.fromisoformat(s) if s else None


def backfill_days():
    try:
        return int(os.environ.get('HARVEST_BACKFILL_DAYS', '14'))
    except ValueError:
        return 14


def window_start_for(state_entry):
    """Start date for incremental queries: last success minus overlap, else backfill."""
    last = parse_iso((state_entry or {}).get('last_success'))
    if last:
        return (last - timedelta(days=3)).date()
    return (now() - timedelta(days=backfill_days())).date()
