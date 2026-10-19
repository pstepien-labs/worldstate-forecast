"""Executive brief and X cards (stage E, prompts/E_brief.md; voice: social/STRATEGY.md).

The brief is a derived view of the edition report: it adds no facts, assessments or
forecasts. Stage E writes the body (<edition>/E_brief_body.html) from 07_report.md;
this tool fills it into site/brief_template.html, injects every forecast value from
registry/forecasts.csv (AGG_RT), checks the result against the registry and the
report, and renders the PDF and the PNG cards with headless Google Chrome.
Nothing is written to docs/briefs/ unless the check passes.

Usage:
  python3 tools/brief.py check              check only, writes nothing
  python3 tools/brief.py build              brief (HTML, PDF), edition, region and score cards
  python3 tools/brief.py cards              those cards only
  python3 tools/brief.py card call   --q Q-0066 --title "Will the Fed raise rates on Wednesday?" --when "Decided: Wed 28 Oct"
  python3 tools/brief.py card result --q Q-0066 --title "Did the Fed raise rates?" --outcome no --note "Rates held."
  python3 tools/brief.py card week   --item "Q-0020|Bank of Russia cuts rates|Fri" --item "…" --item "…"
  python3 tools/brief.py card chain  --title "…" --step "Red Sea|…" --step "Oil|…" [--q Q-0007 --label "Brent above $120 by 31 Dec"]
  python3 tools/brief.py card score  [--best "…"] [--worst "…"]
  python3 tools/brief.py card edition --title "One-sentence state of the world"

Post cards go to social/cards/posts/ and are shown in Finder. Standard library only.
Chrome: BRIEF_CHROME, or the usual install locations.
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
# One message per image (social/STRATEGY.md): a short headline, one big number or at most
# three rows, one context line, and a footer with the lock date and the site. No IDs,
# no hashes, no file paths. Every probability comes from the registry.

CARD_CSS = '''
:root { --paper:#f2f5f5; --surface:#ffffff; --ink:#15232b; --muted:#56666f; --rule:#d3dcdf; --accent:#0b6970; --accent-soft:#dcecec;
  --yes:#0b6970; --no:#8c3a2b; }
* { box-sizing:border-box; margin:0; }
html, body { width:1600px; height:900px; overflow:hidden; }
body { background:var(--paper); color:var(--ink); font-family:"Public Sans","Segoe UI",system-ui,sans-serif; padding:60px 84px 48px; display:flex; flex-direction:column; gap:34px; }
.top { display:flex; justify-content:space-between; font-family:"IBM Plex Mono",Menlo,monospace; font-size:21px; letter-spacing:.12em; text-transform:uppercase; color:var(--muted); border-bottom:3px solid var(--ink); padding-bottom:16px; }
.top b { color:var(--accent); font-weight:500; }
h1 { font-family:"Newsreader",Georgia,serif; font-weight:600; font-size:76px; line-height:1.06; letter-spacing:-.012em; text-wrap:balance; }
h1.mid { font-size:64px; }
.lead { font-family:"Newsreader",Georgia,serif; font-size:36px; line-height:1.3; color:var(--ink); max-width:1300px; }
.ctx { font-size:30px; color:var(--muted); line-height:1.35; }
.big { font-family:"IBM Plex Mono",Menlo,monospace; font-size:230px; font-weight:500; line-height:.9; color:var(--accent); letter-spacing:-.04em; }
.hero { display:flex; align-items:flex-end; gap:56px; }
.hero .side { display:flex; flex-direction:column; gap:16px; padding-bottom:18px; }
.hero .side .k { font-family:"IBM Plex Mono",Menlo,monospace; font-size:24px; letter-spacing:.1em; text-transform:uppercase; color:var(--muted); }
.scale { position:relative; width:640px; height:30px; }
.scale::before { content:""; position:absolute; left:0; right:0; top:13px; height:4px; background:var(--rule); border-radius:2px; }
.scale .fill { position:absolute; left:0; top:13px; height:4px; background:var(--accent); border-radius:2px; }
.scale .dot { position:absolute; top:2px; width:26px; height:26px; margin-left:-13px; border-radius:50%; background:var(--accent); box-shadow:0 0 0 5px var(--paper); }
.scale .tk { position:absolute; top:38px; font-family:"IBM Plex Mono",Menlo,monospace; font-size:18px; color:var(--muted); transform:translateX(-50%); }
.rows { display:grid; }
.r { display:grid; grid-template-columns:minmax(0,1fr) 260px 210px; align-items:baseline; gap:30px; padding:20px 0; border-bottom:2px solid var(--rule); }
.r:first-child { border-top:2px solid var(--rule); }
.r .l { font-size:38px; line-height:1.2; }
.r .d { font-size:26px; color:var(--muted); }
.r .p { font-family:"IBM Plex Mono",Menlo,monospace; font-size:68px; font-weight:500; text-align:right; color:var(--accent); line-height:1; }
.stamp { display:inline-block; font-family:"IBM Plex Mono",Menlo,monospace; font-size:44px; letter-spacing:.08em; font-weight:500; padding:14px 26px; border:5px solid currentColor; }
.stamp.yes { color:var(--yes); } .stamp.no { color:var(--no); }
.verdict { font-family:"Newsreader",Georgia,serif; font-size:56px; font-weight:600; }
.chain { display:grid; grid-auto-flow:column; grid-auto-columns:minmax(0,1fr); gap:70px; }
.step { position:relative; background:var(--surface); border:2px solid var(--rule); border-top:8px solid var(--accent); padding:26px 28px 30px; font-size:32px; line-height:1.3; }
.step b { display:block; font-family:"IBM Plex Mono",Menlo,monospace; font-size:21px; letter-spacing:.1em; text-transform:uppercase; color:var(--accent); margin-bottom:12px; font-weight:500; }
.step:not(:last-child)::after { content:"→"; position:absolute; right:-58px; top:40%; font-size:46px; color:var(--muted); }
.pair { display:grid; grid-template-columns:1fr 1fr; gap:60px; }
.pair div { border-top:6px solid var(--ink); padding-top:18px; }
.pair div.us { border-color:var(--accent); }
.pair b { display:block; font-family:"IBM Plex Mono",Menlo,monospace; font-size:150px; font-weight:500; line-height:1; }
.pair div.us b { color:var(--accent); }
.pair span { display:block; margin-top:16px; font-size:32px; color:var(--muted); }
.foot { margin-top:auto; display:flex; justify-content:space-between; gap:20px; font-family:"IBM Plex Mono",Menlo,monospace; font-size:20px; color:var(--muted); }
.foot b { color:var(--ink); font-weight:500; }
'''
FONTS = ('<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Newsreader:opsz,wght@6..72,400;6..72,600'
         '&family=Public+Sans:wght@400;500;600&family=IBM+Plex+Mono:wght@400;500&display=swap">')
MONTHS = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']


def human_date(s, year=True):
    """'31.12.2026' or '2026-12-31' -> '31 Dec 2026' (or '31 Dec')."""
    for fmt in ('%d.%m.%Y', '%Y-%m-%d'):
        try:
            d = datetime.strptime(s.strip(), fmt)
            return f'{d.day} {MONTHS[d.month - 1]}' + (f' {d.year}' if year else '')
        except (ValueError, AttributeError):
            continue
    return s


def card_doc(kind, inner, foot_left, ctx):
    site = ctx['site'].replace('https://', '').rstrip('/')
    return (f'<!doctype html><html lang="en"><head><meta charset="utf-8">{FONTS}<style>{CARD_CSS}</style></head><body>'
            f'<div class="top"><span>World State Forecast</span><b>{html.escape(kind)}</b></div>{inner}'
            f'<div class="foot"><span>{html.escape(foot_left)}</span><b>{html.escape(site)}</b></div></body></html>')


def official(ctx, q):
    """Latest official value of a question, its edition and the lock date of that edition."""
    eds = sorted(e for (e, qq) in ctx['agg'] if qq == q)
    if not eds:
        sys.exit(f'{q}: no official forecast in registry/forecasts.csv')
    ed = eds[-1]
    ed_row = next((r for r in read_csv('editions.csv') if r['edition'] == ed), {})
    locked = git_date(ed_row.get('freeze_commit', ''))
    return r2(ctx['agg'][(ed, q)]['p']), ed, human_date(locked) if locked else 'date not recorded'


def first_sentence(t, limit=90):
    parts = re.split(r'(?<=[.!?])\s+', t.strip())
    out = parts[0] if parts else t
    if len(out) > limit:
        cut = re.split(r'(?<=[:;])\s+', out)[0]
        out = cut.rstrip(':;') + '.' if len(cut) <= limit else out[:limit].rsplit(' ', 1)[0] + '…'
    return out


def rows_html(rows):
    return '<div class="rows">' + ''.join(
        f'<div class="r"><span class="l">{html.escape(lbl)}</span><span class="d">{html.escape(when)}</span>'
        f'<span class="p">{pct(p)}</span></div>' for lbl, when, p in rows) + '</div>'


def brief_rows(fragment, n):
    out = []
    for q, p, inner in re.findall(r'<tr data-q="(Q-\d{4})" data-p="([\d.]+)"[^>]*>(.*?)</tr>', fragment, flags=re.S):
        cells = re.findall(r'<td[^>]*>(.*?)</td>', inner, flags=re.S)
        out.append((text_of(cells[0]), 'by ' + human_date(text_of(cells[1]), year=False), Decimal(p)))
    return out[:n]


def cards_from_page(ctx, page, headline=None):
    """Cards rendered with the brief: the edition card, one per region, and the scorecard."""
    cards = {}
    locked = f'Forecasts locked {human_date(ctx["freeze_date"])}'
    sections = re.findall(r'<section class="chapter[^"]*"[^>]*>(.*?)</section>', page, flags=re.S)
    head_tbl = re.search(r'<table class="fct" data-card="headline">(.*?)</table>', page, re.S)
    title = headline or f'The world on {human_date(ctx["state"])}'
    cards['edition'] = card_doc('Big picture', f'<h1>{html.escape(title)}</h1>'
                                + (rows_html(brief_rows(head_tbl.group(1), 3)) if head_tbl else ''), locked, ctx)
    for sec in sections:
        k = re.search(r'Region (\d+) of (\d+)', sec)
        if not k:
            continue
        name = text_of(re.search(r'<h2>(.*?)</h2>', sec, re.S).group(1))
        bl = re.search(r'<div class="bl">.*?<p>(.*?)</p>', sec, re.S)
        cards[f'region-{int(k.group(1)):02d}'] = card_doc(
            name, f'<h1 class="mid">{html.escape(first_sentence(text_of(bl.group(1)))) if bl else html.escape(name)}</h1>'
            + rows_html(brief_rows(sec, 2)), locked, ctx)
    cards['scorecard'] = score_card(ctx)
    return cards


def scores_summary(ctx):
    m = re.search(r'^\| AGG_RT \| (\d+) \| ([\d.]+) \| ([\d.]+) \|', ctx['scores'], flags=re.M)
    if not m:
        return None
    return int(m.group(1)), m.group(2), m.group(3)


def score_card(ctx, best=None, worst=None):
    sm = scores_summary(ctx)
    if not sm:
        inner = '<h1>Our track record starts with the next edition</h1>'
    else:
        n, ours, sq = sm
        lines = ''.join(f'<p class="ctx">{html.escape(t)}</p>' for t in (best, worst) if t)
        inner = (f'<h1 class="mid">{n} forecasts settled so far</h1>'
                 f'<div class="pair"><div class="us"><b>{ours}</b><span>our accuracy score</span></div>'
                 f'<div><b>{sq}</b><span>a “nothing changes” guess</span></div></div>'
                 f'<p class="ctx">Lower is better.{" Early numbers: fewer than 30 settled." if n < 30 else ""}</p>{lines}')
    return card_doc('Scorecard', inner, f'Scores from edition {ctx["nr"]}', ctx)


def no_percent(*texts):
    for t in texts:
        if t and '%' in t:
            sys.exit('A probability on a card always comes from the registry. Write other percentages as "percent" '
                     f'(found "%" in: {t!r}).')


def call_card(ctx, q, title, when):
    no_percent(title, when)
    p, ed, locked = official(ctx, q)
    x = float(p) * 100
    inner = (f'<h1>{html.escape(title)}</h1>'
             f'<div class="hero"><span class="big">{pct(p)}</span><div class="side"><span class="k">Our forecast</span>'
             f'<div class="scale"><span class="fill" style="width:{x:.1f}%"></span><span class="dot" style="left:{x:.1f}%"></span>'
             f'<span class="tk" style="left:0">0</span><span class="tk" style="left:50%">50</span><span class="tk" style="left:100%">100</span></div>'
             + (f'<span class="ctx" style="margin-top:26px">{html.escape(when)}</span>' if when else '') + '</div></div>')
    return card_doc('The call', inner, f'Forecast locked {locked}', ctx)


def result_card(ctx, q, title, outcome, note):
    no_percent(title)
    p, ed, locked = official(ctx, q)
    happened = outcome == 'yes'
    if p == Decimal('0.50'):
        verdict = 'A coin flip.'
    else:
        verdict = 'Called it.' if (p > Decimal('0.5')) == happened else 'Missed.'
    inner = (f'<h1 class="mid">{html.escape(title)}</h1>'
             f'<div class="hero"><span class="big">{pct(p)}</span><div class="side"><span class="k">What we had</span>'
             f'<span class="stamp {"yes" if happened else "no"}">{"IT HAPPENED" if happened else "IT DID NOT HAPPEN"}</span></div></div>'
             f'<p class="verdict">{verdict}</p>' + (f'<p class="ctx">{html.escape(note)}</p>' if note else ''))
    return card_doc('Result', inner, f'Forecast locked {locked} · formal score with the next edition', ctx)


def week_card(ctx, title, items):
    if not 1 <= len(items) <= 3:
        sys.exit('week: give 1 to 3 --item "Q-XXXX|label|day"')
    rows, locks = [], set()
    for it in items:
        parts = [x.strip() for x in it.split('|')]
        if len(parts) != 3:
            sys.exit(f'week: item must be "Q-XXXX|label|day", got {it!r}')
        q, label, day = parts
        no_percent(label, day)
        p, ed, locked = official(ctx, q.upper())
        rows.append((label, day, p))
        locks.add(locked)
    return card_doc('This week', f'<h1>{html.escape(title)}</h1>' + rows_html(rows),
                    'Forecasts locked ' + ', '.join(sorted(locks)), ctx)


def chain_card(ctx, title, steps, q=None, label=None):
    if not 2 <= len(steps) <= 3:
        sys.exit('chain: give 2 or 3 --step "Heading|text"')
    no_percent(title, label, *steps)
    boxes = []
    for st in steps:
        head_, _, rest = st.partition('|')
        boxes.append(f'<div class="step"><b>{html.escape(head_.strip())}</b>{html.escape(rest.strip())}</div>')
    tail, foot_left = '', 'Facts from our latest report'
    if q:
        p, ed, locked = official(ctx, q.upper())
        tail = rows_html([(label or '', 'our forecast', p)])
        foot_left = f'Forecast locked {locked}'
    return card_doc('Why it connects', f'<h1 class="mid">{html.escape(title)}</h1><div class="chain">{"".join(boxes)}</div>{tail}',
                    foot_left, ctx)


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


def render_cards(ctx, page, cards_dir, headline=None):
    written = []
    for name, doc in cards_from_page(ctx, page, headline).items():
        target = os.path.join(cards_dir, f'{name}.png')
        png(doc, target)
        written.append(os.path.relpath(target, ROOT))
    return written


def post_card(ctx, a):
    slug = re.sub(r'[^a-z0-9]+', '-', (a.title or a.type).lower()).strip('-')[:40]
    target = path('social', 'cards', 'posts', f'{date.today():%Y-%m-%d}-{a.type}-{slug}.png')
    os.makedirs(os.path.dirname(target), exist_ok=True)
    if a.type == 'call':
        doc = call_card(ctx, a.q.upper(), a.title, a.when)
    elif a.type == 'result':
        doc = result_card(ctx, a.q.upper(), a.title, a.outcome, a.note)
    elif a.type == 'week':
        doc = week_card(ctx, a.title or 'Three things to watch this week', a.item)
    elif a.type == 'chain':
        doc = chain_card(ctx, a.title, a.step, a.q, a.label)
    elif a.type == 'score':
        doc = score_card(ctx, a.best, a.worst)
    else:  # edition: the brief's edition card with a news headline
        page = checked_page(ctx)
        doc = cards_from_page(ctx, page, a.title)['edition']
    png(doc, target)
    print('wrote', os.path.relpath(target, ROOT))
    if sys.platform == 'darwin' and not a.no_reveal:
        subprocess.run(['open', '-R', target], check=False)


def main(argv):
    import argparse
    ap = argparse.ArgumentParser(prog='tools/brief.py', description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest='cmd')
    sub.add_parser('check')
    sub.add_parser('build')
    sub.add_parser('cards')
    c = sub.add_parser('card')
    c.add_argument('type', choices=['call', 'result', 'week', 'chain', 'score', 'edition'])
    c.add_argument('--q', help='question ID (the number is taken from the registry)')
    c.add_argument('--title', help='the headline, in plain words')
    c.add_argument('--when', help='call: when we will know, e.g. "Decided: Wed 28 Oct"')
    c.add_argument('--outcome', choices=['yes', 'no'], help='result: did it happen')
    c.add_argument('--note', help='result: one line on what happened')
    c.add_argument('--item', action='append', default=[], help='week: "Q-XXXX|label|day" (1-3 times)')
    c.add_argument('--step', action='append', default=[], help='chain: "Heading|text" (2-3 times)')
    c.add_argument('--label', help='chain: label of the question that would move')
    c.add_argument('--best', help='score: best call, one line')
    c.add_argument('--worst', help='score: worst miss, one line')
    c.add_argument('--no-reveal', action='store_true', help='do not show the file in Finder')
    a = ap.parse_args(argv[1:] or ['check'])
    ctx = context()
    if a.cmd == 'check':
        checked_page(ctx)
    elif a.cmd in ('build', 'cards'):
        page = checked_page(ctx)
        briefs, cards_dir = out_dirs(ctx)
        if a.cmd == 'build':
            html_file = os.path.join(briefs, f'edition-{ctx["nr"]}.html')
            with open(html_file, 'w', encoding='utf-8') as f:
                f.write(page)
            pdf(html_file, os.path.join(briefs, f'edition-{ctx["nr"]}.pdf'))
            print('wrote', os.path.relpath(html_file, ROOT), 'and', f'docs/briefs/edition-{ctx["nr"]}.pdf')
        for w in render_cards(ctx, page, cards_dir):
            print('wrote', w)
    elif a.cmd == 'card':
        need = {'call': ['q', 'title'], 'result': ['q', 'title', 'outcome'], 'chain': ['title'], 'week': []}.get(a.type, [])
        missing = [n for n in need if not getattr(a, n)]
        if missing:
            ap.error(f'card {a.type} needs ' + ', '.join('--' + m for m in missing))
        post_card(ctx, a)


if __name__ == '__main__':
    main(sys.argv)
