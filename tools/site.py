#!/usr/bin/env python3
"""Build the public landing page and the open data pack from the registry.

  python3 tools/site.py            writes docs/ (GitHub Pages) and site/preview.html

Outputs
  docs/index.html          landing page (served by GitHub Pages from /docs on main)
  docs/llms.txt            guide for AI assistants: what the project is, where the data is
  docs/data/forecasts.json latest official forecasts with question metadata
  docs/data/*.csv          copies of the public registry files
  site/preview.html        the same page as a fragment (for previews)

Only material the project produces itself is published: no harvested news
text and no benchmark (crowd/market) values. Python standard library only.
"""
import csv
import html
import json
import os
import shutil
from collections import defaultdict
from datetime import date, datetime, timedelta, timezone

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
VECTORS = ['MIL', 'ENE', 'ECO', 'FIN', 'TEC', 'DIP', 'DOM', 'INF']
PUBLIC_REGISTRY = ['questions.csv', 'forecasts.csv', 'resolutions.csv', 'editions.csv']
MIN_GAP_DAYS = 14


def read_csv(name):
    p = os.path.join(ROOT, 'registry', name)
    if not os.path.exists(p):
        return []
    with open(p, encoding='utf-8-sig', newline='') as f:
        return list(csv.DictReader(f, delimiter=';'))


def read_text(p):
    with open(os.path.join(ROOT, p), encoding='utf-8') as f:
        return f.read()


def current():
    out = {}
    for line in read_text('editions/CURRENT.md').splitlines():
        if '=' in line and line.split('=', 1)[0].isupper():
            k, v = line.split('=', 1)
            out[k.strip()] = v.strip()
    return out


def e(s):
    return html.escape('' if s is None else str(s), quote=True)


def ddmmyyyy(iso):
    try:
        return datetime.strptime(iso, '%Y-%m-%d').strftime('%d.%m.%Y')
    except (TypeError, ValueError):
        return iso or ''


def pct(p):
    return f'{round(float(p) * 100)}%'


def load():
    questions = {q['id']: q for q in read_csv('questions.csv')}
    forecasts = read_csv('forecasts.csv')
    editions = read_csv('editions.csv')
    res_rows = read_csv('resolutions.csv')
    latest_ed = max((f['edition'] for f in forecasts if f['run'] == 'AGG_RT'), default=None)
    official, spread = {}, defaultdict(list)
    for f in forecasts:
        if f['edition'] != latest_ed:
            continue
        if f['run'] == 'AGG_RT':
            official[f['question_id']] = f
        elif f['run'] in ('A', 'B', 'C'):
            spread[f['question_id']].append(float(f['p']))
    final = {}
    for r in res_rows:
        q = r['question_id']
        if q not in final or int(r['version']) > int(final[q]['version']):
            final[q] = r
    outcomes = {}
    for q, r in final.items():
        o = r['outcome'].strip().upper()
        if o in ('0', '1') and not (r.get('verify', '').upper() == 'Y' and r.get('user_approved', '').upper() != 'Y'):
            outcomes[q] = int(o)
    return questions, forecasts, editions, official, spread, outcomes, latest_ed


def scores(forecasts, questions, outcomes):
    rows = [f for f in forecasts if f['run'] == 'AGG_RT' and f['question_id'] in outcomes]
    if not rows:
        return None
    b = sum((float(f['p']) - outcomes[f['question_id']]) ** 2 for f in rows) / len(rows)
    sq = [(float(questions[f['question_id']]['p_status_quo']) - outcomes[f['question_id']]) ** 2
          for f in rows if questions.get(f['question_id'], {}).get('p_status_quo')]
    bsq = sum(sq) / len(sq) if sq else None
    return {'n_questions': len(outcomes), 'n_forecasts': len(rows), 'brier': b, 'brier_sq': bsq,
            'bss': (1 - b / bsq) if bsq else None}


def pick_ledger(questions, official, n, today):
    cand = [q for qid, q in questions.items() if qid in official and q.get('status') == 'ACTIVE' and q.get('deadline', '') >= today]
    if len(cand) < n:
        cand = [q for qid, q in questions.items() if qid in official and q.get('status') == 'ACTIVE']
    by_vec = defaultdict(list)
    for q in sorted(cand, key=lambda q: (q['deadline'], q['id'])):
        by_vec[q['vector'].split('/')[0]].append(q)
    out = []
    while len(out) < n and any(by_vec.values()):
        for v in VECTORS + sorted(set(by_vec) - set(VECTORS)):
            if by_vec.get(v):
                out.append(by_vec[v].pop(0))
                if len(out) >= n:
                    break
    return sorted(out, key=lambda q: (q['deadline'], q['id']))


def page_head(cfg, desc):
    return ('<!doctype html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n'
            '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n'
            f'<meta name="description" content="{desc}">\n<meta property="og:title" content="{e(cfg["name"])}">\n'
            f'<meta property="og:description" content="{desc}">\n<meta property="og:type" content="website">\n'
            f'<meta property="og:url" content="{e(cfg.get("site_url", ""))}">\n'
            '<style>img{max-width:100%}[hidden]{display:none!important}body{margin:0}</style>\n')


def build():
    cfg = json.load(open(os.path.join(ROOT, 'site', 'config.json'), encoding='utf-8'))
    repo = cfg['repo_url'].rstrip('/')
    cur = current()
    today = datetime.now(timezone.utc).date().isoformat()
    questions, forecasts, editions, official, spread, outcomes, latest_ed = load()
    ed_row = next((r for r in editions if r['edition'] == latest_ed), {})
    framework = read_text('VERSION').strip()
    state_date = cur.get('STATE_DATE', '')
    next_date = (datetime.strptime(state_date, '%Y-%m-%d').date() + timedelta(days=MIN_GAP_DAYS)).isoformat() if state_date else ''
    report_dir = ed_row.get('directory') or cur.get('DIRECTORY', '')
    latest_report_url = f'{repo}/blob/main/{report_dir}/07_report.md'
    sc = scores(forecasts, questions, outcomes)

    # featured ticket
    fq = cfg.get('featured_question')
    if fq not in official:
        fq = next(iter(sorted(official)), None)
    featured = ''
    if fq:
        q, f = questions[fq], official[fq]
        p = float(f['p'])
        lo, hi = (min(spread[fq]), max(spread[fq])) if spread.get(fq) else (p, p)
        freeze = ed_row.get('freeze_commit', '')
        featured = f'''<aside class="ticket" aria-label="Example of a frozen forecast">
        <span class="stamp">FROZEN</span>
        <p class="label">{e(fq)} · {e(q['vector'])} · {e(q.get('pir', ''))}</p>
        <p class="q">{e(q['question'])}</p>
        <p class="p">{pct(p)}<small>official forecast</small></p>
        <div class="scale" aria-hidden="true"><span class="track"></span>
          <span class="spread" style="left:{lo * 100:.1f}%;width:{max(0.6, (hi - lo) * 100):.1f}%"></span>
          <span class="mark" style="left:calc({p * 100:.1f}% - 1px)"></span>
          <span class="ticks"><span>0</span><span>50</span><span>100</span></span></div>
        <dl>
          <dt>edition</dt><dd>{e(latest_ed)} · state {e(ddmmyyyy(ed_row.get('state_date')))}</dd>
          <dt>frozen in</dt><dd><a href="{e(repo)}/commit/{e(freeze)}">commit {e(freeze)}</a></dd>
          <dt>lens spread</dt><dd>{pct(lo)}–{pct(hi)} (three blind lenses)</dd>
          <dt>resolves</dt><dd>{e(ddmmyyyy(q['deadline']))} · source: {e(q.get('resolution_source', '')[:60])}</dd>
        </dl>
      </aside>'''

    # status strip
    n_editions = len([r for r in editions if r.get('methodology_version', '').startswith('v')])
    active = sum(1 for q in questions.values() if q.get('status') == 'ACTIVE')
    stats = [(n_editions, 'edition published' if n_editions == 1 else 'editions published'), (active, 'open questions'), (len(outcomes), 'resolved and scored'),
             (ddmmyyyy(next_date), 'next edition (earliest)'), (f"{cfg.get('harvest_languages', '')}", 'languages harvested')]
    stats_html = ''.join(f'<div><b>{e(v)}</b><span>{e(t)}</span></div>' for v, t in stats)

    # ledger
    rows = []
    for q in pick_ledger(questions, official, int(cfg.get('forecasts_on_page', 12)), today):
        p = float(official[q['id']]['p'])
        rows.append(f'<div class="row" role="row"><span class="id" role="cell">{e(q["id"])}</span>'
                    f'<span class="qt" role="cell">{e(q["question"])}</span>'
                    f'<span class="date" role="cell">{e(ddmmyyyy(q["deadline"]))}</span>'
                    f'<span class="prob" role="cell"><span class="bar"><i style="width:{p * 100:.1f}%"></i></span><b>{pct(p)}</b></span>'
                    f'<span class="vec" role="cell">{e(q["vector"])}</span></div>')
    ledger_note = (f'Official forecasts (aggregate of three blind lenses after red team) from edition {e(latest_ed)}, '
                   f'frozen in commit {e(ed_row.get("freeze_commit", ""))}. All {len(official)} forecasts: '
                   f'<a href="{e(repo)}/blob/main/registry/forecasts.csv">registry/forecasts.csv</a> · '
                   f'<a href="data/forecasts.json">forecasts.json</a>.')

    # track record
    if not sc:
        track = (f'<div class="track-box"><p class="big">No question has resolved yet. The first scores arrive with the next edition '
                 f'(earliest {e(ddmmyyyy(next_date))}), when the questions due in early October are checked.</p>'
                 f'<div><p>Misses will be published as prominently as hits. Below 30 resolved questions the scores are labelled '
                 f'indicative and no conclusions are drawn about the method.</p>'
                 f'<p>Each edition\'s scores are in its <code class="mono">01_scores.md</code>, computed by '
                 f'<a href="{e(repo)}/blob/main/tools/scores.py">tools/scores.py</a>.</p></div></div>')
    else:
        label = 'indicative' if sc['n_questions'] < 30 else 'measured'
        bss = f"{sc['bss']:+.2f}" if sc['bss'] is not None else 'n/a'
        bsq = f"{sc['brier_sq']:.3f}" if sc['brier_sq'] is not None else 'n/a'
        track = (f'<div class="track-box"><p class="big">{sc["n_questions"]} questions resolved. Brier score of the official forecast: '
                 f'<span class="mono">{sc["brier"]:.3f}</span> against <span class="mono">{bsq}</span> for "nothing changes" '
                 f'(skill {bss}, {label}).</p><div><p>Lower is better. A positive skill score means the forecasts beat the status-quo baseline. '
                 f'Full breakdown by lens, vector and horizon: the latest <code class="mono">01_scores.md</code>.</p>'
                 f'<p>Below 30 resolved questions the numbers are indicative only.</p></div></div>')

    # data & access
    data_rows = [
        ('Reports', 'Every edition: facts with sources, analysis, scenarios, forecasts, quality control', 'Markdown',
         f'<span class="pill free">free · CC BY 4.0</span> <a href="{e(latest_report_url)}">latest</a> · <a href="{e(repo)}/tree/main/editions">all</a>'),
        ('Forecast registry', 'Questions with resolution criteria, every forecast by lens and official, resolutions, edition versions', 'CSV, JSON',
         f'<span class="pill free">free · CC BY 4.0</span> <a href="data/forecasts.json">JSON</a> · <a href="{e(repo)}/tree/main/registry">CSV</a>'),
        ('Methodology and prompts', 'The method, every stage instruction, the source map and harvester configuration', 'Markdown, CSV',
         f'<span class="pill free">free · CC BY 4.0</span> <a href="{e(repo)}/blob/main/methodology/methodology_v1.0.md">method</a> · <a href="{e(repo)}/tree/main/prompts">prompts</a>'),
        ('For AI assistants', 'A guide that lets any AI assistant read and query the forecasts and reports', 'llms.txt, JSON',
         '<span class="pill free">free</span> <a href="llms.txt">llms.txt</a>'),
        ('Software', 'Harvester, scoring, pipeline: run your own independent forecast series', 'Python',
         f'<span class="pill free">free · MIT</span> <a href="{e(repo)}">repository</a>'),
        ('Harvested news', 'Headlines and snippets collected from about 200 publishers', '—',
         '<span class="pill">not redistributed</span> copyright stays with the publishers; coverage statistics are published in each edition'),
        ('For organisations', 'Custom questions on your topic, a structured data feed, briefings', 'on request',
         '<span class="pill">planned</span> register interest via the contact below'),
    ]
    data_html = '\n            '.join(f'<tr><td class="k">{e(a)}</td><td>{e(b)}</td><td class="mono">{e(c)}</td><td>{d}</td></tr>' for a, b, c, d in data_rows)

    # support + contact
    names = {'github_sponsors': 'GitHub Sponsors', 'open_collective': 'Open Collective', 'kofi': 'Ko-fi'}
    links = [(names.get(k, k), v) for k, v in (cfg.get('donate') or {}).items() if v]
    if links:
        support = '<div class="support-links">' + ''.join(f'<a class="btn" href="{e(u)}">{e(n)}</a>' for n, u in links) + '</div>'
    else:
        support = ('<p style="margin-top:16px">Donation options are being set up. Until then, the most useful support is a star on '
                   f'<a href="{e(repo)}">GitHub</a> and sharing a report with someone who will argue with it.</p>')
    contact = ''
    if cfg.get('contact_email'):
        em = e(cfg['contact_email'])
        contact += (f'<p style="margin-top:22px" class="label">Contact</p><div class="copy"><code>{em}</code>'
                    f'<button type="button" data-copy="{em}">Copy</button></div>')
    if cfg.get('x_handle'):
        h = cfg['x_handle'].strip().rstrip('/')
        for prefix in ('https://', 'http://', 'www.', 'x.com/', 'twitter.com/', '@'):
            if h.lower().startswith(prefix):
                h = h[len(prefix):]
        h = h.split('?')[0]
        contact += f'<p style="margin-top:12px">Signals between editions: <a href="https://x.com/{e(h)}">@{e(h)} on X</a></p>'

    footer = (f'Framework {e(framework)} · methodology {e(cur.get("METHODOLOGY", "v1.0"))} · latest edition {e(latest_ed)} '
              f'(state {e(ddmmyyyy(ed_row.get("state_date")))}) · page built {datetime.now(timezone.utc):%d.%m.%Y}')

    tpl = read_text('site/template.html')
    for k, v in {'NAME': e(cfg['name']), 'REPO': e(repo), 'LATEST_REPORT_URL': e(latest_report_url), 'FEATURED': featured,
                 'STATS': stats_html, 'LEDGER': '\n        '.join(rows), 'LEDGER_NOTE': ledger_note, 'TRACK': track,
                 'DATA_ROWS': data_html, 'SUPPORT': support, 'CONTACT': contact, 'FOOTER_META': footer,
                 'SOURCES': e(cfg.get('harvest_sources', '')), 'LANGUAGES': e(cfg.get('harvest_languages', ''))}.items():
        tpl = tpl.replace('{{' + k + '}}', v)
    assert '{{' not in tpl, 'unfilled placeholder in site/template.html'

    with open(os.path.join(ROOT, 'site', 'preview.html'), 'w', encoding='utf-8') as f:
        f.write(tpl)

    # legal notice page (shares the landing page's stylesheet)
    style = tpl[tpl.index('<style>'):tpl.index('</style>') + len('</style>')]
    operator = e(cfg.get('operator_name')) or 'the maintainer of its <a href="' + e(repo) + '">GitHub repository</a>'
    if cfg.get('contact_email'):
        em = e(cfg['contact_email'])
        contact_block = (f'<p>Contact for questions, corrections, opt-out and takedown requests:</p>'
                         f'<div class="copy"><code>{em}</code><button type="button" data-copy="{em}">Copy</button></div>')
    else:
        contact_block = (f'<p>Contact for questions, corrections, opt-out and takedown requests: open an issue in the '
                         f'<a href="{e(repo)}/issues">repository</a>.</p>')
    legal = read_text('site/legal.html')
    for k, v in {'NAME': e(cfg['name']), 'REPO': e(repo), 'STYLE': style, 'OPERATOR': operator,
                 'CONTACT_BLOCK': contact_block, 'UPDATED': e(cfg.get('legal_updated') or datetime.now(timezone.utc).strftime('%d.%m.%Y')),
                 'FOOTER_META': footer}.items():
        legal = legal.replace('{{' + k + '}}', v)
    assert '{{' not in legal, 'unfilled placeholder in site/legal.html'
    legal += tpl[tpl.rindex('<script>'):]  # copy-button script
    with open(os.path.join(ROOT, 'site', 'preview_legal.html'), 'w', encoding='utf-8') as f:
        f.write(legal)
    split = tpl.index('<div class="wrap">')
    head, body = tpl[:split], tpl[split:]
    desc = e(cfg.get('tagline', ''))
    page = page_head(cfg, desc) + f'{head}</head>\n<body>\n{body}</body>\n</html>\n'
    docs = os.path.join(ROOT, 'docs')
    os.makedirs(os.path.join(docs, 'data'), exist_ok=True)
    with open(os.path.join(docs, 'index.html'), 'w', encoding='utf-8') as f:
        f.write(page)
    lsplit = legal.index('<div class="wrap">')
    with open(os.path.join(docs, 'legal.html'), 'w', encoding='utf-8') as f:
        f.write(page_head(cfg, desc) + legal[:lsplit] + '</head>\n<body>\n' + legal[lsplit:] + '</body>\n</html>\n')
    open(os.path.join(docs, '.nojekyll'), 'w').close()
    for name in PUBLIC_REGISTRY:
        src = os.path.join(ROOT, 'registry', name)
        if os.path.exists(src):
            shutil.copyfile(src, os.path.join(docs, 'data', name))
    payload = {
        'project': cfg['name'], 'generated': datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ'),
        'framework_version': framework, 'methodology_version': cur.get('METHODOLOGY', 'v1.0'),
        'edition': latest_ed, 'state_date': ed_row.get('state_date'), 'freeze_commit': ed_row.get('freeze_commit'),
        'licence': 'CC BY 4.0', 'note': 'p = official forecast (AGG_RT): mean of three blind lenses after red-team adjustment. Probabilities 0.01-0.99.',
        'forecasts': [{'id': qid, 'question': questions[qid]['question'], 'resolution_criterion': questions[qid].get('resolution_criterion'),
                       'resolution_source': questions[qid].get('resolution_source'), 'deadline': questions[qid].get('deadline'),
                       'vector': questions[qid].get('vector'), 'region': questions[qid].get('region'), 'cluster': questions[qid].get('cluster'),
                       'status': questions[qid].get('status'), 'p': float(f['p']),
                       'lens_min': min(spread[qid]) if spread.get(qid) else None, 'lens_max': max(spread[qid]) if spread.get(qid) else None,
                       'outcome': outcomes.get(qid)}
                      for qid, f in sorted(official.items()) if qid in questions],
    }
    with open(os.path.join(docs, 'data', 'forecasts.json'), 'w', encoding='utf-8') as f:
        json.dump(payload, f, ensure_ascii=False, indent=1)
    site = cfg.get('site_url', '').rstrip('/')
    llms = f"""# {cfg['name']}

> {cfg.get('tagline', '')}

An open research experiment: an AI-assisted process forecasts great-power moves every two weeks, freezes every forecast in an append-only registry before the outcome, and scores itself with Brier scores against a status-quo baseline and forecasting crowds. Facts are sourced from three perspectives (Western, the actor's side, a third party). Not investment or political advice.

Current: framework {framework}, methodology {cur.get('METHODOLOGY', 'v1.0')}, latest edition {latest_ed} (state date {ed_row.get('state_date')}), {active} open questions, {len(outcomes)} resolved.

## Data (CC BY 4.0)
- [Latest official forecasts, JSON]({site}/data/forecasts.json): id, question, resolution criterion and source, deadline, p (0.01-0.99), lens range, outcome if resolved
- [Questions CSV]({site}/data/questions.csv), [all forecasts by lens CSV]({site}/data/forecasts.csv), [resolutions CSV]({site}/data/resolutions.csv), [editions and versions CSV]({site}/data/editions.csv) — separator ';', UTF-8 with BOM

## Reports
- [Latest report]({latest_report_url})
- [All editions]({repo}/tree/main/editions)

## Method
- [Methodology]({repo}/blob/main/methodology/methodology_v1.0.md)
- [Stage prompts]({repo}/tree/main/prompts)
- [Rules]({repo}/blob/main/CLAUDE.md)

## How to answer questions about this project
- Quote forecasts with their question ID, edition and deadline; they are frozen and never edited.
- A forecast is a probability, not a prediction that the event will or will not happen.
- Say when a question has resolved and give the outcome from resolutions.csv.
"""
    with open(os.path.join(docs, 'llms.txt'), 'w', encoding='utf-8') as f:
        f.write(llms)
    print(f'site built: docs/index.html ({len(page) // 1024} KB), {len(payload["forecasts"])} forecasts, '
          f'{len(outcomes)} resolved, featured {fq}; preview: site/preview.html')


if __name__ == '__main__':
    build()
