#!/usr/bin/env python3
"""Pipeline guide and provenance recorder.

  python3 tools/pipeline.py status                   where the current edition is and the exact next step
  python3 tools/pipeline.py stage-start 03 --model M  record the start of a stage (commit, versions, prompt hash, model)
  python3 tools/pipeline.py stage-start 02 --arg G1 --model M
  python3 tools/pipeline.py stage-end 03             record the end of a stage
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
from datetime import datetime, timezone

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
    'L1': ('prompts/learning/L1_hindsight.md', 'Learning: hindsight audit of reports'),
    'L2': ('prompts/learning/L2_forecast_performance.md', 'Learning: forecast performance'),
    'L3': ('prompts/learning/L3_reasoning_trace.md', 'Learning: reasoning trace of hits and misses'),
    'L4': ('prompts/learning/L4_sources_coverage.md', 'Learning: sources and coverage'),
    'L5': ('prompts/learning/L5_framework_proposals.md', 'Learning: framework proposals'),
}
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


def now():
    return datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')


def prov_path(stage, cur):
    if stage.startswith('L') or stage in ('M', 'Q'):
        return os.path.join(ROOT, 'reviews', 'learning', 'provenance.jsonl')
    return os.path.join(ROOT, cur['DIRECTORY'], 'provenance.jsonl')


def record(event, stage, arg, model, note):
    stage = stage.upper() if stage.upper() in STAGES else stage
    if stage not in STAGES:
        sys.exit(f'unknown stage {stage}; known: {", ".join(STAGES)}')
    cur = current()
    prompt = STAGES[stage][0]
    rec = {
        'ts': now(), 'event': event, 'stage': stage, 'arg': arg or None, 'edition': cur.get('NR'),
        'model': model or None,
        'framework_version': framework_version(), 'methodology_version': methodology_version(cur),
        'harvester_version': harvester_version(),
        'commit': sh('git', 'rev-parse', '--short=12', 'HEAD') or None,
        'dirty_files': len([x for x in sh('git', 'status', '--porcelain').splitlines() if x.strip()]),
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
    if event == 'start' and not model:
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
    rows = []
    for r in recs:
        key = (r['stage'], r.get('arg'))
        if r['event'] == 'start':
            starts[key] = r
        elif r['event'] == 'end':
            s = starts.pop(key, None)
            rows.append((s, r))
    for key, s in starts.items():
        rows.append((s, None))
    fw = sorted({r['framework_version'] for r in recs})
    mv = sorted({r['methodology_version'] for r in recs})
    models = sorted({r['model'] for r in recs if r.get('model')})
    lines = [f"# Provenance — edition {cur.get('NR')}", '',
             f'Framework version(s): {", ".join(fw)} · methodology: {", ".join(mv)} · models: {", ".join(models) or "not recorded"}', '']
    if len(fw) > 1 or len(mv) > 1:
        lines += ['**Warning:** more than one framework or methodology version was used within this edition. '
                  'Learning analyses must treat this edition as mixed.', '']
    lines += ['| Stage | Arg | Start (UTC) | End (UTC) | Model | Framework | Commit at start | Prompt sha | Dirty files at start |',
              '|---|---|---|---|---|---|---|---|---|']
    for s, e in rows:
        s = s or {}
        lines.append(f"| {s.get('stage') or e.get('stage')} | {s.get('arg') or ''} | {s.get('ts', '—')} | "
                     f"{e['ts'] if e else 'not finished'} | {s.get('model') or '—'} | {s.get('framework_version')} | "
                     f"{s.get('commit')} | {s.get('prompt_sha')} | {s.get('dirty_files')} |")
    p = os.path.join(ROOT, cur['DIRECTORY'], 'provenance.md')
    with open(p, 'w', encoding='utf-8') as f:
        f.write('\n'.join(lines) + '\n')
    if not quiet:
        print('\n'.join(lines))


def edition_done_map(cur):
    """Which stages are complete in the current edition (provenance first, files as fallback)."""
    d = os.path.join(ROOT, cur.get('DIRECTORY', ''))
    ended = {(r['stage'], r.get('arg')) for r in load_prov(cur) if r['event'] == 'end'}

    def has(*files):
        return all(os.path.exists(os.path.join(d, f)) for f in files)

    def done(stage, arg=None, files=()):
        return (stage, arg) in ended or (bool(files) and has(*files) and not load_prov(cur))

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


def cmd_status(a):
    cur = current()
    print(f"Framework {framework_version()} · methodology {methodology_version(cur)} · harvester {harvester_version()} · "
          f"commit {sh('git', 'rev-parse', '--short', 'HEAD')} · branch {sh('git', 'rev-parse', '--abbrev-ref', 'HEAD')}")
    print(harvester_line())
    if not cur.get('DIRECTORY'):
        print('No current edition. Next: /g00 <STATE_DATE> <NR>')
        return
    print(f"\nEdition {cur.get('NR')} · state date {cur.get('STATE_DATE')} · period from {cur.get('PERIOD_FROM')} · {cur.get('DIRECTORY')}\n")
    steps = edition_done_map(cur)
    if steps[-1][3]:  # edition closed (stage 08 done and tagged): earlier gaps are historical
        steps = [(st, arg, cmd, True) for st, arg, cmd, _ in steps]
    nxt = None
    for stage, arg, cmd, ok in steps:
        mark = 'done' if ok else 'todo'
        if not ok and nxt is None:
            nxt = (stage, arg, cmd)
            mark = 'NEXT'
        label = (stage + (' ' + arg if arg else '')).ljust(6)
        print(f"  [{mark:4}] {label} {cmd}")
    print()
    today = datetime.now(timezone.utc).date().isoformat()
    if nxt is None:
        nr = int(cur.get('NR', '0')) + 1
        print(f"Edition {cur.get('NR')} is closed. Keep the harvester running. Next edition: "
              f"`/g00 <STATE_DATE> {nr:02d}` in a new session (state date at least 14 days after {cur.get('STATE_DATE')}, "
              f"and not in the future). Learning loop (optional, any time between editions): /gL1 … /gL5 — see RUNBOOK.md.")
        return
    stage, arg, cmd = nxt
    if stage == 'H' and cur.get('STATE_DATE', '9999') > today:
        print(f"Next: {cmd} — but the state date {cur['STATE_DATE']} is in the future. Keep harvesting until then.")
        return
    extra = ''
    if stage in ('04', '05', '06') or (stage == '02'):
        extra = ' Start it in a NEW session (/clear first).'
    if stage == '04':
        extra += ' Each lens in its own session; do not read other lens files.'
    print(f'Next step: {cmd}.{extra}')


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


def cmd_versions(a):
    cur = current()
    print(json.dumps({'framework_version': framework_version(), 'methodology_version': methodology_version(cur),
                      'harvester_version': harvester_version(), 'commit': sh('git', 'rev-parse', '--short=12', 'HEAD'),
                      'branch': sh('git', 'rev-parse', '--abbrev-ref', 'HEAD'),
                      'dirty_files': len([x for x in sh('git', 'status', '--porcelain').splitlines() if x.strip()]),
                      'edition': cur.get('NR'), 'claude_cli': sh('claude', '--version') or None}, indent=1))


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = p.add_subparsers(dest='cmd', required=True)
    sub.add_parser('status').set_defaults(fn=cmd_status)
    for ev in ('stage-start', 'stage-end'):
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
    a = p.parse_args()
    a.fn(a)


if __name__ == '__main__':
    main()
