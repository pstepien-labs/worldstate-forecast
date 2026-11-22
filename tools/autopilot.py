#!/usr/bin/env python3
"""Decision logic of the autopilot (framework 1.9, P-0013..P-0016). Called by scripts/autopilot.sh.

  python3 tools/autopilot.py decide              next action for this tick: "<action> <reason>"
  python3 tools/autopilot.py heartbeat           write docs/data/autopilot.json if its content changed (exit 1 = unchanged)
  python3 tools/autopilot.py state-get KEY [DEFAULT]
  python3 tools/autopilot.py state-set KEY VALUE  (VALUE as JSON, else a string)
  python3 tools/autopilot.py result FILE         classify a headless run log: ok | limit <iso> | blocked | failed
  python3 tools/autopilot.py conf KEY [DEFAULT]  a value from autopilot.conf (environment variables win)
  python3 tools/autopilot.py classify-paths      (paths on stdin) protected | not-auto | replay | ok  (framework 1.10)
  python3 tools/autopilot.py replay-edition      latest closed edition with >= 30 questions resolved after it
  python3 tools/autopilot.py replay-score NN F   n and Brier of a replay file on that edition

Actions, in priority order:
  none (backing off / blocked / model mismatch), edition (resume, finish brief/site, or start when due),
  learn (L1-L5 reports after an edition), interim (resolutions in the off-week), repair (weekly source repair),
  qprep (evidence file for the quarterly review), none.
The logic is a pure function of (status, state, conf, now, provenance), so tests/test_autopilot.py can drive it.
Python standard library only.
"""
import json
import os
import re
import sys
from datetime import date, datetime, timedelta, timezone

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
DATA = os.path.join(ROOT, 'data', 'autopilot')
STATUS = os.path.join(DATA, 'status.json')
STATE = os.path.join(DATA, 'state.json')
CONF = os.path.join(ROOT, 'autopilot.conf')
HEARTBEAT = os.path.join(ROOT, 'docs', 'data', 'autopilot.json')
INBOX = os.path.join(ROOT, 'AUTOPILOT_INBOX.md')

DEFAULTS = {
    'AUTOPILOT_MODEL': 'claude-opus-5-5',
    'AUTOPILOT_START_HOUR': '20',
    'AUTOPILOT_REPAIR_DOW': '7',
    'AUTOPILOT_INTERIM_AFTER_DAYS': '7',
    'AUTOPILOT_QPREP_FROM': '2026-12-19',
    'AUTOPILOT_REPAIR_MIN_FAILING': '3',
    'AUTOPILOT_IMPROVE_MIN_DAYS_BEFORE_DUE': '2',
    'AUTOPILOT_NOISE_FLOOR': '0.011',
    'AUTOPILOT_REPLAY_MIN_RESOLVED': '30',
}

# Files an automatic improvement may never change (framework 1.10, user decision 20.11.2026;
# framework 2.0: every methodology version file and the driver list of methodology v1.1).
PROTECTED = ('CLAUDE.md', 'methodology/methodology_v', 'registry/', 'world_model/drivers.csv', 'tools/blindness_guard.py',
             'tools/registry_guard.py', 'tools/autopilot.py', 'scripts/autopilot.sh', '.claude/', '.github/',
             'editions/', 'docs/', 'autopilot.conf', 'AUTOPILOT_INBOX.md')
# Changes to these need the replay gate (they change how forecasts are made and can be replayed).
REPLAY_GATED = ('prompts/04_forecasts.md',)
# Changes to these change forecasting but cannot be replayed: they wait for the user / quarterly review.
NOT_AUTO = ('prompts/03_analysis.md', 'prompts/W_world_model.md', 'prompts/05_red_team.md', 'prompts/06_aggregation_and_benchmarks.md',
            'tools/scores.py', 'tools/quant.py', 'tools/coherence.py', 'methodology/')


# ---------- configuration and state ----------

def load_conf(path=CONF, env=None):
    env = os.environ if env is None else env
    conf = dict(DEFAULTS)
    if os.path.exists(path):
        with open(path, encoding='utf-8') as f:
            for line in f:
                line = line.split('#', 1)[0].strip()
                if '=' in line:
                    k, v = line.split('=', 1)
                    conf[k.strip()] = v.strip().strip('"').strip("'")
    for k in list(conf):
        if env.get(k):
            conf[k] = env[k]
    return conf


def load_json(path, default=None):
    try:
        with open(path, encoding='utf-8') as f:
            return json.load(f)
    except (OSError, ValueError):
        return {} if default is None else default


def save_json(path, data):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    tmp = path + '.tmp'
    with open(tmp, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=1, ensure_ascii=False)
    os.replace(tmp, path)


def edition_model(root, directory):
    """Model of the first provenance record of an edition that names one (None if none)."""
    p = os.path.join(root, directory or '', 'provenance.jsonl')
    try:
        with open(p, encoding='utf-8') as f:
            for line in f:
                try:
                    m = json.loads(line).get('model')
                except ValueError:
                    continue
                if m:
                    return m
    except OSError:
        pass
    return None


def failing_sources(harvester_line):
    m = re.search(r'failing (\d+)', harvester_line or '')
    return int(m.group(1)) if m else 0


# ---------- the decision ----------

def decide(st, state, conf, now, root=ROOT):
    """Return (action, reason). `now` is local naive datetime."""
    start_hour = int(conf['AUTOPILOT_START_HOUR'])
    # 1. waiting for a usage-limit reset (not a failure)
    until = state.get('wait_until')
    if until:
        try:
            if now < datetime.fromisoformat(until):
                return 'none', f'waiting for the usage limit to reset at {until}'
        except ValueError:
            pass
    # 2. back-off after failed runs: 1, 2, 4, 8, 16, 24 hours
    fails = int(state.get('consecutive_failures', 0) or 0)
    if fails:
        wait_h = min(24, 2 ** (fails - 1))
        try:
            last = datetime.fromisoformat(state.get('last_run_end') or '2000-01-01T00:00:00')
        except ValueError:
            last = datetime(2000, 1, 1)
        if (now - last).total_seconds() < wait_h * 3600 - 300:
            return 'none', f'backing off {wait_h}h after {fails} failed run(s)'
    # 3. an open edition: resume it, with the model it started with
    if not st.get('edition_closed'):
        started = edition_model(root, st.get('directory'))
        if started and started != conf['AUTOPILOT_MODEL']:
            return 'none', (f"model mismatch: edition {st.get('edition')} started with {started}, "
                            f"autopilot.conf names {conf['AUTOPILOT_MODEL']}; finish it with the same model")
        nx = st.get('next') or {}
        return 'edition', f"resume edition {st.get('edition')} at stage {nx.get('stage')} {nx.get('arg') or ''}".rstrip()
    if st.get('publish_blocked'):
        return 'none', f"publication of edition {st.get('edition')} blocked by a critical quality-control item (see AUTOPILOT_INBOX.md)"
    if not st.get('brief_done') or not st.get('site_done'):
        return 'edition', f"finish brief/site of edition {st.get('edition')}"
    # 4. the next edition: on its due date, from the start hour
    if st.get('can_start_next_edition') and now.hour >= start_hour:
        late = (now.date() - date.fromisoformat(st['earliest_state_date'])).days
        return 'edition', f"start edition {st['next_edition']} ({late} day(s) after the earliest date)"
    ed = st.get('edition')
    # 5. learning reports once per closed edition
    if state.get('learn_done_for') != ed and now.hour >= start_hour:
        return 'learn', f'learning reports L1-L5 for edition {ed}'
    # 5b. apply the learning proposals by policy, once per edition, not too close to the next edition
    try:
        to_due = (date.fromisoformat(st['earliest_state_date']) - now.date()).days
    except (KeyError, TypeError, ValueError):
        to_due = 0
    if state.get('learn_done_for') == ed and state.get('improve_done_for') != ed and now.hour >= start_hour \
            and to_due >= int(conf['AUTOPILOT_IMPROVE_MIN_DAYS_BEFORE_DUE']):
        return 'improve', f'apply learning proposals of edition {ed} by policy ({to_due} days before the next edition)'
    # 6. interim resolutions in the off-week
    try:
        days = (now.date() - date.fromisoformat(st['state_date'])).days
    except (KeyError, TypeError, ValueError):
        days = -1
    if days >= int(conf['AUTOPILOT_INTERIM_AFTER_DAYS']) and state.get('interim_done_for') != ed \
            and now.hour >= start_hour:
        return 'interim', f'interim resolutions {days} days after the state date of edition {ed}'
    # 7. weekly source repair
    week = now.strftime('%G-W%V')
    if now.isoweekday() == int(conf['AUTOPILOT_REPAIR_DOW']) and now.hour >= start_hour \
            and state.get('repair_week') != week:
        n = failing_sources(st.get('harvester'))
        if n >= int(conf['AUTOPILOT_REPAIR_MIN_FAILING']):
            return 'repair', f'{n} failing sources ({week})'
        return 'skip-repair', f'{n} failing sources, no repair needed ({week})'
    # 8. evidence file for the quarterly review
    if now.date() >= date.fromisoformat(conf['AUTOPILOT_QPREP_FROM']) and not state.get('qprep_done') \
            and now.hour >= start_hour:
        return 'qprep', 'evidence file for the quarterly review'
    return 'none', 'nothing due'


# ---------- run results ----------

LIMIT_RE = re.compile(r"hit your .*?limit.*?resets\s+(\d{1,2})(?::(\d{2}))?\s*([ap]m)?", re.I)


def classify(text, now):
    """Classify the output of a headless run: ('ok'|'blocked'|'failed', None) or ('limit', reset_iso)."""
    lines = [l for l in text.splitlines() if l.startswith('AUTOPILOT:')]
    last = lines[-1] if lines else ''
    if last.startswith('AUTOPILOT: complete') or last.startswith('AUTOPILOT: not-due'):
        return 'ok', None
    if last.startswith('AUTOPILOT: blocked'):
        return 'blocked', None
    m = LIMIT_RE.search(text)
    if m:
        h, mi, ap = int(m.group(1)), int(m.group(2) or 0), (m.group(3) or '').lower()
        if ap == 'pm' and h != 12:
            h += 12
        if ap == 'am' and h == 12:
            h = 0
        reset = now.replace(hour=h % 24, minute=mi, second=0, microsecond=0)
        if reset <= now:
            reset += timedelta(days=1)
        return 'limit', (reset + timedelta(minutes=5)).isoformat(timespec='minutes')
    if re.search(r"hit your .*limit", text, re.I):
        return 'limit', (now + timedelta(hours=1)).isoformat(timespec='minutes')
    return 'failed', None


# ---------- improvement gate (framework 1.10) ----------

def classify_paths(paths):
    """'protected' | 'not-auto' | 'replay' | 'ok' for the files one commit changes (worst wins)."""
    kinds = set()
    for p in paths:
        if p.startswith('methodology/methodology_changes.md') or p.startswith('reviews/'):
            kinds.add('ok')
        elif any(p == x or p.startswith(x) for x in PROTECTED):
            kinds.add('protected')
        elif p == 'methodology/methodology_changes.md':
            kinds.add('ok')
        elif any(p == x or p.startswith(x) for x in NOT_AUTO):
            kinds.add('not-auto')
        elif any(p == x for x in REPLAY_GATED):
            kinds.add('replay')
        else:
            kinds.add('ok')
    for k in ('protected', 'not-auto', 'replay'):
        if k in kinds:
            return k
    return 'ok'


def _registry(root):
    import csv
    R = lambda f: list(csv.DictReader(open(os.path.join(root, 'registry', f), encoding='utf-8-sig'), delimiter=';'))
    res = {}
    for r in R('resolutions.csv'):
        if r['question_id'] not in res or int(r['version']) > int(res[r['question_id']]['version']):
            res[r['question_id']] = r
    out = {q: int(r['outcome']) for q, r in res.items() if r['outcome'] in ('0', '1')
           and not (r.get('verify') == 'Y' and r.get('user_approved') not in ('Y', 'A'))}
    return R, res, out


def replay_edition(root=ROOT, min_resolved=30):
    """Latest closed edition with at least `min_resolved` AGG_RT questions resolved after its state date."""
    R, res, out = _registry(root)
    eds = {e['edition']: e['state_date'] for e in R('editions.csv') if e['edition'] not in ('00',)}
    fc = R('forecasts.csv')
    best = None
    for ed, sd in sorted(eds.items()):
        qs = {f['question_id'] for f in fc if f['edition'] == ed and f['run'] == 'AGG_RT'}
        n = sum(1 for q in qs if q in out and res[q]['resolution_date'] > sd)
        if n >= min_resolved:
            best = ed
    return best


def replay_score(edition, path, root=ROOT):
    """Brier of a replay file on the edition's questions resolved after its state date: (n, brier)."""
    import csv
    R, res, out = _registry(root)
    sd = {e['edition']: e['state_date'] for e in R('editions.csv')}[edition]
    rows = list(csv.DictReader(open(path, encoding='utf-8-sig'), delimiter=';'))
    sq = []
    for r in rows:
        q = r['question_id']
        if q in out and res[q]['resolution_date'] > sd:
            try:
                sq.append((float(r['p']) - out[q]) ** 2)
            except ValueError:
                pass
    return len(sq), (sum(sq) / len(sq) if sq else float('nan'))


def replay_gate(candidate, baseline, noise):
    """Accept if the candidate is no worse than the best baseline so far plus the noise floor."""
    return candidate <= baseline + noise


# ---------- heartbeat ----------

def heartbeat(st, state, inbox_text, old, now_utc):
    """Return the new heartbeat dict, or None if nothing changed and the old one is under 72 h old."""
    def count(section):
        m = re.search(r'## ' + section + r'\n(.*?)(\n## |\Z)', inbox_text or '', re.S)
        return len([l for l in (m.group(1) if m else '').splitlines() if l.strip().startswith('-')])
    hb = {'edition': st.get('edition'), 'state_date': st.get('state_date'), 'edition_closed': st.get('edition_closed'),
          'next_stage': None if st.get('edition_closed') else (st.get('next') or {}).get('cmd'),
          'earliest_next_edition': st.get('earliest_state_date'), 'last_result': state.get('last_result'),
          'consecutive_failures': state.get('consecutive_failures', 0), 'open_blockers': count('Blockers'),
          'waiting_for_user': count('Waiting for the user'),
          'resolutions_disputed': len(st.get('verification_disputed') or []),
          'publish_blocked': bool(st.get('publish_blocked')),
          'harvester': st.get('harvester'), 'framework_version': st.get('framework_version')}
    age_h = 1e9
    if old.get('updated'):
        try:
            age_h = (now_utc - datetime.fromisoformat(old['updated'].replace('Z', '+00:00'))).total_seconds() / 3600
        except ValueError:
            pass
    strip = lambda d: {k: v for k, v in d.items() if k not in ('updated', 'harvester')}
    if strip(old) == strip(hb) and age_h < 72:
        return None
    hb['updated'] = now_utc.strftime('%Y-%m-%dT%H:%M:%SZ')
    return hb


# ---------- command line ----------

def main(argv):
    if not argv:
        print(__doc__)
        return 2
    cmd, args = argv[0], argv[1:]
    if cmd == 'decide':
        action, reason = decide(load_json(STATUS), load_json(STATE), load_conf(), datetime.now())
        print(f'{action} {reason}')
        return 0
    if cmd == 'heartbeat':
        inbox = open(INBOX, encoding='utf-8').read() if os.path.exists(INBOX) else ''
        hb = heartbeat(load_json(STATUS), load_json(STATE), inbox, load_json(HEARTBEAT), datetime.now(timezone.utc))
        if hb is None:
            return 1
        save_json(HEARTBEAT, hb)
        return 0
    if cmd == 'state-get':
        v = load_json(STATE).get(args[0], args[1] if len(args) > 1 else '')
        print(json.dumps(v) if isinstance(v, (dict, list, bool)) else v)
        return 0
    if cmd == 'state-set':
        s = load_json(STATE)
        try:
            s[args[0]] = json.loads(args[1])
        except ValueError:
            s[args[0]] = args[1]
        save_json(STATE, s)
        return 0
    if cmd == 'result':
        with open(args[0], encoding='utf-8', errors='replace') as f:
            kind, until = classify(f.read(), datetime.now())
        print(kind if until is None else f'{kind} {until}')
        return 0
    if cmd == 'classify-paths':
        print(classify_paths([x for x in sys.stdin.read().split() if x]))
        return 0
    if cmd == 'replay-edition':
        print(replay_edition(min_resolved=int(load_conf()['AUTOPILOT_REPLAY_MIN_RESOLVED'])) or '')
        return 0
    if cmd == 'replay-score':
        n, b = replay_score(args[0], args[1])
        print(f'{n} {b:.4f}')
        return 0
    if cmd == 'conf':
        print(load_conf().get(args[0], args[1] if len(args) > 1 else ''))
        return 0
    print(__doc__)
    return 2


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
