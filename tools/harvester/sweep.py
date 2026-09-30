"""Scheduler: decides which sources are due, runs them one by one, checkpoints
state after every source, backs off failing sources, keeps status files live.

Resumability: state/sources.json is rewritten atomically after each source.
If the process dies, the next start skips every source that already succeeded
within its interval and continues with the rest. Nothing is fetched twice
unnecessarily and no stored item is lost (items are appended before state).
"""
import json
import os
import shutil
import signal
import time
from datetime import timedelta

from . import HARVESTER_VERSION, adapters, store
from .config import (forbidden_domains, interval_hours, iso, load_sources, now, parse_iso, truthy)
from .net import Fetcher

MAX_BACKOFF_H = 24


class Stop(Exception):
    pass


class Harvester:
    def __init__(self, echo=True):
        self.log = store.EventLog(echo=echo)
        self.state_path = store.path('state', 'sources.json')
        self.state = store.read_json(self.state_path, {})
        self.fetcher = Fetcher(log=lambda ev, **kw: self.log(ev, level='warn', **kw))
        self.ctx = {'forbidden': forbidden_domains()}
        self.stop_requested = False
        self.status = store.read_json(store.path('status.json'), {})
        self.seen = None

    # ----- state helpers -----
    def entry(self, sid):
        return self.state.setdefault(sid, {})

    def save_state(self):
        store.write_atomic(self.state_path, json.dumps(self.state, ensure_ascii=False, indent=1, sort_keys=True))

    def due(self, task, t):
        e = self.state.get(task['id'], {})
        nxt = parse_iso(e.get('next_due'))
        return nxt is None or nxt <= t

    def _handle_signal(self, signum, frame):
        self.stop_requested = True
        self.log('stop_requested', level='warn', signal=signum)

    def stop_file(self):
        return store.path('state', 'STOP')

    def should_stop(self):
        return self.stop_requested or os.path.exists(self.stop_file())

    # ----- one source -----
    def run_one(self, task):
        e = self.entry(task['id'])
        t0 = time.time()
        e['last_attempt'] = iso(now())
        res = adapters.run_task(task, self.fetcher, e, self.ctx)
        ms = int((time.time() - t0) * 1000)
        e.update(res.state)
        e['last_http'] = res.http_status
        new_items = 0
        new_obs = 0
        if res.items:
            new_items = store.store_items(res.items, self.seen)
        if res.observations:
            new_obs = self._store_observations(res.observations)
        interval = interval_hours(task)
        if res.skipped:
            e['status'] = 'skipped'
            e['last_error'] = res.skipped
            e['next_due'] = iso(now() + timedelta(hours=24))
            self.log('source_skipped', level='warn', source=task['id'], reason=res.skipped)
        elif res.error:
            fails = int(e.get('consecutive_failures', 0)) + 1
            e['consecutive_failures'] = fails
            e['status'] = 'failing' if fails >= 3 else 'retrying'
            e['last_error'] = res.error
            backoff = min(MAX_BACKOFF_H, max(0.5, interval / 4) * (2 ** (fails - 1)))
            e['next_due'] = iso(now() + timedelta(hours=backoff))
            self.log('source_failed', level='warn', source=task['id'], error=res.error, fails=fails,
                     retry_in_h=round(backoff, 1), ms=ms)
            self.status.setdefault('recent_errors', []).insert(0, {'ts': iso(now()), 'source': task['id'], 'error': res.error})
            self.status['recent_errors'] = self.status['recent_errors'][:15]
        else:
            e['status'] = 'ok'
            e['consecutive_failures'] = 0
            e['last_error'] = None
            e['last_success'] = iso(now())
            e['next_due'] = iso(now() + timedelta(hours=interval))
            e['items_total'] = int(e.get('items_total', 0)) + new_items
            e['obs_total'] = int(e.get('obs_total', 0)) + new_obs
            e['last_new'] = new_items + new_obs
            self.log('source_ok', source=task['id'], new_items=new_items, new_obs=new_obs,
                     note=res.note or None, ms=ms)
        self.save_state()
        return new_items, new_obs

    def _store_observations(self, observations):
        p = store.path('datasets', 'observations.jsonl')
        keys_path = store.path('state', 'obs_keys.txt')
        keys = set()
        if os.path.exists(keys_path):
            with open(keys_path, encoding='utf-8') as f:
                keys = set(f.read().splitlines())
        lines, new_keys = [], []
        for o in observations:
            k = f"{o['source_id']}|{o['indicator']}|{o['date']}|{o['value']}"
            if k in keys or k in new_keys:
                continue
            lines.append(json.dumps(o, ensure_ascii=False))
            new_keys.append(k)
        store.append_lines(p, lines)
        store.append_lines(keys_path, new_keys)
        return len(lines)

    # ----- a sweep over due sources -----
    def sweep(self, force=False, only=None, max_sources=None):
        tasks = [t for t in load_sources() if truthy(t.get('enabled', '1'))]
        if only:
            wanted = set(only)
            tasks = [t for t in tasks if t['id'] in wanted or t.get('kind') in wanted or t.get('adapter') in wanted]
        t = now()
        due = [x for x in tasks if force or self.due(x, t)]
        # oldest-due first, so a restart continues where the last run stopped
        due.sort(key=lambda x: self.state.get(x['id'], {}).get('next_due') or '')
        if max_sources:
            due = due[:max_sources]
        self.status.update({
            'state': 'sweeping', 'sweep_no': int(self.status.get('sweep_no', 0)) + 1,
            'sweep_started': iso(t), 'sweep_total': len(due), 'sweep_done': 0,
            'sweep_new_items': 0, 'sweep_new_obs': 0, 'current': None,
        })
        self.write_status(tasks)
        self.log('sweep_start', sweep=self.status['sweep_no'], due=len(due), enabled=len(tasks), force=force)
        crash_after = int(os.environ.get('HARVEST_TEST_CRASH_AFTER', '0') or 0)
        for i, task in enumerate(due, 1):
            if self.should_stop():
                raise Stop()
            self.status['current'] = task['id']
            self.write_status(tasks)
            ni, no = self.run_one(task)
            self.status['sweep_done'] = i
            self.status['sweep_new_items'] += ni
            self.status['sweep_new_obs'] += no
            self.status['current'] = None
            self.write_status(tasks)
            if crash_after and i >= crash_after:
                os._exit(3)  # used only by the self-test to simulate a crash
        self.status['state'] = 'idle'
        self.status['last_sweep_finished'] = iso(now())
        self.write_status(tasks)
        self.log('sweep_end', sweep=self.status['sweep_no'], done=len(due),
                 new_items=self.status['sweep_new_items'], new_obs=self.status['sweep_new_obs'])
        return len(due)

    def next_due_in(self):
        tasks = [t for t in load_sources() if truthy(t.get('enabled', '1'))]
        t = now()
        waits = []
        for x in tasks:
            nd = parse_iso(self.state.get(x['id'], {}).get('next_due'))
            waits.append(0 if nd is None else max(0, (nd - t).total_seconds()))
        return min(waits) if waits else 3600

    # ----- entry points -----
    def _start(self, mode):
        self.lock = store.Lock(self.log)
        self.lock.acquire()
        if os.path.exists(self.stop_file()):
            os.remove(self.stop_file())
        signal.signal(signal.SIGINT, self._handle_signal)
        signal.signal(signal.SIGTERM, self._handle_signal)
        self.seen = store.Seen()
        self.status.update({'pid': os.getpid(), 'mode': mode, 'started': iso(now()),
                            'harvester_version': HARVESTER_VERSION})
        self.log('harvester_start', mode=mode, pid=os.getpid(), version=HARVESTER_VERSION,
                 sources_known=len(self.state), items_known=len(self.seen.ids))

    def _finish(self, reason):
        self.status['state'] = 'stopped'
        self.status['stopped'] = iso(now())
        self.status['stop_reason'] = reason
        self.write_status()
        self.log('harvester_stop', reason=reason)
        self.lock.release()

    def run(self, force=False, only=None, max_sources=None):
        self._start('check' if force else 'run')
        try:
            self.sweep(force=force, only=only, max_sources=max_sources)
            self._finish('sweep complete')
        except Stop:
            self._finish('stop requested (resume with the same command)')

    def watch(self, min_sleep=300, max_sleep=3600):
        self._start('watch')
        try:
            while True:
                self.sweep()
                wait = min(max_sleep, max(min_sleep, self.next_due_in()))
                self.status.update({'state': 'sleeping', 'next_sweep': iso(now() + timedelta(seconds=wait))})
                self.write_status()
                end = time.time() + wait
                while time.time() < end:
                    if self.should_stop():
                        raise Stop()
                    self.status['heartbeat'] = iso(now())
                    store.write_atomic(store.path('status.json'), json.dumps(self.status, ensure_ascii=False, indent=1))
                    time.sleep(min(5, max(1, end - time.time())))
        except Stop:
            self._finish('stop requested (resume with the same command)')

    # ----- observability -----
    def write_status(self, tasks=None):
        tasks = tasks if tasks is not None else [t for t in load_sources() if truthy(t.get('enabled', '1'))]
        self.status['heartbeat'] = iso(now())
        counts = {'ok': 0, 'retrying': 0, 'failing': 0, 'skipped': 0, 'never_run': 0}
        for t in tasks:
            st = self.state.get(t['id'], {}).get('status') or 'never_run'
            counts[st] = counts.get(st, 0) + 1
        self.status['sources'] = counts
        self.status['sources_enabled'] = len(tasks)
        self.status['items_stored'] = len(self.seen.ids) if self.seen else self.status.get('items_stored')
        store.write_atomic(store.path('status.json'), json.dumps(self.status, ensure_ascii=False, indent=1))
        store.write_atomic(store.path('STATUS.md'), render_status_md(self.status, self.state, tasks))


def render_status_md(status, state, tasks):
    lines = ['# Harvester status', '',
             f"Updated: {status.get('heartbeat')} (UTC) · version {status.get('harvester_version')} · "
             f"mode {status.get('mode')} · state **{status.get('state')}** · pid {status.get('pid')}", '']
    if status.get('state') == 'sweeping':
        lines.append(f"Sweep {status.get('sweep_no')}: {status.get('sweep_done')}/{status.get('sweep_total')} sources, "
                     f"current: `{status.get('current')}`, new items {status.get('sweep_new_items')}, "
                     f"new observations {status.get('sweep_new_obs')}")
    elif status.get('next_sweep'):
        lines.append(f"Next sweep: {status.get('next_sweep')}")
    s = status.get('sources', {})
    lines += ['', f"Sources enabled: {status.get('sources_enabled')} — ok {s.get('ok', 0)}, retrying {s.get('retrying', 0)}, "
              f"failing {s.get('failing', 0)}, skipped (robots/key) {s.get('skipped', 0)}, never run {s.get('never_run', 0)}",
              f"Items stored in total: {status.get('items_stored')}", '']
    bad = [(t['id'], state.get(t['id'], {})) for t in tasks if state.get(t['id'], {}).get('status') in ('failing', 'skipped')]
    if bad:
        lines += ['## Sources needing attention', '', '| Source | Status | Last error | Last success |', '|---|---|---|---|']
        for sid, e in sorted(bad):
            lines.append(f"| {sid} | {e.get('status')} | {(e.get('last_error') or '')[:120]} | {e.get('last_success') or '—'} |")
        lines.append('')
    if status.get('recent_errors'):
        lines += ['## Recent errors', '']
        for r in status['recent_errors'][:10]:
            lines.append(f"- {r['ts']} `{r['source']}` — {r['error'][:150]}")
    return '\n'.join(lines) + '\n'


def disk_usage():
    total = 0
    root = store.path('x')
    for dp, _, files in os.walk(os.path.dirname(root)):
        for f in files:
            try:
                total += os.path.getsize(os.path.join(dp, f))
            except OSError:
                pass
    free = shutil.disk_usage(os.path.dirname(root)).free
    return total, free
