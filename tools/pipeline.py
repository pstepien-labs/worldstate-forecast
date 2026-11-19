#!/usr/bin/env python3
"""Pipeline guide and provenance recorder.

  python3 tools/pipeline.py status                   where the current edition is and the exact next step
  python3 tools/pipeline.py stage-start 03 --model M  record the start of a stage (commit, versions, prompt hash, model)
  python3 tools/pipeline.py stage-start 02 --arg G1 --model M
  python3 tools/pipeline.py stage-end 03             record the end of a stage
  python3 tools/pipeline.py stage-resume 03 --model M record that an interrupted stage is being continued
  python3 tools/pipeline.py provenance               render editions/<DIR>/provenance.md from provenance.jsonl
  python3 tools/pipeline.py register-edition         append the edition's row to registry/editions.csv (stage 08)
  python3 tools/pipeline.py versions                 framework, methodology, harvester versions and git state

Every report must be traceable to the framework version (VERSION), the
methodology version, the git commit and the prompt files that produced it,
and to the model that ran each stage. Learning prompts (prompts/learning/)
group results by these versions.

Python standard library only.
"""
import argparse
import csv
import hashlib
import json
import os
import re
import subprocess
import sys
from datetime import datetime, timedelta, timezone

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

STAGES = {
    '00': ('prompts/00_start_edition.md', 'Start of edition'),
    'H': ('prompts/H_harvest.md', 'Harvest digest'),
    '01': ('prompts/01_resolutions.md', 'Resolutions and scores'),
    '02': ('prompts/02_collection.md', 'Fact collection'),
    '03': ('prompts/03_analysis.md', 'Analysis and question bank'),
    '04': ('prompts/04_forecasts.md', 'Forecasts of one lens'),
    '05': ('prompts/05_red_team.md', 'Red team'),
    '06': ('prompts/06_aggregation_and_benchmarks.md', 'Aggregation, freezing, benchmarks'),
    '07': ('prompts/07_report.md', 'Report'),
    '08': ('prompts/08_quality_control.md', 'Quality control'),
    'M': ('prompts/M_mini_retro.md', 'Mini-retrospective'),
    'Q': ('prompts/Q_quarterly_review.md', 'Quarterly review'),
    'S': ('prompts/S_social.md', 'Social drafts (X)'),
    'E': ('prompts/E_brief.md', 'Executive brief and social cards'),
    'I': ('prompts/I_interim.md', 'Interim resolutions between editions (autopilot)'),
    'R': ('prompts/R_replay.md', 'Replay of a lens prompt on a closed edition (evaluation only)'),
    'QE': ('prompts/Q_evidence.md', 'Evidence file for the quarterly review (autopilot)'),
    'V': ('prompts/V_autoverify.md', 'Independent re-check of resolutions awaiting verification (autopilot)'),
    'L1': ('prompts/learning/L1_hindsight.md', 'Learning: hindsight audit of reports'),
    'L2': ('prompts/learning/L2_forecast_performance.md', 'Learning: forecast performance'),
    'L3': ('prompts/learning/L3_reasoning_trace.md', 'Learning: reasoning trace of hits and misses'),
    'L4': ('prompts/learning/L4_sources_coverage.md', 'Learning: sources and coverage'),
    'L5': ('prompts/learning/L5_framework_proposals.md', 'Learning: framework proposals'),
}
S_MODES = ('watch', 'release', 'resolved', 'weekahead', 'event-pre', 'event-post', 'region', 'crosslink',
           'reply', 'bench', 'explainer')
EDITIONS_HEADER = ['edition', 'state_date', 'directory', 'framework_version', 'methodology_version', 'models',
                   'freeze_commit', 'report_commit', 'tag', 'harvest_manifest_sha', 'notes']


def sh(*args):
    try:
        return subprocess.run(args, cwd=ROOT, capture_output=True, text=True, timeout=30).stdout.strip()
    except Exception:
        return ''


def read(p, default=''):
    try:
        with open(os.path.join(ROOT, p), encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        return default


def sha(p):
    full = os.path.join(ROOT, p)
    if not os.path.exists(full):
        return None
    with open(full, 'rb') as f:
        return hashlib.sha256(f.read()).hexdigest()[:16]


def current():
    out = {}
    for line in read('editions/CURRENT.md').splitlines():
        m = re.match(r'^([A-Z_]+)=(.*)$', line.strip())
        if m:
            out[m.group(1)] = m.group(2).strip()
    return out


def framework_version():
    return read('VERSION').strip() or 'unknown'


def methodology_version(cur=None):
    cur = cur or current()
    return cur.get('METHODOLOGY') or 'v1.0'


def harvester_version():
    m = re.search(r"HARVESTER_VERSION = '([^']+)'", read('tools/harvester/__init__.py'))
    return m.group(1) if m else None


def dirty_paths():
    try:  # not sh(): stripping the output would cut the status column of the first line
        out = subprocess.run(['git', 'status', '--porcelain'], cwd=ROOT, capture_output=True, text=True, timeout=30).stdout
    except Exception:
        return []
    return [x[3:] for x in out.splitlines() if x.strip()]


SEQUENCE_STAGES = {'00', 'H', '01', '02', '03', '04', '05', '06', '07', '08'}


def now():
    return datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')


def prov_path(stage, cur):
    if stage.startswith('L') or stage in ('M', 'Q', 'QE', 'R'):
        return os.path.join(ROOT, 'reviews', 'learning', 'provenance.jsonl')
    if stage == 'S':
        return os.path.join(ROOT, 'social', 'provenance.jsonl')
    return os.path.join(ROOT, cur['DIRECTORY'], 'provenance.jsonl')


def record(event, stage, arg, model, note):
    stage = stage.upper() if stage.upper() in STAGES else stage
    if stage not in STAGES:
        sys.exit(f'unknown stage {stage}; known: {", ".join(STAGES)}')
    if stage == 'S' and (arg or 'watch').split()[0] not in S_MODES:
        sys.exit(f'unknown social mode {arg!r}; known: {", ".join(S_MODES)} (a target may follow, e.g. "event-pre Q-0083")')
    cur = current()
    prompt = STAGES[stage][0]
    rec = {
        'ts': now(), 'event': event, 'stage': stage, 'arg': arg or None, 'edition': cur.get('NR'),
        'model': model or None,
        'framework_version': framework_version(), 'methodology_version': methodology_version(cur),
        'harvester_version': harvester_version(),
        'commit': sh('git', 'rev-parse', '--short=12', 'HEAD') or None,
        'dirty_files': len(dirty_paths()),
        'dirty_paths': dirty_paths()[:50],
        'prompt_file': prompt, 'prompt_sha': sha(prompt), 'claude_md_sha': sha('CLAUDE.md'),
        'methodology_sha': sha(f"methodology/methodology_{methodology_version(cur)}.md"),
        'claude_cli': sh('claude', '--version') or None,
        'note': note or None,
    }
    if cur.get('DIRECTORY'):
        rec['harvest_manifest_sha'] = sha(os.path.join(cur['DIRECTORY'], '02_harvest', 'manifest.json'))
    p = prov_path(stage, cur)
    os.makedirs(os.path.dirname(p), exist_ok=True)
    with open(p, 'a', encoding='utf-8') as f:
        f.write(json.dumps(rec, ensure_ascii=False) + '\n')
    if event in ('start', 'resume') and not model:
        print('WARNING: no --model given; record the model id (e.g. from /model) for provenance.')
    print(f"{event}: stage {stage}{' ' + arg if arg else ''} · framework {rec['framework_version']} · "
          f"methodology {rec['methodology_version']} · commit {rec['commit']} · model {rec['model']}")
    if event == 'end':
        render_provenance(quiet=True)


def load_prov(cur):
    p = os.path.join(ROOT, cur.get('DIRECTORY', ''), 'provenance.jsonl')
    out = []
    if os.path.exists(p):
        with open(p, encoding='utf-8') as f:
            for line in f:
                try:
                    out.append(json.loads(line))
                except json.JSONDecodeError:
                    pass
    return out


def render_provenance(quiet=False):
    cur = current()
    recs = load_prov(cur)
    if not recs:
        if not quiet:
            print('no provenance records yet')
        return
    starts = {}
    resumes = {}
    rows = []
    for r in recs:
        key = (r['stage'], r.get('arg'))
        if r['event'] == 'start':
            starts[key] = r
            resumes[key] = []
        elif r['event'] == 'resume':
            resumes.setdefault(key, []).append(r['ts'])
        elif r['event'] == 'end':
            s = starts.pop(key, None)
            rows.append((s, r, resumes.pop(key, [])))
    for key, s in starts.items():
        rows.append((s, None, resumes.pop(key, [])))
    fw = sorted({r['framework_version'] for r in recs})
    mv = sorted({r['methodology_version'] for r in recs})
    models = sorted({r['model'] for r in recs if r.get('model')})
    lines = [f"# Provenance — edition {cur.get('NR')}", '',
             f'Framework version(s): {", ".join(fw)} · methodology: {", ".join(mv)} · models: {", ".join(models) or "not recorded"}', '']
    if len(fw) > 1 or len(mv) > 1:
        lines += ['**Warning:** more than one framework or methodology version was used within this edition. '
                  'Learning analyses must treat this edition as mixed.', '']
    lines += ['| Stage | Arg | Start (UTC) | Resumed (UTC) | End (UTC) | Model | Framework | Commit at start | Prompt sha | Dirty files at start |',
              '|---|---|---|---|---|---|---|---|---|---|']
    for s, e, res in rows:
        s = s or {}
        dirty = s.get('dirty_files')
        if s.get('dirty_paths'):
            dirty = f"{dirty}: {', '.join(s['dirty_paths'])}"
        lines.append(f"| {s.get('stage') or e.get('stage')} | {s.get('arg') or ''} | {s.get('ts', '—')} | "
                     f"{', '.join(res) or '—'} | {e['ts'] if e else 'not finished'} | {s.get('model') or '—'} | "
                     f"{s.get('framework_version')} | {s.get('commit')} | {s.get('prompt_sha')} | {dirty} |")
    p = os.path.join(ROOT, cur['DIRECTORY'], 'provenance.md')
    with open(p, 'w', encoding='utf-8') as f:
        f.write('\n'.join(lines) + '\n')
    if not quiet:
        print('\n'.join(lines))


def edition_framework(recs):
    """Framework version (tuple) of the first provenance record of an edition; (0,) if unknown."""
    for r in recs:
        v = r.get('framework_version')
        if v:
            try:
                return tuple(int(x) for x in v.split('.')[:3])
            except ValueError:
                return (0,)
    return tuple(int(x) for x in framework_version().split('.')[:3]) if not recs else (0,)


def edition_done_map(cur):
    """Which stages are complete in the current edition (provenance first, files as fallback)."""
    d = os.path.join(ROOT, cur.get('DIRECTORY', ''))
    recs = load_prov(cur)
    ended = {(r['stage'], r.get('arg')) for r in recs if r['event'] == 'end'}
    # Editions run before provenance existed are judged by their output files. Off-sequence records
    # (e.g. a later "H repair") must not switch that fallback off.
    file_fallback = not any(r['stage'] in SEQUENCE_STAGES and r.get('arg') != 'repair' for r in recs)

    def has(*files):
        return all(os.path.exists(os.path.join(d, f)) for f in files)

    def done(stage, arg=None, files=()):
        return (stage, arg) in ended or (bool(files) and has(*files) and file_fallback)

    nr = cur.get('NR', '00')
    tag = f'edition-{nr}'
    tags = sh('git', 'tag').split()
    steps = [
        ('00', None, '/g00 <STATE_DATE> <NR>', done('00', None, ['00_plan.md'])),
        ('H', 'digest', '/gH digest', done('H', 'digest', ['02_harvest/manifest.json'])),
        ('01', None, '/g01', done('01', None, ['01_resolutions.md'])),
    ]
    for g in ('G1', 'G2', 'G3', 'G4'):
        steps.append(('02', g, f'/g02 {g}', done('02', g, [f'02_facts/{g}.md'])))
    steps.append(('03', None, '/g03', done('03', None, ['03_analysis.md'])))
    for lens in ('A', 'B', 'C'):
        steps.append(('04', lens, f'/g04 {lens}', done('04', lens, [f'04_forecasts_{lens}.md'])))
    if edition_framework(recs) >= (1, 9, 0):  # shadow run B2 (framework 1.9, WP-11): editions started on 1.9+
        steps.append(('04', 'B2', '/g04 B2', done('04', 'B2', ['04_forecasts_B2.md'])))
    steps += [
        ('05', None, '/g05', done('05', None, ['05_red_team.md'])),
        ('06', None, '/g06', done('06', None, ['06_aggregation.md', '06_benchmarks.md'])),
        ('07', None, '/g07', done('07', None, ['07_report.md'])),
        ('08', None, '/g08', done('08', None, ['08_quality_control.md']) and (tag in tags or 'wydanie-' + nr in tags)),
    ]
    return steps


def harvester_line():
    data = os.environ.get('HARVEST_DATA') or os.path.join(ROOT, 'data', 'harvest')
    try:
        st = json.load(open(os.path.join(data, 'status.json'), encoding='utf-8'))
        lock = json.load(open(os.path.join(data, 'state', 'harvester.lock'), encoding='utf-8')) \
            if os.path.exists(os.path.join(data, 'state', 'harvester.lock')) else None
    except (FileNotFoundError, json.JSONDecodeError):
        return 'Harvester: never run on this machine. Start it: `scripts/harvest.sh start` (see RUNBOOK.md, step 3).'
    alive = False
    if lock:
        try:
            os.kill(int(lock['pid']), 0)
            alive = True
        except (OSError, ValueError):
            alive = False
    s = st.get('sources', {})
    return (f"Harvester: {'RUNNING' if alive else 'NOT RUNNING'} · state {st.get('state')} · heartbeat {st.get('heartbeat')} · "
            f"sources ok {s.get('ok', 0)}/{st.get('sources_enabled')} · failing {s.get('failing', 0)} · items {st.get('items_stored')}"
            + ('' if alive else ' — restart with `scripts/harvest.sh start` (it resumes)'))


MIN_GAP_DAYS = 14  # editions are two-weekly (methodology §1; README schedule)

STAGE_TEXT = {
    '00': 'Start the edition: plan, calendar, versions, and the harvest digest',
    'H': 'Build the harvest digest for the edition window',
    '01': 'Resolve questions whose deadline has passed and compute accuracy scores',
    '02': 'Collect and verify facts for one group of topics',
    '03': 'Analysis and question bank',
    '04': 'Blind forecast by one lens',
    '05': 'Red team: challenge the analysis and the forecasts',
    '06': 'Aggregate, freeze the forecasts, then collect benchmarks',
    '07': 'Write the report',
    '08': 'Quality control, tag and register the edition',
}


def compute_state():
    """Everything a human or the /edition orchestrator needs to decide the next step."""
    cur = current()
    today = datetime.now(timezone.utc).date()
    st = {'today': today.isoformat(), 'framework_version': framework_version(),
          'methodology_version': methodology_version(cur), 'harvester': harvester_line(),
          'edition': cur.get('NR'), 'state_date': cur.get('STATE_DATE'), 'directory': cur.get('DIRECTORY'),
          'steps': [], 'next': None, 'edition_closed': False}
    if not cur.get('DIRECTORY'):
        st['next'] = {'stage': '00', 'arg': f'{today.isoformat()} 01', 'cmd': f'/g00 {today.isoformat()} 01'}
        return st
    steps = edition_done_map(cur)
    if steps[-1][3]:  # edition closed (stage 08 done and tagged): earlier gaps are historical
        steps = [(s_, a_, c_, True) for s_, a_, c_, _ in steps]
    for stage, arg, cmd, ok in steps:
        st['steps'].append({'stage': stage, 'arg': arg, 'cmd': cmd, 'done': ok})
        if not ok and st['next'] is None:
            st['next'] = {'stage': stage, 'arg': arg, 'cmd': cmd, 'prompt': STAGES[stage][0], 'what': STAGE_TEXT.get(stage, '')}
    if st['next'] is None:
        st['edition_closed'] = True
        # after stage 08: executive brief and social cards (stage E), before the release drafts
        nr_ = cur.get('NR', '00')
        # autopilot (framework 1.8): the public page rebuilt for this edition, and resolutions still awaiting a check
        st['site_done'] = bool(sh('git', 'log', '-1', '--format=%h', '--extended-regexp',
                                  f'--grep=^edition-{nr_} site'))
        st['publish_blocked'] = critical_open(os.path.join(ROOT, cur['DIRECTORY'], '08_quality_control.md'))
        st['brief_done'] = all(os.path.exists(os.path.join(ROOT, 'docs', 'briefs', f'edition-{nr_}.{x}')) for x in ('html', 'pdf')) \
            and os.path.isdir(os.path.join(ROOT, 'social', 'cards', f'edition-{nr_}'))
        prev = datetime.strptime(cur['STATE_DATE'], '%Y-%m-%d').date()
        earliest = prev + timedelta(days=MIN_GAP_DAYS)
        nr = f"{int(cur.get('NR', '0')) + 1:02d}"
        st['next_edition'] = nr
        st['earliest_state_date'] = earliest.isoformat()
        st['can_start_next_edition'] = today >= earliest
        st['suggested_state_date'] = today.isoformat() if today >= earliest else earliest.isoformat()
        st['days_to_wait'] = max(0, (earliest - today).days)
        st['next'] = {'stage': '00', 'arg': f"{st['suggested_state_date']} {nr}", 'cmd': f"/g00 {st['suggested_state_date']} {nr}",
                      'prompt': STAGES['00'][0], 'what': STAGE_TEXT['00']}
    pend = pending_verification()
    st['pending_verification'] = pend['unchecked']
    st['verification_disputed'] = pend['disputed']
    st['unpushed_commits'] = int(sh('git', 'rev-list', '--count', '@{u}..HEAD') or 0)
    if st['next'] is not None and not st['edition_closed'] and st['next']['stage'] == 'H' \
            and cur.get('STATE_DATE', '9999') > today.isoformat():
        st['waiting_reason'] = f"the state date {cur['STATE_DATE']} is in the future; keep harvesting until then"
    return st


def critical_open(path):
    """Stage 08 (framework 1.9) writes 'Critical discrepancies open: N'. True if N > 0 (publication gate)."""
    try:
        with open(path, encoding='utf-8') as f:
            m = re.search(r'Critical discrepancies open:\s*\**\s*(\d+)', f.read(), re.I)
    except OSError:
        return False
    return bool(m and int(m.group(1)) > 0)


def pending_verification():
    """Resolutions flagged VERIFY whose latest row is neither approved (Y) nor auto-verified (A).
    'unchecked': no stage V row yet (stage V may check them); 'disputed': stage V disagreed (user decides)."""
    path = os.path.join(ROOT, 'registry', 'resolutions.csv')
    if not os.path.exists(path):
        return {'unchecked': [], 'disputed': []}
    with open(path, encoding='utf-8-sig', newline='') as f:
        rows = list(csv.DictReader(f, delimiter=';'))
    latest, checked = {}, set()
    for r in rows:
        q = r['question_id']
        if 'autoverify' in (r.get('notes') or '').lower():
            checked.add(q)
        if q not in latest or int(r['version']) > int(latest[q]['version']):
            latest[q] = r
    out = {'unchecked': [], 'disputed': []}
    for q, r in sorted(latest.items()):
        if r.get('verify', '').strip().upper() == 'Y' and r.get('user_approved', '').strip().upper() not in ('Y', 'A') \
                and r['outcome'].strip().upper() != 'VOID':
            out['disputed' if q in checked else 'unchecked'].append(q)
    return out


def fmt_date(iso_date):
    return datetime.strptime(iso_date, '%Y-%m-%d').strftime('%d.%m.%Y')


def cmd_status(a):
    st = compute_state()
    if getattr(a, 'json', False):
        print(json.dumps(st, ensure_ascii=False, indent=1))
        return
    print(f"Framework {st['framework_version']} · methodology {st['methodology_version']} · harvester {harvester_version()} · "
          f"commit {sh('git', 'rev-parse', '--short', 'HEAD')} · branch {sh('git', 'rev-parse', '--abbrev-ref', 'HEAD')}")
    print(st['harvester'])
    if st['directory']:
        print(f"\nEdition {st['edition']} · state date {fmt_date(st['state_date'])} · {st['directory']}\n")
        for x in st['steps']:
            mark = 'done' if x['done'] else ('NEXT' if st['next'] and not st['edition_closed'] and x['stage'] == st['next']['stage'] and x['arg'] == st['next']['arg'] else 'todo')
            label = (x['stage'] + (' ' + x['arg'] if x['arg'] else '')).ljust(9)
            print(f"  [{mark:4}] {label} {x['cmd']}")
        print()
    if st['edition_closed']:
        e, nr = st['earliest_state_date'], st['next_edition']
        print(f"Edition {st['edition']} is finished (report: {st['directory']}/07_report.md).")
        if not st['brief_done']:
            print(f"Executive brief and cards of edition {st['edition']} are missing: run /gE (prompts/E_brief.md).")
        if st['can_start_next_edition']:
            print(f"You can produce edition {nr} now. Type: /edition   (it uses today, {fmt_date(st['today'])}, as the state date)")
        else:
            print(f"Edition {nr} can start on or after {fmt_date(e)}: editions are two weeks apart, counted from edition "
                  f"{st['edition']}'s state date ({fmt_date(st['state_date'])}). That is {st['days_to_wait']} day(s) from today. "
                  f"Until then keep the harvester running; on that day type: /edition")
        return
    if st.get('waiting_reason'):
        print(f"Waiting: {st['waiting_reason']}.")
        return
    nx = st['next']
    print(f"Edition {st['edition']} is in progress. To continue everything automatically type: /edition")
    print(f"(Manual mode: next stage is {nx['cmd']} — {nx['what']}; one stage per session, /clear first.)")


def cmd_register(a):
    cur = current()
    nr = cur.get('NR')
    path = os.path.join(ROOT, 'registry', 'editions.csv')
    rows = []
    if os.path.exists(path):
        with open(path, encoding='utf-8-sig', newline='') as f:
            rows = list(csv.DictReader(f, delimiter=';'))
    if any(r['edition'] == nr for r in rows):
        print(f'edition {nr} is already registered (append-only: add a correction row with notes if needed)')
        return
    recs = load_prov(cur)
    models = sorted({r['model'] for r in recs if r.get('model')})
    fws = sorted({r['framework_version'] for r in recs}) or [framework_version()]
    freeze = sh('git', 'log', '--format=%h', '-1', f'--grep=edition-{nr} forecasts frozen')
    report = sh('git', 'log', '--format=%h', '-1', '--', os.path.join(cur['DIRECTORY'], '07_report.md'))
    row = {'edition': nr, 'state_date': cur.get('STATE_DATE'), 'directory': cur.get('DIRECTORY'),
           'framework_version': '+'.join(fws), 'methodology_version': methodology_version(cur),
           'models': '+'.join(models) or 'not recorded', 'freeze_commit': freeze, 'report_commit': report,
           'tag': f'edition-{nr}', 'harvest_manifest_sha': sha(os.path.join(cur['DIRECTORY'], '02_harvest', 'manifest.json')) or '',
           'notes': a.notes or ''}
    new_file = not os.path.exists(path)
    with open(path, 'a', encoding='utf-8-sig' if new_file else 'utf-8', newline='') as f:
        w = csv.DictWriter(f, fieldnames=EDITIONS_HEADER, delimiter=';', quoting=csv.QUOTE_NONNUMERIC)
        if new_file:
            w.writeheader()
        w.writerow(row)
    print('registered:', row)


FORECAST_RUNS_APPENDABLE = {'A', 'B', 'C', 'B2', 'AGG', 'AGG_RT', 'QNT'}


def cmd_lens_rows(a):
    """Header and the rows of one run only (a lens sees its own earlier forecasts, nothing else; rule 3.8)."""
    p = os.path.join(ROOT, 'registry', 'forecasts.csv')
    with open(p, encoding='utf-8-sig', newline='') as f:
        rows = list(csv.reader(f, delimiter=';'))
    i = rows[0].index('run')
    w = csv.writer(sys.stdout, delimiter=';', quoting=csv.QUOTE_NONNUMERIC, lineterminator='\n')
    w.writerow(rows[0])
    for r in rows[1:]:
        if len(r) > i and r[i] == a.run:
            w.writerow(r)


def cmd_append_forecasts(a):
    """Validate a CSV of forecast rows (registry header, optional) and append it to registry/forecasts.csv."""
    p = os.path.join(ROOT, 'registry', 'forecasts.csv')
    with open(p, encoding='utf-8-sig', newline='') as f:
        header = next(csv.reader(f, delimiter=';'))
    with open(a.file, encoding='utf-8-sig', newline='') as f:
        rows = [r for r in csv.reader(f, delimiter=';') if r]
    if rows and rows[0] == header:
        rows = rows[1:]
    qids = set()
    with open(os.path.join(ROOT, 'registry', 'questions.csv'), encoding='utf-8-sig', newline='') as f:
        qids = {q['id'] for q in csv.DictReader(f, delimiter=';')}
    errors = []
    idx = {k: header.index(k) for k in ('question_id', 'edition', 'date', 'run', 'p')}
    for n, r in enumerate(rows, 1):
        if len(r) != len(header):
            errors.append(f'row {n}: {len(r)} fields, expected {len(header)}')
            continue
        if r[idx['question_id']] not in qids:
            errors.append(f"row {n}: unknown question {r[idx['question_id']]}")
        if r[idx['run']] not in FORECAST_RUNS_APPENDABLE or (a.run and r[idx['run']] != a.run):
            errors.append(f"row {n}: run {r[idx['run']]!r} not allowed here")
        try:
            pv = float(r[idx['p']])
            if not 0.01 <= pv <= 0.99:
                errors.append(f'row {n}: p {pv} outside 0.01-0.99')
        except ValueError:
            errors.append(f"row {n}: p {r[idx['p']]!r} is not a number")
        if not re.match(r'^\d{4}-\d{2}-\d{2}$', r[idx['date']]):
            errors.append(f"row {n}: date {r[idx['date']]!r} is not YYYY-MM-DD")
    if errors:
        sys.exit('append-forecasts refused:\n  ' + '\n  '.join(errors[:30]))
    with open(p, 'a', encoding='utf-8', newline='') as f:
        w = csv.writer(f, delimiter=';', quoting=csv.QUOTE_ALL, lineterminator='\n')
        for r in rows:
            w.writerow(r)
    print(f'appended {len(rows)} rows to registry/forecasts.csv')


def cmd_cutoff(a):
    """INFO_CUTOFF of the current edition as YYYY-MM-DD (first line of 03_analysis.md), for stages that may not open it."""
    cur = current()
    try:
        with open(os.path.join(ROOT, cur['DIRECTORY'], '03_analysis.md'), encoding='utf-8') as f:
            first = f.readline()
    except (OSError, KeyError):
        sys.exit('no 03_analysis.md in the current edition yet')
    m = re.search(r'(\d{2})\.(\d{2})\.(\d{4})', first)
    if not m:
        sys.exit('INFO_CUTOFF line not found')
    print(f'{m.group(3)}-{m.group(2)}-{m.group(1)}')


def cmd_versions(a):
    cur = current()
    print(json.dumps({'framework_version': framework_version(), 'methodology_version': methodology_version(cur),
                      'harvester_version': harvester_version(), 'commit': sh('git', 'rev-parse', '--short=12', 'HEAD'),
                      'branch': sh('git', 'rev-parse', '--abbrev-ref', 'HEAD'),
                      'dirty_files': len(dirty_paths()), 'dirty_paths': dirty_paths()[:50],
                      'edition': cur.get('NR'), 'claude_cli': sh('claude', '--version') or None}, indent=1))


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = p.add_subparsers(dest='cmd', required=True)
    stp = sub.add_parser('status')
    stp.add_argument('--json', action='store_true', help='machine-readable state (used by /edition)')
    stp.set_defaults(fn=cmd_status)
    for ev in ('stage-start', 'stage-end', 'stage-resume'):
        s = sub.add_parser(ev)
        s.add_argument('stage')
        s.add_argument('--arg')
        s.add_argument('--model')
        s.add_argument('--note')
        s.set_defaults(fn=lambda a, ev=ev: record(ev.split('-')[1], a.stage, a.arg, a.model, a.note))
    sub.add_parser('provenance').set_defaults(fn=lambda a: render_provenance())
    r = sub.add_parser('register-edition')
    r.add_argument('--notes')
    r.set_defaults(fn=cmd_register)
    sub.add_parser('versions').set_defaults(fn=cmd_versions)
    sub.add_parser('cutoff', help='INFO_CUTOFF date of the current edition').set_defaults(fn=cmd_cutoff)
    lr = sub.add_parser('lens-rows', help='header + rows of one run of registry/forecasts.csv (rule 3.8)')
    lr.add_argument('run')
    lr.set_defaults(fn=cmd_lens_rows)
    af = sub.add_parser('append-forecasts', help='validate and append forecast rows from a CSV file')
    af.add_argument('file')
    af.add_argument('--run', help='require every row to have this run')
    af.set_defaults(fn=cmd_append_forecasts)
    a = p.parse_args()
    a.fn(a)


if __name__ == '__main__':
    main()
