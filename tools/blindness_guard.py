#!/usr/bin/env python3
"""PreToolUse hook: technical enforcement of forecast blindness (CLAUDE.md rules 3.8 and 3.9; framework 1.9, WP-22).

Claude Code runs this before every Bash, Read, Grep, Edit, Write, WebFetch and WebSearch call in this project,
including those of sub-agents. It reads the tool call (JSON on stdin) and the open stage of the current edition
(the last provenance record without an end). Exit 2 blocks the call; the message on stderr goes to the agent.

  stages 03, 04, 05  no 06_* files, 07_annex_benchmarks, registry/benchmarks.csv, reviews/learning/, social/,
                     docs/data/, docs/briefs/; no forecasting or betting sites; no "odds"-type searches
  stage 04 <LENS>    also: no other lens's 04 files; registry/forecasts.csv only through
                     `python3 tools/pipeline.py lens-rows <LENS>` and `... append-forecasts <file>`
  stage 04 B2        also: no facts, analysis, harvest or forecasts at all, and no web: question + base rates only
  any stage but 06   no forecasting or betting sites (rule 3.9)

Testing: BLINDNESS_STAGE="04:A" overrides the detected stage. Python standard library only.
"""
import json
import os
import re
import sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
FORBIDDEN_DOMAINS = ('metaculus.com', 'gjopen.com', 'goodjudgment.com', 'polymarket.com', 'kalshi.com',
                     'manifold.markets', 'predictit.org', 'randforecastinginitiative.org', 'infer-pub.com')
ODDS_WORDS = re.compile(r'\b(odds|prediction market|market-implied|betting)\b', re.I)
BLIND_COMMON = [r'(^|/)06_[^/\s"\']*', r'07_annex_benchmarks', r'registry/benchmarks\.csv', r'benchmarks\.csv',
                r'reviews/learning', r'(^|[\s"\'/])social/', r'docs/data', r'docs/briefs']


def open_stage():
    """(stage, arg) of the open stage of the current edition, or (None, None)."""
    env = os.environ.get('BLINDNESS_STAGE')
    if env is not None:
        st, _, arg = env.partition(':')
        return (st or None), (arg or None)
    try:
        cur = {}
        with open(os.path.join(ROOT, 'editions', 'CURRENT.md'), encoding='utf-8') as f:
            for line in f:
                if '=' in line:
                    k, v = line.strip().split('=', 1)
                    cur[k] = v
        recs = []
        with open(os.path.join(ROOT, cur['DIRECTORY'], 'provenance.jsonl'), encoding='utf-8') as f:
            for line in f:
                try:
                    recs.append(json.loads(line))
                except ValueError:
                    pass
    except (OSError, KeyError):
        return None, None
    openk = {}
    for r in recs:
        k = (r.get('stage'), r.get('arg'))
        if r.get('event') in ('start', 'resume'):
            openk[k] = r.get('ts', '')
        elif r.get('event') == 'end':
            openk.pop(k, None)
    if not openk:
        return None, None
    stage, arg = max(openk.items(), key=lambda kv: kv[1])[0]
    return stage, arg


def text_of(tool, inp):
    if tool == 'Bash':
        return inp.get('command', '')
    if tool in ('Read', 'Edit', 'Write', 'MultiEdit', 'NotebookEdit'):
        return inp.get('file_path', '') or inp.get('notebook_path', '')
    if tool == 'Grep':
        return ' '.join(str(inp.get(k, '')) for k in ('path', 'glob', 'pattern'))
    if tool == 'WebFetch':
        return inp.get('url', '')
    if tool == 'WebSearch':
        return inp.get('query', '') + ' ' + ' '.join(inp.get('allowed_domains') or [])
    return json.dumps(inp)


SECRETS = [r'(^|[\s/"\'=])\.env(?!\.example)(\b|$)', r'\.ssh/', r'\.config/gh', r'\bgh\s+auth\s+token',
           r'\bsecurity\s+(find|dump|export)', r'git-credential', r'osxkeychain', r'\bgit\s+(-C\s+\S+\s+)?push\b',
           r'\bgit\s+remote\s+(set-url|add|remove|rename)', r'\bgit\s+config\b.*(credential|url\.|remote\.|pushurl)',
           r'\blaunchctl\b', r'LaunchAgents']


def decide(tool, inp, stage, arg):
    """Return None (allow) or a reason (block)."""
    text = text_of(tool, inp)
    low = text.lower()
    if tool != 'WebSearch':
        for pat in SECRETS:  # every stage (framework 1.9, WP-16): secrets, credentials, publishing, launchd
            if re.search(pat, text):
                return ('secrets, credentials, publishing and the launchd jobs are off limits to agents '
                        '(CLAUDE.md rule 6; scripts/autopilot.sh publishes)')
    if stage != '06' and tool in ('WebFetch', 'WebSearch', 'Bash'):
        for d in FORBIDDEN_DOMAINS:
            if d in low:
                return f'{d} is a forecasting or betting site: forbidden outside stage 06 (CLAUDE.md rule 3.9)'
    if stage == 'R':  # replay (WP-07): only the replayed edition's facts and analysis, and the replay folder
        if tool in ('WebFetch', 'WebSearch'):
            return 'a replay uses no web access (its validity depends on it)'
        rdir = os.environ.get('BLINDNESS_REPLAY_DIR', '')
        odir = os.environ.get('BLINDNESS_REPLAY_OUT', '')
        if re.search(r'registry/|docs/|social/|reviews/learning|data/harvest', text) \
                and not (odir and odir in text and 'registry/' not in text):
            return 'a replay may read only the replayed edition\'s 02_facts and 03_analysis and its replay folder'
        if rdir and re.search(re.escape(rdir) + r'/(0[014-8]_|E_|V_|provenance|log\.md)', text):
            return 'a replay may read only the replayed edition\'s 02_facts and 03_analysis (no later stages, outcomes or logs)'
        for m in re.finditer(r'editions/[^\s"\']+', text):
            if not (rdir and m.group(0).startswith(rdir)):
                return 'a replay may not open another edition'
        return None
    if stage not in ('03', 'W', '04', '05'):
        return None
    if tool == 'WebSearch' and ODDS_WORDS.search(text):
        return 'searches for odds, betting or prediction markets are forbidden in stages 03-05 and W (rule 3.8)'
    if stage == '04' and arg == 'B2':
        if tool in ('WebFetch', 'WebSearch'):
            return 'stage 04 B2 (outside view from base rates) uses no web access'
        for pat in (r'02_facts', r'03_analysis', r'03_question', r'02_harvest', r'04_forecasts_', r'04_rows_',
                    r'registry/forecasts\.csv', r'forecasts\.csv', r'07_report', r'00_plan'):
            if re.search(pat, text):
                return 'stage 04 B2 sees only the questions and the base rates (framework 1.9, WP-11)'
    for pat in BLIND_COMMON:
        if re.search(pat, text):
            return f'forecast blindness: stage {stage} may not open this (CLAUDE.md rule 3.8): {pat}'
    if stage == '04':
        lens = arg or ''
        m = re.findall(r'04_(?:forecasts|rows)_([A-Za-z0-9]+)', text)
        if any(x != lens for x in m):
            return f'forecast blindness: lens {lens} may not open another lens\'s files (rule 3.8)'
        if re.search(r'forecasts\.csv', text):
            cmd = text.strip()
            ok = re.match(r'^python3 tools/pipeline\.py (lens-rows|append-forecasts)\b', cmd) and not re.search(r'[;&|`$<>]', cmd)
            lr = re.match(r'^python3 tools/pipeline\.py lens-rows\s+(\S+)', cmd)
            if not ok or (lr and lr.group(1) != lens):
                return ('lens files use registry/forecasts.csv only through `python3 tools/pipeline.py lens-rows '
                        f'{lens}` and `python3 tools/pipeline.py append-forecasts <file>` (rule 3.8)')
        lr = re.search(r'lens-rows\s+(\S+)', text)
        if lr and lr.group(1) != lens:
            return f'lens {lens} may read only its own rows (rule 3.8)'
    return None


def main():
    try:
        data = json.load(sys.stdin)
    except ValueError:
        return 0
    stage, arg = open_stage()
    reason = decide(data.get('tool_name', ''), data.get('tool_input') or {}, stage, arg)
    if reason:
        print(f'BLOCKED by tools/blindness_guard.py: {reason}', file=sys.stderr)
        return 2
    return 0


if __name__ == '__main__':
    sys.exit(main())
