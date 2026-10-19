"""Executive brief and social cards of the current edition (stage E, prompts/E_brief.md).

The brief is a derived view of the edition report: it adds no facts, assessments or
forecasts. Stage E writes the body (<edition>/E_brief_body.html) from 07_report.md;
this tool fills it into site/brief_template.html, injects every forecast value from
registry/forecasts.csv (AGG_RT), checks the result against the registry and the
report, and renders the PDF and the PNG cards with headless Google Chrome.
Nothing is written to docs/briefs/ unless the check passes.

Usage:
  python3 tools/brief.py check            check only, writes nothing
  python3 tools/brief.py build            brief (HTML, PDF) and all cards
  python3 tools/brief.py cards            cards only (e.g. a fresh week-ahead window)
  python3 tools/brief.py ticket Q-0083    forecast ticket card for one question

Standard library only. Chrome: BRIEF_CHROME, or the usual install locations.
"""
import csv
import hashlib
import html
import os
import re
import shutil
import subprocess
import sys
import tempfile
import time
from datetime import date, datetime, timedelta
from decimal import Decimal, ROUND_HALF_UP

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MIN_GAP_DAYS = 14
CHROME_CANDIDATES = [
    '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',
    '/Applications/Chromium.app/Contents/MacOS/Chromium',
    'google-chrome', 'google-chrome-stable', 'chromium', 'chromium-browser',
]


# ---------------------------------------------------------------- inputs

def path(*p):
    return os.path.join(ROOT, *p)


def current():
    cur = {}
    with open(path('editions', 'CURRENT.md'), encoding='utf-8') as f:
        for line in f:
            m = re.match(r'^([A-Z_]+)=(.*)$', line.strip())
            if m:
                cur[m.group(1)] = m.group(2).strip()
    return cur


def read_csv(name):
    with open(path('registry', name), encoding='utf-8-sig') as f:
        return list(csv.DictReader(f, delimiter=';'))


def r2(x):
    return Decimal(x).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)


def fmt_p(d):
    return f'{d:.2f}'


def pct(d):
    return f'{int((Decimal(d) * 100).quantize(Decimal("1"), rounding=ROUND_HALF_UP))}%'


def ddmmyyyy(iso):
    try:
        return datetime.strptime(iso, '%Y-%m-%d').strftime('%d.%m.%Y')
    except (TypeError, ValueError):
        return iso or ''


def sha16(p):
    with open(p, 'rb') as f:
        return hashlib.sha256(f.read()).hexdigest()[:16]


def git_date(commit):
    if not commit:
        return ''
    try:
        out = subprocess.run(['git', '-C', ROOT, 'show', '-s', '--format=%cd', '--date=format:%d.%m.%Y', commit],
                             capture_output=True, text=True, timeout=10)
        return out.stdout.strip()
    except (OSError, subprocess.SubprocessError):
        return ''


def context():
    cur = current()
    nr = cur['NR']
    prev = f'{int(nr) - 1:02d}'
    directory = cur['DIRECTORY']
    agg = {}
    for r in read_csv('forecasts.csv'):
        if r['run'] == 'AGG_RT':
            agg[(r['edition'], r['question_id'])] = r
    questions = {r['id']: r for r in read_csv('questions.csv')}
    ed_row = next((r for r in read_csv('editions.csv') if r['edition'] == nr), {})
    report_path = path(directory, '07_report.md')
    with open(report_path, encoding='utf-8') as f:
        report = f.read()
    scores_path = path(directory, '01_scores.md')
    scores = open(scores_path, encoding='utf-8').read() if os.path.exists(scores_path) else ''
    state = cur['STATE_DATE']
    freeze = ed_row.get('freeze_commit', '')
    import json
    cfg = json.load(open(path('site', 'config.json'), encoding='utf-8'))
    return {
        'cur': cur, 'nr': nr, 'prev': prev, 'dir': directory, 'agg': agg, 'questions': questions,
        'ed_row': ed_row, 'report': report, 'report_path': report_path, 'scores': scores,
        'annex': load_annex(report), 'state': ddmmyyyy(state),
        'next': (datetime.strptime(state, '%Y-%m-%d').date() + timedelta(days=MIN_GAP_DAYS)).strftime('%d.%m.%Y'),
        'freeze': freeze, 'freeze_date': git_date(freeze) or 'date not recorded',
        'site': cfg.get('site_url', '').rstrip('/'),
    }


def load_annex(report):
    """Annex rows: | ID | Question | Deadline | **p** | Verbal | A / B / C | Spread | Confidence | Change |"""
    annex = {}
    if '## Annex.' not in report:
        return annex
    for line in report.split('## Annex.', 1)[1].splitlines():
        m = re.match(r'\| (Q-\d{4}) \|', line)
        if not m:
            continue
        cells = [c.strip() for c in line.strip().strip('|').split('|')]
        annex[m.group(1)] = {'deadline': cells[2], 'p': Decimal(cells[3].strip('*')), 'verbal': cells[4]}
    return annex


# ---------------------------------------------------------------- build the page

def fill(ctx, body):
    with open(path('site', 'brief_template.html'), encoding='utf-8') as f:
        tpl = f.read()
    values = {
        'EDITION': ctx['nr'], 'PREV': ctx['prev'], 'STATE_DATE': ctx['state'], 'NEXT_EDITION': ctx['next'],
        'FREEZE_COMMIT': ctx['freeze'] or 'not recorded', 'FREEZE_DATE': ctx['freeze_date'],
        'DIRECTORY': ctx['dir'], 'REPORT_SHA': sha16(ctx['report_path']), 'REGISTRY_SHA': sha16(path('registry', 'forecasts.csv')),
        'METHODOLOGY': ctx['cur'].get('METHODOLOGY', ''), 'EDITION_FRAMEWORK': ctx['ed_row'].get('framework_version', 'not recorded'),
        'FRAMEWORK': open(path('VERSION'), encoding='utf-8').read().strip(), 'BUILD_DATE': date.today().strftime('%d.%m.%Y'),
    }
    out = tpl.replace('{{BODY}}', body)
    for k, v in values.items():
        out = out.replace('{{' + k + '}}', html.escape(v))
    return out


def inject(ctx, page):
    agg, annex, questions, nr, prev = ctx['agg'], ctx['annex'], ctx['questions'], ctx['nr'], ctx['prev']
    problems = []

    def row(m):
        q, label = m.group(1), m.group(2)
        now = agg.get((nr, q))
        if not now:
            problems.append(f'{q}: no AGG_RT row for edition {nr}')
            return m.group(0)
        p = r2(now['p'])
        a = annex.get(q)
        if not a:
            problems.append(f'{q}: not in the report annex')
            return m.group(0)
        if a['p'] != p:
            problems.append(f'{q}: registry {p} != report annex {a["p"]}')
        before = agg.get((prev, q))
        pp = r2(before['p']) if before else None
        if pp is None:
            change, prev_mark = 'new', ''
        elif pp == p:
            change, prev_mark = f'= {fmt_p(pp)}', ''
        else:
            arrow, sign = ('▲', '+') if p > pp else ('▼', '−')
            change = f'{arrow} {sign}{fmt_p(abs(p - pp))} <span class="muted">from {fmt_p(pp)}</span>'
            prev_mark = f'<span class="prev" style="left:{float(pp) * 100:.1f}%"></span>'
        title = html.escape(questions.get(q, {}).get('question', ''), quote=True)
        return (f'<tr data-q="{q}" data-p="{fmt_p(p)}" title="{title}">{label}'
                f'<td class="dl">{a["deadline"]}</td>'
                f'<td><div class="track" aria-hidden="true"><span class="mid"></span>{prev_mark}'
                f'<span class="now" style="left:{float(p) * 100:.1f}%"></span></div></td>'
                f'<td class="p">{fmt_p(p)}</td><td class="w">{a["verbal"]}</td>'
                f'<td class="ch">{change}</td><td class="c">{now["analytic_confidence"]}</td>'
                f'<td class="id">{q}</td></tr>')

    def pv(m):
        q = m.group(1)
        now = agg.get((nr, q))
        if not now:
            problems.append(f'{q}: no AGG_RT row for edition {nr} (inline value)')
            return m.group(0)
        return f'<b class="pv" data-q="{q}" data-p="{fmt_p(r2(now["p"]))}">{fmt_p(r2(now["p"]))}</b>'

    page = re.sub(r'<tr class="fc" data-q="(Q-\d{4})">(.*?)</tr>', row, page, flags=re.S)
    page = re.sub(r'<b class="pv" data-q="(Q-\d{4})"></b>', pv, page)
    return page, problems


def text_of(fragment):
    t = re.sub(r'<[^>]+>', ' ', fragment)
    return re.sub(r'\s+', ' ', html.unescape(t)).strip()


def verify(ctx, page):
    problems = []
    nr = ctx['nr']
    if '{{' in page:
        problems.append('unfilled placeholder: ' + ', '.join(sorted(set(re.findall(r'{{[A-Z_]+}}', page)))))
    if re.search(r'<tr class="fc"|<b class="pv" data-q="Q-\d{4}"></b>', page):
        problems.append('a forecast row or inline value was not filled')
    # 1. every rendered value equals the registry
    for q, p in re.findall(r'data-q="(Q-\d{4})" data-p="([\d.]+)"', page):
        row = ctx['agg'].get((nr, q))
        if not row or fmt_p(r2(row['p'])) != p:
            problems.append(f'{q}: rendered {p} differs from the registry')
    # 2. scenario shares equal section H.1 of the report
    h1 = ctx['report'].split('### H.1', 1)[1].split('### H.2', 1)[0] if '### H.1' in ctx['report'] else ''
    rep = re.findall(r'^\| \*\*(Base|Favourable|Crisis)\b[^\n]*?\| \*\*(\d+)%\*\*[^|]*\| (\d+)% \|', h1, flags=re.M)
    rep_now, rep_prev = [], []
    for i in range(0, len(rep) - len(rep) % 3, 3):
        trio = {name: (int(a), int(b)) for name, a, b in rep[i:i + 3]}
        rep_now.append([trio.get(k, (None, None))[0] for k in ('Favourable', 'Base', 'Crisis')])
        rep_prev.append([trio.get(k, (None, None))[1] for k in ('Favourable', 'Base', 'Crisis')])
    rows = re.findall(r'<div class="row"[^>]*>(.*?)</div>\s*<span[^>]*>ed\. \d{2}: (\d+) · (\d+) · (\d+)</span>', page, flags=re.S)
    for i, (bar, a, b, c) in enumerate(rows):
        segs = [int(x) for x in re.findall(r'class="seg \w+" style="flex:(\d+)"', bar)]
        if i >= len(rep_now):
            problems.append(f'scenario row {i + 1}: no matching horizon in report section H.1')
            continue
        if segs != rep_now[i]:
            problems.append(f'scenario row {i + 1}: {segs} != report H.1 {rep_now[i]} (favourable, base, crisis)')
        if [int(a), int(b), int(c)] != rep_prev[i]:
            problems.append(f'scenario row {i + 1}: previous {[a, b, c]} != report H.1 {rep_prev[i]}')
    # 3. every number in the prose appears in the report or the scores
    prose = re.sub(r'<table class="fct".*?</table>', ' ', page, flags=re.S)
    prose = re.sub(r'<div class="foot">.*?</div>|<div class="meta">.*?</div>|<h1>.*?</h1>', ' ', prose, flags=re.S)
    prose = re.sub(r'<style>.*?</style>|<head>.*?</head>|<b class="pv"[^>]*>[^<]*</b>', ' ', prose, flags=re.S)
    prose = re.sub(r'<div class="scen.*?</div>\s*</div>\s*</div>', ' ', prose, flags=re.S)
    sources = ctx['report'] + '\n' + ctx['scores']
    missing = sorted({n for n in re.findall(r'\d+(?:[.,]\d+)+|\d{2,}', text_of(prose)) if n not in sources})
    if missing:
        problems.append('numbers not found in the report or 01_scores.md: ' + ', '.join(missing))
    return problems


def build_page(ctx):
    body_path = path(ctx['dir'], 'E_brief_body.html')
    if not os.path.exists(body_path):
        return None, [f'missing {os.path.relpath(body_path, ROOT)} (written by stage E)']
    with open(body_path, encoding='utf-8') as f:
        body = f.read()
    page, problems = inject(ctx, fill(ctx, body))
    return page, problems + verify(ctx, page)


# ---------------------------------------------------------------- rendering

def chrome():
    exe = os.environ.get('BRIEF_CHROME')
    if exe:
        return exe
    for c in CHROME_CANDIDATES:
        if os.path.isabs(c) and os.path.exists(c):
            return c
        if not os.path.isabs(c) and shutil.which(c):
            return shutil.which(c)
    sys.exit('Google Chrome not found: set BRIEF_CHROME to its executable')


def run_chrome(args, out_file):
    """Headless Chrome sometimes keeps running after writing its output: wait for the file, then stop it."""
    profile = tempfile.mkdtemp(prefix='brief-chrome-')
    if os.path.exists(out_file):
        os.remove(out_file)
    proc = subprocess.Popen([chrome(), '--headless=new', '--disable-gpu', '--no-first-run', '--hide-scrollbars',
                             f'--user-data-dir={profile}', '--virtual-time-budget=15000'] + args,
                            stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    deadline = time.time() + 90
    try:
        while time.time() < deadline:
            if proc.poll() is not None:
                break
            if os.path.exists(out_file) and os.path.getsize(out_file) > 0:
                time.sleep(1.5)
                break
            time.sleep(0.5)
    finally:
        if proc.poll() is None:
            proc.kill()
        shutil.rmtree(profile, ignore_errors=True)
    if not os.path.exists(out_file):
        sys.exit(f'Chrome did not write {out_file}')


def pdf(html_file, pdf_file):
    run_chrome(['--no-pdf-header-footer', f'--print-to-pdf={pdf_file}', 'file://' + html_file], pdf_file)


def png(card_html, png_file, width=1600, height=900):
    with tempfile.NamedTemporaryFile('w', suffix='.html', delete=False, encoding='utf-8') as f:
        f.write(card_html)
        tmp = f.name
    try:
        run_chrome([f'--window-size={width},{height}', f'--screenshot={png_file}', 'file://' + tmp], png_file)
    finally:
        os.remove(tmp)


# ---------------------------------------------------------------- cards

CARD_CSS = '''
:root { --paper:#f2f5f5; --surface:#ffffff; --ink:#15232b; --muted:#56666f; --rule:#d3dcdf; --accent:#0b6970; --accent-soft:#dcecec;
  --fav:#0a7fa6; --base:#a3afb4; --crisis:#b4462c; }
* { box-sizing:border-box; margin:0; }
html, body { width:1600px; height:900px; overflow:hidden; }
body { background:var(--paper); color:var(--ink); font-family:"Public Sans","Segoe UI",system-ui,sans-serif; padding:56px 76px 44px; display:flex; flex-direction:column; gap:26px; }
.top { display:flex; justify-content:space-between; font-family:"IBM Plex Mono",Menlo,monospace; font-size:19px; letter-spacing:.1em; text-transform:uppercase; color:var(--muted); border-bottom:3px solid var(--ink); padding-bottom:14px; }
h1 { font-family:"Newsreader",Georgia,serif; font-weight:600; font-size:62px; line-height:1.05; letter-spacing:-.01em; }
.bl { font-family:"Newsreader",Georgia,serif; font-size:31px; line-height:1.3; background:var(--accent-soft); border-left:6px solid var(--accent); padding:18px 24px; }
.rows { display:grid; gap:2px; }
.r { display:grid; grid-template-columns:minmax(0,1fr) 300px 130px 250px; align-items:center; gap:24px; padding:13px 0; border-bottom:2px solid var(--rule); font-size:27px; line-height:1.2; }
.r .t { position:relative; height:22px; }
.r .t::before { content:""; position:absolute; left:0; right:0; top:10px; height:2px; background:var(--rule); }
.r .t .m { position:absolute; left:50%; top:2px; width:2px; height:18px; background:var(--rule); }
.r .t .n { position:absolute; top:1px; width:20px; height:20px; margin-left:-10px; border-radius:50%; background:var(--accent); box-shadow:0 0 0 4px var(--paper); }
.r .t .o { position:absolute; top:2px; width:18px; height:18px; margin-left:-9px; border-radius:50%; border:3px solid var(--muted); background:var(--paper); }
.r .p { font-family:"IBM Plex Mono",Menlo,monospace; font-size:44px; font-weight:500; text-align:right; }
.r .w { font-size:21px; color:var(--muted); line-height:1.3; }
.r .w b { color:var(--ink); font-weight:500; }
.foot { margin-top:auto; display:flex; justify-content:space-between; gap:20px; font-family:"IBM Plex Mono",Menlo,monospace; font-size:17px; color:var(--muted); }
.bar { display:flex; gap:4px; height:46px; }
.seg { display:flex; align-items:center; justify-content:center; font-family:"IBM Plex Mono",Menlo,monospace; font-size:22px; font-weight:500; }
.seg:first-child { border-radius:8px 0 0 8px; } .seg:last-child { border-radius:0 8px 8px 0; }
.fav { background:var(--fav); color:#fff; } .base { background:var(--base); color:var(--ink); } .crisis { background:var(--crisis); color:#fff; }
.scen { display:grid; grid-template-columns:230px minmax(0,1fr); gap:20px; align-items:center; font-family:"IBM Plex Mono",Menlo,monospace; font-size:19px; color:var(--muted); text-transform:uppercase; letter-spacing:.06em; }
.tiles { display:grid; grid-template-columns:repeat(3,minmax(0,1fr)); gap:36px; margin-top:20px; }
.tile { border-top:5px solid var(--ink); padding-top:14px; }
.tile b { display:block; font-family:"IBM Plex Mono",Menlo,monospace; font-size:96px; font-weight:500; line-height:1; }
.tile span { display:block; margin-top:14px; font-size:27px; color:var(--muted); line-height:1.3; }
.note { font-size:24px; color:var(--muted); line-height:1.4; }
.chain { display:grid; grid-auto-flow:column; grid-auto-columns:minmax(0,1fr); gap:44px; margin-top:16px; }
.step { position:relative; background:var(--surface); border:2px solid var(--rule); border-top:6px solid var(--accent); padding:18px 18px 20px; font-size:24px; line-height:1.3; }
.step b { display:block; font-family:"IBM Plex Mono",Menlo,monospace; font-size:17px; letter-spacing:.08em; text-transform:uppercase; color:var(--accent); margin-bottom:8px; }
.step:not(:last-child)::after { content:"→"; position:absolute; right:-38px; top:42%; font-size:34px; color:var(--muted); }
.wk { display:grid; grid-template-columns:150px minmax(0,1fr) 120px; gap:22px; padding:12px 0; border-bottom:2px solid var(--rule); font-size:26px; align-items:baseline; }
.wk .d { font-family:"IBM Plex Mono",Menlo,monospace; color:var(--muted); font-size:23px; }
.wk .p { font-family:"IBM Plex Mono",Menlo,monospace; font-size:36px; text-align:right; }
.q { font-family:"Newsreader",Georgia,serif; font-size:46px; line-height:1.2; }
.big { font-family:"IBM Plex Mono",Menlo,monospace; font-size:150px; font-weight:500; line-height:1; color:var(--accent); }
.stamp { font-family:"IBM Plex Mono",Menlo,monospace; font-size:22px; letter-spacing:.16em; color:#8c3a2b; border:3px solid #8c3a2b; padding:6px 14px; align-self:flex-start; }
'''
FONTS = ('<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Newsreader:opsz,wght@6..72,400;6..72,600'
         '&family=Public+Sans:wght@400;500;600&family=IBM+Plex+Mono:wght@400;500&display=swap">')


def card_doc(inner):
    return f'<!doctype html><html lang="en"><head><meta charset="utf-8">{FONTS}<style>{CARD_CSS}</style></head><body>{inner}</body></html>'


def first_sentences(t, limit=230):
    parts = re.split(r'(?<=[.!?])\s+', t)
    out = ''
    for s in parts:
        if out and len(out) + len(s) + 1 > limit:
            break
        out = (out + ' ' + s).strip()
    return out


def fc_rows(fragment, n=4):
    rows = []
    for q, p, inner in re.findall(r'<tr data-q="(Q-\d{4})" data-p="([\d.]+)"[^>]*>(.*?)</tr>', fragment, flags=re.S):
        cells = re.findall(r'<td[^>]*>(.*?)</td>', inner, flags=re.S)
        prev = re.search(r'class="prev" style="left:([\d.]+)%"', inner)
        rows.append({'q': q, 'p': Decimal(p), 'label': text_of(cells[0]), 'deadline': text_of(cells[1]),
                     'verbal': text_of(cells[4]), 'change': text_of(cells[5]), 'prev': float(prev.group(1)) if prev else None})
    return rows[:n]


def rows_html(rows):
    out = []
    for r in rows:
        prev = f'<span class="o" style="left:{r["prev"]:.1f}%"></span>' if r['prev'] is not None else ''
        out.append(f'<div class="r"><div>{html.escape(r["label"])}</div>'
                   f'<div class="t"><span class="m"></span>{prev}<span class="n" style="left:{float(r["p"]) * 100:.1f}%"></span></div>'
                   f'<div class="p">{pct(r["p"])}</div>'
                   f'<div class="w"><b>{html.escape(r["verbal"])}</b> · by {html.escape(r["deadline"])}<br>{html.escape(r["q"])} · {html.escape(r["change"])}</div></div>')
    return '<div class="rows">' + ''.join(out) + '</div>'


def foot(ctx, left=None):
    site = ctx['site'].replace('https://', '')
    left = left or f'Official forecasts (AGG_RT) · frozen {ctx["freeze_date"]} · commit {ctx["freeze"]}'
    return f'<div class="foot"><span>{html.escape(left)}</span><span>{html.escape(site)}</span></div>'


def top(ctx, right):
    return (f'<div class="top"><span>Worldstate Forecast · Edition {ctx["nr"]} · state {ctx["state"]}</span>'
            f'<span>{html.escape(right)}</span></div>')


def cards_from_page(ctx, page):
    cards = {}
    sections = re.findall(r'<section class="chapter[^"]*"[^>]*>(.*?)</section>', page, flags=re.S)
    first = sections[0] if sections else ''
    title = text_of(re.search(r'<h1>(.*?)</h1>', first, re.S).group(1)) if '<h1>' in first else f'Edition {ctx["nr"]}'
    bl = re.search(r'<div class="bl">.*?<p>(.*?)</p>', first, re.S)
    head_tbl = re.search(r'<table class="fct" data-card="headline">(.*?)</table>', page, re.S)
    scen = re.search(r'<div class="row"[^>]*><span class="label">(.*?)</span>\s*<div class="bar">(.*?)</div>', page, re.S)
    scen_html = ''
    if scen:
        segs = re.findall(r'class="seg (\w+)" style="flex:(\d+)"', scen.group(2))
        scen_html = (f'<div class="scen"><span>Scenarios · {html.escape(text_of(scen.group(1)))}</span><div class="bar">'
                     + ''.join(f'<div class="seg {c}" style="flex:{v}">{v}%</div>' for c, v in segs) + '</div></div>')
    cards['edition'] = card_doc(top(ctx, 'Executive brief') + f'<h1>{html.escape(title)}</h1>'
                                + (f'<div class="bl">{html.escape(first_sentences(text_of(bl.group(1)), 260))}</div>' if bl else '')
                                + (rows_html(fc_rows(head_tbl.group(1), 3)) if head_tbl else '') + scen_html + foot(ctx))
    for sec in sections:
        k = re.search(r'Region (\d+) of (\d+)', sec)
        if not k:
            continue
        name = text_of(re.search(r'<h2>(.*?)</h2>', sec, re.S).group(1))
        sbl = re.search(r'<div class="bl">.*?<p>(.*?)</p>', sec, re.S)
        cards[f'region-{int(k.group(1)):02d}'] = card_doc(
            top(ctx, f'Region {k.group(1)} of {k.group(2)}') + f'<h1>{html.escape(name)}</h1>'
            + (f'<div class="bl">{html.escape(first_sentences(text_of(sbl.group(1))))}</div>' if sbl else '')
            + rows_html(fc_rows(sec, 3)) + foot(ctx))
    chain = re.search(r'<ol class="chain" data-card="crosslink">(.*?)</ol>(.*?)</p>', page, re.S)
    if chain:
        steps = []
        for li in re.findall(r'<li>(.*?)</li>', chain.group(1), re.S):
            li = re.sub(r'<span class="ref">.*?</span>', '', li, flags=re.S)
            m = re.match(r'\s*<span>\s*<b>(.*?)</b>(.*)', li, re.S)
            head_, rest = (text_of(m.group(1)).rstrip('.'), text_of(m.group(2))) if m else ('', text_of(li))
            steps.append(f'<div class="step"><b>{html.escape(head_)}</b>{html.escape(rest)}</div>')
        qs = re.findall(r'<b class="pv" data-q="(Q-\d{4})" data-p="([\d.]+)">', chain.group(2))
        tail = ' · '.join(f'{q}: {pct(p)}' for q, p in qs)
        cards['crosslink'] = card_doc(top(ctx, 'How the regions connect') + '<h1>One chain, several regions</h1>'
                                      + '<p class="note">Assessment: each step is a dated fact in the report; the links are the report\'s reading.</p>'
                                      + '<div class="chain">' + ''.join(steps) + '</div>'
                                      + (f'<p class="note" style="margin-top:12px">Questions that register it: {html.escape(tail)}</p>' if tail else '')
                                      + foot(ctx))
    tiles = re.search(r'<div class="tiles" data-check="track">(.*?)</div>\s*<p', page, re.S)
    if tiles:
        ts = re.findall(r'<div class="tile"><b>(.*?)</b><span>(.*?)</span></div>', tiles.group(1), re.S)
        cards['scorecard'] = card_doc(top(ctx, 'Track record') + '<h1>How the forecasts have scored</h1>'
                                      + '<div class="tiles">' + ''.join(f'<div class="tile"><b>{html.escape(text_of(a))}</b><span>{html.escape(text_of(b))}</span></div>' for a, b in ts) + '</div>'
                                      + '<p class="note" style="margin-top:24px">Brier score: lower is better. Below 30 resolved questions the numbers are indicative only. Misses are published with the same prominence as hits.</p>'
                                      + foot(ctx, f'Scores from {ctx["dir"]}/01_scores.md · tools/scores.py'))
    cards['week-ahead'] = week_card(ctx, page)
    return cards


def short_labels(page):
    return {q: text_of(lbl) for q, lbl in re.findall(r'<tr data-q="(Q-\d{4})"[^>]*><td>(.*?)</td>', page, re.S)}


def week_card(ctx, page, start=None):
    start = start or date.today()
    end = start + timedelta(days=7)
    labels = short_labels(page)
    items = []
    for q, row in ctx['questions'].items():
        if row.get('status') != 'ACTIVE' or not row.get('deadline'):
            continue
        d = datetime.strptime(row['deadline'], '%Y-%m-%d').date()
        f = ctx['agg'].get((ctx['nr'], q))
        if f and start <= d <= end:
            label = labels.get(q) or row['question']
            if len(label) > 95:
                label = label[:92].rsplit(' ', 1)[0] + '…'
            items.append((d, q, label, r2(f['p'])))
    items.sort()
    body = ''.join(f'<div class="wk"><span class="d">{d:%d.%m}</span><span>{html.escape(label)} <span class="note">· {q}</span></span>'
                   f'<span class="p">{pct(p)}</span></div>' for d, q, label, p in items[:9])
    if not body:
        body = '<p class="note">No question has its deadline in this window.</p>'
    return card_doc(top(ctx, f'Week ahead · {start:%d.%m}–{end:%d.%m.%Y}') + '<h1>What closes this week, and what we froze</h1>'
                    + f'<div>{body}</div>' + foot(ctx))


def ticket_card(ctx, q):
    row = ctx['questions'].get(q)
    eds = sorted(e for (e, qq) in ctx['agg'] if qq == q)
    if not row or not eds:
        sys.exit(f'{q}: no such question with an official forecast')
    ed = eds[-1]
    p = r2(ctx['agg'][(ed, q)]['p'])
    ed_row = next((r for r in read_csv('editions.csv') if r['edition'] == ed), {})
    freeze = ed_row.get('freeze_commit', '')
    inner = (top(ctx, f'{q} · {row.get("vector", "")}') + '<span class="stamp">FROZEN</span>'
             + f'<p class="q">{html.escape(row["question"])}</p>'
             + f'<div style="display:flex;align-items:flex-end;gap:40px"><span class="big">{pct(p)}</span>'
             + f'<span class="note">official forecast, edition {ed}<br>resolves {ddmmyyyy(row["deadline"])}<br>'
             + f'source: {html.escape(row.get("resolution_source", "")[:70])}</span></div>'
             + foot(ctx, f'Frozen {git_date(freeze) or "date not recorded"} · commit {freeze} · registry/forecasts.csv'))
    return card_doc(inner)


# ---------------------------------------------------------------- commands

def out_dirs(ctx):
    briefs = path('docs', 'briefs')
    cards = path('social', 'cards', f'edition-{ctx["nr"]}')
    os.makedirs(briefs, exist_ok=True)
    os.makedirs(cards, exist_ok=True)
    return briefs, cards


def checked_page(ctx):
    page, problems = build_page(ctx)
    if problems:
        print('CHECK FAILED — nothing written:')
        for p in problems:
            print('  -', p)
        sys.exit(1)
    n = len(re.findall(r'data-q="Q-\d{4}" data-p=', page))
    print(f'check passed: {n} forecast values match the registry and the report annex; scenarios match H.1; '
          f'every number in the prose appears in the report or 01_scores.md')
    return page


def render_cards(ctx, page, cards_dir):
    written = []
    for name, doc in cards_from_page(ctx, page).items():
        target = os.path.join(cards_dir, f'{name}.png')
        png(doc, target)
        written.append(os.path.relpath(target, ROOT))
    return written


def main(argv):
    cmd = argv[1] if len(argv) > 1 else 'check'
    ctx = context()
    if cmd == 'check':
        checked_page(ctx)
    elif cmd in ('build', 'cards'):
        page = checked_page(ctx)
        briefs, cards_dir = out_dirs(ctx)
        if cmd == 'build':
            html_file = os.path.join(briefs, f'edition-{ctx["nr"]}.html')
            with open(html_file, 'w', encoding='utf-8') as f:
                f.write(page)
            pdf(html_file, os.path.join(briefs, f'edition-{ctx["nr"]}.pdf'))
            print('wrote', os.path.relpath(html_file, ROOT), 'and', f'docs/briefs/edition-{ctx["nr"]}.pdf')
        for w in render_cards(ctx, page, cards_dir):
            print('wrote', w)
    elif cmd == 'ticket' and len(argv) > 2:
        q = argv[2].upper()
        _, cards_dir = out_dirs(ctx)
        target = os.path.join(cards_dir, f'ticket-{q}.png')
        png(ticket_card(ctx, q), target)
        print('wrote', os.path.relpath(target, ROOT))
    else:
        sys.exit(__doc__)


if __name__ == '__main__':
    main(sys.argv)
