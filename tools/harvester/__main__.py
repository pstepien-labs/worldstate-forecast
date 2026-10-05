"""Command line of the harvester.

  python3 -m tools.harvester doctor            environment check (Python, disk, keys, config)
  python3 -m tools.harvester selftest          offline end-to-end test (local fake server), incl. crash + resume
  python3 -m tools.harvester check             fetch every enabled source once now (writes data/harvest/CHECK.md)
  python3 -m tools.harvester run               one sweep over sources that are due, then exit
  python3 -m tools.harvester watch             run sweeps continuously until stopped (resumable)
  python3 -m tools.harvester stop              ask a running harvester to stop after the current source
  python3 -m tools.harvester status            live status: progress, health, errors, liveness
  python3 -m tools.harvester digest            build the edition digest (window from editions/CURRENT.md)
  python3 -m tools.harvester purge-domain DOMAIN    delete stored items from a publisher (opt-out request)
  python3 -m tools.harvester search CONCEPT|TEXT [--day YYYY-MM-DD | --from YYYY-MM-DD --to YYYY-MM-DD]
"""
import argparse
import json
import os
import shutil
import sys
import time
from datetime import date, datetime, timezone

from . import HARVESTER_VERSION, store
from .config import (ROOT, data_dir, load_env, load_sources, parse_iso, read_csv, split_list, truthy)


def cmd_doctor(a):
    ok = True
    print(f'harvester {HARVESTER_VERSION} · repository {ROOT}')
    v = sys.version_info
    print(f"Python {v.major}.{v.minor}.{v.micro}: {'OK' if v >= (3, 9) else 'TOO OLD (need 3.9+)'}")
    ok &= v >= (3, 9)
    dd = data_dir()
    os.makedirs(dd, exist_ok=True)
    free = shutil.disk_usage(dd).free / 1e9
    print(f'Data directory {dd}: free disk {free:.1f} GB ' + ('OK' if free > 2 else '(LOW: keep at least 2 GB free)'))
    try:
        tasks = load_sources()
    except SystemExit as e:
        print('Config error:', e)
        return 1
    en = [t for t in tasks if truthy(t.get('enabled', '1'))]
    kinds = {}
    for t in en:
        kinds[t.get('kind')] = kinds.get(t.get('kind'), 0) + 1
    print(f'Sources: {len(tasks)} configured, {len(en)} enabled — ' + ', '.join(f'{k} {n}' for k, n in sorted(kinds.items())))
    langs = sorted({t.get('lang') for t in en if t.get('lang')})
    print(f"Languages configured: {len(langs)} — {' '.join(langs)}")
    print(f"Keyword concepts: {len({r['concept'] for r in read_csv('keywords.csv')})}")
    needs = sorted({t.get('needs_key') for t in en if t.get('needs_key')})
    for k in needs:
        print(f"API key {k}: {'set' if os.environ.get(k) else 'NOT SET — sources using it will be skipped (see .env.example)'}")
    print(f"HARVEST_CONTACT: {'set' if os.environ.get('HARVEST_CONTACT') else 'not set (recommended: an e-mail for site operators, in .env)'}")
    return 0 if ok else 1


def cmd_check(a):
    from .sweep import Harvester
    h = Harvester()
    only = split_list(a.only, ',') if a.only else None
    h.run(force=True, only=only)
    state = store.read_json(store.path('state', 'sources.json'), {})
    tasks = [t for t in load_sources() if truthy(t.get('enabled', '1'))]
    if only:
        tasks = [t for t in tasks if t['id'] in only or t.get('kind') in only or t.get('adapter') in only]
    lines = ['# Source check', '', f'{datetime.now(timezone.utc):%Y-%m-%d %H:%M} UTC', '',
             '| Source | Kind | Status | HTTP | Items/obs total | Error |', '|---|---|---|---|---|---|']
    bad = 0
    for t in tasks:
        e = state.get(t['id'], {})
        if e.get('status') != 'ok':
            bad += 1
        lines.append(f"| {t['id']} | {t.get('kind')} | {e.get('status', 'not run')} | {e.get('last_http') or ''} | "
                     f"{e.get('items_total', e.get('obs_total', 0))} | {(e.get('last_error') or '')[:120]} |")
    store.write_atomic(store.path('CHECK.md'), '\n'.join(lines) + '\n')
    print(f'\n{len(tasks) - bad}/{len(tasks)} sources OK. Details: {store.path("CHECK.md")}')
    return 0


def cmd_run(a):
    from .sweep import Harvester
    Harvester().run(max_sources=a.max)
    return 0


def cmd_watch(a):
    from .sweep import Harvester
    Harvester().watch(min_sleep=a.min_sleep)
    return 0


def cmd_stop(a):
    p = store.path('state', 'STOP')
    with open(p, 'w') as f:
        f.write(datetime.now(timezone.utc).isoformat())
    lock = store.read_json(store.path('state', 'harvester.lock'), None)
    if lock and store.pid_alive(int(lock['pid'])):
        print(f"Stop requested; harvester pid {lock['pid']} will stop after the current source.")
        if a.wait:
            while store.pid_alive(int(lock['pid'])):
                time.sleep(2)
            print('Stopped.')
    else:
        print('No running harvester found (stop file left in place; it is removed on the next start).')
    return 0


def cmd_status(a):
    st = store.read_json(store.path('status.json'), None)
    if not st:
        print('No harvest has run yet in', data_dir())
        return 1
    lock = store.read_json(store.path('state', 'harvester.lock'), None)
    alive = bool(lock and store.pid_alive(int(lock['pid'])))
    hb = parse_iso(st.get('heartbeat'))
    age = (datetime.now(timezone.utc) - hb).total_seconds() / 60 if hb else None
    md = open(store.path('STATUS.md'), encoding='utf-8').read() if os.path.exists(store.path('STATUS.md')) else ''
    print(md)
    if alive and age is not None and age < 15:
        print(f'LIVENESS: running (pid {lock["pid"]}), last heartbeat {age:.0f} min ago.')
    elif alive:
        print(f'LIVENESS: process {lock["pid"]} exists but heartbeat is {age:.0f} min old — it may be stuck on a slow source; '
              'if it stays like this for >30 min, stop it and start again (it resumes).')
    else:
        print('LIVENESS: not running. Start or resume with `scripts/harvest.sh start` (or `python3 -m tools.harvester watch`).')
    logs = sorted(os.listdir(store.path('logs', 'x').rsplit(os.sep, 1)[0])) if os.path.isdir(os.path.join(data_dir(), 'logs')) else []
    if logs:
        print(f"Event log: {os.path.join(data_dir(), 'logs', logs[-1])}")
    return 0


def cmd_digest(a):
    from . import digest
    d_from, d_to, out = digest.default_window()
    if a.from_:
        d_from = date.fromisoformat(a.from_)
    if a.to:
        d_to = date.fromisoformat(a.to)
    if a.out:
        out = a.out
    m = digest.build(d_from, d_to, out)
    print(json.dumps({k: m[k] for k in ('items_in_window', 'items_matched', 'western_share_pct', 'countries')}, indent=1))
    return 0


def cmd_search(a):
    from . import digest
    for it in digest.search(a.query, day=a.day, limit=a.limit, d_from=a.from_, d_to=a.to):
        print(f"{(it.get('published') or '')[:16]} [{it.get('lang')}·{it.get('country')}·{it.get('role')}] "
              f"{it.get('source_name')}: {it.get('title')}\n    {it.get('url')}")
    return 0


def cmd_purge_domain(a):
    """Delete every stored item whose link is on the given domain (publisher opt-out)."""
    import glob
    from .config import is_forbidden
    d = a.domain.lower().strip()
    dom = {d[4:] if d.startswith('www.') else d}
    removed = kept = 0
    for p in glob.glob(os.path.join(data_dir(), 'items', '*', '*.jsonl')):
        out = []
        with open(p, encoding='utf-8') as f:
            for line in f:
                try:
                    url = json.loads(line).get('url', '')
                except json.JSONDecodeError:
                    out.append(line)
                    continue
                if is_forbidden(url, dom):
                    removed += 1
                else:
                    out.append(line)
                    kept += 1
        store.write_atomic(p, ''.join(out))
    print(f'purged {removed} items from {a.domain}; {kept} items kept. '
          f'Add the domain to sources/harvest/optout_domains.txt so it is never collected again.')
    return 0


def cmd_selftest(a):
    from . import selftest
    return selftest.main()


def main(argv=None):
    load_env()
    p = argparse.ArgumentParser(prog='python3 -m tools.harvester', description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = p.add_subparsers(dest='cmd', required=True)
    sub.add_parser('doctor').set_defaults(fn=cmd_doctor)
    sub.add_parser('selftest').set_defaults(fn=cmd_selftest)
    c = sub.add_parser('check')
    c.add_argument('--only', help='comma-separated source ids, kinds (rss, gdelt, …) or adapters')
    c.set_defaults(fn=cmd_check)
    r = sub.add_parser('run')
    r.add_argument('--max', type=int, help='at most N sources in this sweep')
    r.set_defaults(fn=cmd_run)
    w = sub.add_parser('watch')
    w.add_argument('--min-sleep', type=int, default=300, help='seconds between sweeps at least (default 300)')
    w.set_defaults(fn=cmd_watch)
    s = sub.add_parser('stop')
    s.add_argument('--wait', action='store_true')
    s.set_defaults(fn=cmd_stop)
    sub.add_parser('status').set_defaults(fn=cmd_status)
    d = sub.add_parser('digest')
    d.add_argument('--from', dest='from_')
    d.add_argument('--to')
    d.add_argument('--out')
    d.set_defaults(fn=cmd_digest)
    pg = sub.add_parser('purge-domain', help='delete stored items from a publisher (opt-out)')
    pg.add_argument('domain')
    pg.set_defaults(fn=cmd_purge_domain)
    q = sub.add_parser('search')
    q.add_argument('query')
    q.add_argument('--day')
    q.add_argument('--from', dest='from_', help='YYYY-MM-DD (default: current edition window)')
    q.add_argument('--to')
    q.add_argument('--limit', type=int, default=200)
    q.set_defaults(fn=cmd_search)
    a = p.parse_args(argv)
    return a.fn(a) or 0


if __name__ == '__main__':
    sys.exit(main())
