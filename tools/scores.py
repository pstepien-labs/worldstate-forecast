#!/usr/bin/env python3
"""Forecast accuracy scoring (methodology v1.0 §8; v1.1 §1 and §9).

The only script in the project. Reads the CSV registry (separator ';', UTF-8
with BOM) and prints the scores as Markdown.

Usage:
  python3 tools/scores.py                             # all editions, output to screen
  python3 tools/scores.py --to-edition 03 --out editions/.../01_scores.md
  python3 tools/scores.py --bootstrap A B             # confidence interval of the Brier difference A−B
  python3 tools/scores.py --editions 02,03,04         # only forecasts made in these editions
  python3 tools/scores.py --framework 1.1.0           # only editions produced with this framework version
                                                      # (mapping edition -> version: registry/editions.csv)
  python3 tools/scores.py --bank [--bank-edition 04]  # methodology v1.1 question-bank counts (no forecasts read)

Methodology v1.1 (framework 2.0) adds auxiliary tables, never the official measure: v1.0 and v1.1 cohorts,
drivers (registry/question_meta.csv, else the cluster mapping in world_model/drivers.csv), forms, horizon
classes, origins, importance-weighted Brier, actor models (CONDITIONAL questions) and the tail group.

Forecasts of an edition made on or after the question's resolution date are left out
(the outcome was already known; framework 1.5). The "Diagnostics" section is not the
official measure (methodology §1): it shows other reference baselines and lens diversity.
"""
import argparse
import csv
import random
import statistics
from collections import defaultdict
from datetime import date

REG = 'registry/'
RUNS = ['A', 'B', 'C', 'AGG', 'AGG_RT']
BIAS_GROUPS = ['US_WEST', 'EU', 'UKRAINE', 'RUSSIA', 'CHINA', 'IRAN', 'COMPROMISE']


def read(name):
    try:
        with open(REG + name, encoding='utf-8-sig', newline='') as f:
            return list(csv.DictReader(f, delimiter=';'))
    except FileNotFoundError:
        return []


def read_path(path):
    with open(path, encoding='utf-8-sig', newline='') as f:
        return list(csv.DictReader(f, delimiter=';'))


def d(s):
    return date.fromisoformat(s.strip()[:10])


def final_resolutions(rows):
    """Highest version of the resolution for each question."""
    best = {}
    for r in rows:
        qid = r['question_id']
        v = int(r.get('version') or 1)
        if qid not in best or v > best[qid][0]:
            best[qid] = (v, r)
    return {k: v[1] for k, v in best.items()}


def mean(xs):
    return sum(xs) / len(xs) if xs else float('nan')


def fmt(x, n=3):
    return 'n/a' if x != x else f'{x:.{n}f}'


def corr(x, y):
    mx, my = mean(x), mean(y)
    sxy = sum((i - mx) * (j - my) for i, j in zip(x, y))
    sxx, syy = sum((i - mx) ** 2 for i in x), sum((j - my) ** 2 for j in y)
    return sxy / (sxx * syy) ** 0.5 if sxx > 0 and syy > 0 else float('nan')


def diagnostics(pr, official, forecasts, questions, res, outcome, in_scope):
    """Other reference baselines and lens diversity. Not the official measure (methodology §1)."""
    pr('## Diagnostics (not the official measure)\n')
    pr('Methodology §1 keeps BSS vs status quo and vs the crowd as the official measures. '
       'These lines show how hard those baselines are and how independent the lenses are.\n')

    pr('### YES rate by p_status_quo (scored questions)\n')
    pr('| p_status_quo | N questions | YES rate |')
    pr('|---|---|---|')
    by_sq = defaultdict(list)
    for qid in {w[0] for w in official}:
        by_sq[questions[qid]['p_status_quo']].append(outcome[qid])
    for k in sorted(by_sq):
        pr(f'| {k} | {len(by_sq[k])} | {fmt(mean(by_sq[k]), 2)} |')
    pr('')

    pr('### AGG_RT against other reference baselines\n')
    pr('| Reference | N forecasts | Brier AGG_RT | Brier reference | BSS |')
    pr('|---|---|---|---|---|')

    def line(name, pairs):
        if not pairs:
            pr(f'| {name} | 0 | n/a | n/a | n/a |')
            return
        bm, br = mean([x[0] for x in pairs]), mean([x[1] for x in pairs])
        pr(f'| {name} | {len(pairs)} | {fmt(bm)} | {fmt(br)} | {fmt(1 - bm / br if br > 0 else float("nan"))} |')

    line('status quo (official)', [((w[3] - w[4]) ** 2, (float(questions[w[0]]['p_status_quo']) - w[4]) ** 2) for w in official])
    line('constant 0.50', [((w[3] - w[4]) ** 2, 0.25) for w in official])
    # Prior YES rate: share of YES among questions resolved before the forecast date (at least 10).
    resolved_dates = [(d(res[q]['resolution_date']), o) for q, o in outcome.items() if res[q].get('resolution_date')]
    prior = []
    for w in official:
        past = [o for rd, o in resolved_dates if rd < d(w[5])]
        if len(past) >= 10:
            prior.append(((w[3] - w[4]) ** 2, (mean(past) - w[4]) ** 2))
    line('YES rate of earlier resolutions (≥ 10)', prior)
    # Persistence: the same question's AGG_RT in the previous edition (did updating help?).
    agg = {(f['question_id'], f['edition']): float(f['p']) for f in forecasts if f['run'] == 'AGG_RT'}
    pers = []
    for w in official:
        prev = agg.get((w[0], f"{int(w[1]) - 1:02d}"))
        if prev is not None:
            pers.append(((w[3] - w[4]) ** 2, (prev - w[4]) ** 2))
    line("previous edition's AGG_RT", pers)
    pr('')

    pr('### Lens diversity by edition (all forecasts, resolved or not)\n')
    pr('| Edition | N questions | corr A–B | corr A–C | corr B–C | median spread | spread > 0.30 |')
    pr('|---|---|---|---|---|---|---|')
    lens = defaultdict(dict)
    for f in forecasts:
        if f['run'] in ('A', 'B', 'C') and in_scope(f):
            lens[(f['edition'], f['question_id'])][f['run']] = float(f['p'])
    for ed in sorted({k[0] for k in lens}):
        qs = [v for k, v in lens.items() if k[0] == ed and len(v) == 3]
        if not qs:
            continue
        sp = [max(v.values()) - min(v.values()) for v in qs]
        c = [corr([v[x] for v in qs], [v[y] for v in qs]) for x, y in (('A', 'B'), ('A', 'C'), ('B', 'C'))]
        pr(f'| {ed} | {len(qs)} | {fmt(c[0], 2)} | {fmt(c[1], 2)} | {fmt(c[2], 2)} | '
           f'{fmt(statistics.median(sp), 2)} | {sum(x > 0.30 for x in sp)} |')
    pr('')


# ---------------------------------------------------------------- framework 1.9 diagnostics (WP-06)

def horizon_band(days):
    return '<=14' if days <= 14 else ('<=100' if days <= 100 else '>100')


def cluster_boot(items, stat, n=2000, seed=20261117, level=0.90):
    """Bootstrap interval of stat(list of items), resampling whole clusters. items: (cluster, value)."""
    groups = defaultdict(list)
    for c, v in items:
        groups[c].append(v)
    keys = sorted(groups)
    if len(keys) < 2:
        return float('nan'), float('nan')
    rnd = random.Random(seed)
    out = []
    for _ in range(n):
        sample = [v for k in (rnd.choice(keys) for _ in keys) for v in groups[k]]
        out.append(stat(sample))
    out.sort()
    lo = out[int((1 - level) / 2 * n)]
    hi = out[int((1 + level) / 2 * n) - 1]
    return lo, hi


def derived_runs(rows_all):
    """Aggregates computed at scoring time from A, B, C of the same (question, edition). No registry rows."""
    import math
    by = defaultdict(dict)
    meta = {}
    for w in rows_all:
        if w[2] in ('A', 'B', 'C'):
            by[(w[0], w[1])][w[2]] = w[3]
            meta[(w[0], w[1])] = w
    lo = lambda p: math.log(p / (1 - p))
    inv = lambda x: 1 / (1 + math.exp(-x))
    out = []
    for k, v in by.items():
        if len(v) != 3:
            continue
        w = meta[k]
        ps = sorted(v.values())
        m = sum(lo(min(max(p, 0.01), 0.99)) for p in ps) / 3
        for name, p in (('derived:median', ps[1]), ('derived:logodds', inv(m)), ('derived:logodds^1.5', inv(1.5 * m))):
            out.append((w[0], w[1], name, p, w[4], w[5]))
    return out


def diagnostics_19(pr, rows_all, questions, res, outcome, pending, as_of):
    """Closed cohort, intervals, paired differences, derived aggregates, bias. Not the official measure."""
    clus = lambda q: questions[q].get('cluster', '') or q
    sq = lambda q: float(questions[q]['p_status_quo'])
    all_rows = rows_all + derived_runs(rows_all)
    runs = list(RUNS) + sorted({w[2] for w in all_rows} - set(RUNS))

    # Closed cohort
    pr('### Closed cohort (questions whose deadline has passed)\n')
    pr(f'A YES resolves on the day the event happens and a NO only at the deadline, so the set of resolved '
       f'questions over-represents YES while many deadlines are still open. The closed cohort counts only '
       f'questions with a deadline before {as_of.strftime("%d.%m.%Y")}.\n')
    closed = {q for q in outcome if d(questions[q]['deadline']) < as_of}
    overdue = [q for q, x in questions.items() if x.get('status') == 'ACTIVE' and d(x['deadline']) < as_of]
    pr('| Set | N questions | YES rate | Brier AGG_RT | Brier SQ | BSS vs SQ |')
    pr('|---|---|---|---|---|---|')
    for name, qs in (('all resolved', set(outcome)), ('closed cohort', closed)):
        ws = [w for w in rows_all if w[2] == 'AGG_RT' and w[0] in qs]
        if not ws:
            pr(f'| {name} | 0 | n/a | n/a | n/a | n/a |')
            continue
        b, bs = mean([(w[3] - w[4]) ** 2 for w in ws]), mean([(sq(w[0]) - w[4]) ** 2 for w in ws])
        pr(f'| {name} | {len({w[0] for w in ws})} | {fmt(mean([outcome[q] for q in {w[0] for w in ws}]), 2)} | '
           f'{fmt(b)} | {fmt(bs)} | {fmt(1 - b / bs if bs > 0 else float("nan"))} |')
    pr(f'\nActive questions past their deadline and not yet resolved: {len(overdue)} · awaiting verification: {len(pending)}\n')

    # Intervals per run
    pr('### Runs with 90% intervals (cluster bootstrap, 2000 resamples, fixed seed)\n')
    pr('| Run | N | Brier | 90% interval | BSS vs SQ | 90% interval |')
    pr('|---|---|---|---|---|---|')
    for run in runs:
        ws = [w for w in all_rows if w[2] == run]
        if not ws:
            continue
        items = [(clus(w[0]), ((w[3] - w[4]) ** 2, (sq(w[0]) - w[4]) ** 2)) for w in ws]
        brier = lambda xs: mean([x[0] for x in xs])
        bss = lambda xs: 1 - mean([x[0] for x in xs]) / mean([x[1] for x in xs]) if mean([x[1] for x in xs]) > 0 else float('nan')
        vals = [x for _, x in items]
        b_lo, b_hi = cluster_boot(items, brier)
        s_lo, s_hi = cluster_boot(items, bss)
        pr(f'| {run} | {len(ws)} | {fmt(brier(vals))} | [{fmt(b_lo)}, {fmt(b_hi)}] | {fmt(bss(vals))} | [{fmt(s_lo)}, {fmt(s_hi)}] |')
    pr('')

    # Paired differences against AGG_RT
    pr('### Paired difference against AGG_RT (same question and edition)\n')
    pr('Negative = the run was more accurate than the official forecast. An interval containing 0 = no evidence of a difference.\n')
    pr('| Run | N pairs | Mean Brier difference | 90% interval | closer than AGG_RT / further |')
    pr('|---|---|---|---|---|')
    off = {(w[0], w[1]): (w[3] - w[4]) ** 2 for w in rows_all if w[2] == 'AGG_RT'}
    for run in runs:
        if run == 'AGG_RT':
            continue
        diffs = [(clus(w[0]), (w[3] - w[4]) ** 2 - off[(w[0], w[1])]) for w in all_rows
                 if w[2] == run and (w[0], w[1]) in off]
        if not diffs:
            continue
        lo_, hi_ = cluster_boot(diffs, mean)
        better = sum(1 for _, x in diffs if x < -1e-12)
        worse = sum(1 for _, x in diffs if x > 1e-12)
        pr(f'| {run} | {len(diffs)} | {fmt(mean([x for _, x in diffs]))} | [{fmt(lo_)}, {fmt(hi_)}] | {better} / {worse} |')
    pr('')

    # Bias
    pr('### Mean forecast against YES rate (AGG_RT)\n')
    pr('| Group | N | Mean p | YES rate | Difference |')
    pr('|---|---|---|---|---|')
    off_rows = [w for w in rows_all if w[2] == 'AGG_RT']

    def bias_line(name, ws):
        if ws:
            mp, yr = mean([w[3] for w in ws]), mean([w[4] for w in ws])
            pr(f'| {name} | {len(ws)} | {fmt(mp, 2)} | {fmt(yr, 2)} | {fmt(mp - yr, 2)} |')
    bias_line('all', off_rows)
    bias_line('closed cohort', [w for w in off_rows if w[0] in closed])
    for band in ('<=14', '<=100', '>100'):
        bias_line(f'horizon {band} days', [w for w in off_rows
                                            if horizon_band((d(questions[w[0]]['deadline']) - d(w[5])).days) == band])
    for v in sorted({questions[w[0]].get('vector', '') for w in off_rows}):
        bias_line(f'vector {v}', [w for w in off_rows if questions[w[0]].get('vector', '') == v])
    pr('')


def write_base_rates(path, questions, res, outcome, as_of):
    """YES rate by question family from the closed cohort (framework 1.9, WP-11). Laplace-smoothed.
    Levels: vector x horizon band x p_status_quo -> horizon band x p_status_quo -> p_status_quo -> all."""
    fam = defaultdict(list)
    for q, o in outcome.items():
        x = questions.get(q)
        if not x or d(x['deadline']) >= as_of:
            continue
        try:
            band = horizon_band((d(x['deadline']) - d(x['created'])).days)
        except ValueError:
            continue
        keys = [('family', x.get('vector', ''), band, x['p_status_quo']), ('band_sq', '', band, x['p_status_quo']),
                ('sq', '', '', x['p_status_quo']), ('all', '', '', '')]
        for k in keys:
            fam[k].append(o)
    with open(path, 'w', encoding='utf-8-sig', newline='') as f:
        w = csv.writer(f, delimiter=';', quoting=csv.QUOTE_NONNUMERIC)
        w.writerow(['level', 'vector', 'horizon_band', 'p_status_quo', 'n', 'yes', 'yes_rate_smoothed', 'as_of'])
        for k in sorted(fam):
            n, y = len(fam[k]), sum(fam[k])
            w.writerow([k[0], k[1], k[2], k[3], n, y, round((y + 1) / (n + 2), 3), as_of.isoformat()])
    print(f'base rates: {len(fam)} rows from {sum(len(v) for k, v in fam.items() if k[0] == "all")} closed questions -> {path}')



# ---------- methodology v1.1 (framework 2.0): drivers, importance, forms, actor models ----------

DRIVERS = ['D%d' % i for i in range(1, 14)]


def read_csv_path(path):
    try:
        with open(path, encoding='utf-8-sig', newline='') as f:
            return list(csv.DictReader(f, delimiter=';'))
    except FileNotFoundError:
        return []


def load_meta():
    """question_meta.csv: the first row per question counts (the file is append-only; metadata is frozen)."""
    meta = {}
    for r in read('question_meta.csv'):
        meta.setdefault(r.get('id', ''), r)
    return meta


def cluster_drivers(path='world_model/drivers.csv'):
    m = {}
    for r in read_csv_path(path):
        for c in (r.get('clusters') or '').split('|'):
            if c.strip():
                m[c.strip()] = r['code']
    return m


def horizon_class(q):
    try:
        days = (d(q['deadline']) - d(q['created'])).days
    except (KeyError, ValueError):
        return 'unknown'
    return 'Q' if days <= 90 else ('Y' if days <= 365 else 'M')


class Bank:
    """Per-question v1.1 attributes, with fallbacks for questions that have no metadata row."""

    def __init__(self, questions, meta=None, cmap=None):
        self.q = questions
        self.meta = load_meta() if meta is None else meta
        self.cmap = cluster_drivers() if cmap is None else cmap

    def m(self, qid):
        return self.meta.get(qid, {})

    def driver(self, qid):
        return self.m(qid).get('driver') or self.cmap.get(self.q.get(qid, {}).get('cluster', ''), 'unmapped')

    def form(self, qid):
        return self.m(qid).get('form') or 'EVENT (no metadata)'

    def horizon(self, qid):
        return self.m(qid).get('horizon') or horizon_class(self.q.get(qid, {}))

    def origin(self, qid):
        return self.m(qid).get('origin') or 'V1.0'

    def cohort(self, qid):
        return 'v1.1' if self.m(qid).get('rating', '').upper() == 'NEW' else 'v1.0'

    def impact(self, qid, new_only=True):
        r = self.m(qid)
        if new_only and r.get('rating', '').upper() != 'NEW':
            return None
        try:
            return int(r.get('impact', ''))
        except ValueError:
            return None

    def panel(self, qid):
        return self.m(qid).get('panel', '')

    def tail(self, qid):
        return self.m(qid).get('tail', '').upper() == 'Y'


def v11_measures(pr, official, questions, bank):
    """Auxiliary measures of methodology v1.1 §1. Never the official measure."""
    pr('## Methodology v1.1 measures (auxiliary, §1)\n')
    pr('Indicative below about 30 resolved questions per group. Cohort v1.1 = questions with a NEW metadata row; v1.0 = the rest.\n')
    for cohort in ('v1.0', 'v1.1'):
        ws = [w for w in official if bank.cohort(w[0]) == cohort]
        if not ws:
            pr(f'Cohort {cohort}: no resolved questions yet.\n')
            continue
        b = mean([(w[3] - w[4]) ** 2 for w in ws])
        bsq = mean([(float(questions[w[0]]['p_status_quo']) - w[4]) ** 2 for w in ws])
        nt = [w for w in ws if not bank.tail(w[0])]
        bnt = mean([(w[3] - w[4]) ** 2 for w in nt])
        bsqnt = mean([(float(questions[w[0]]['p_status_quo']) - w[4]) ** 2 for w in nt])
        pr(f'Cohort {cohort}: N {len(ws)} · Brier AGG_RT {fmt(b)} · BSS vs SQ {fmt(1 - b / bsq if bsq > 0 else float("nan"))}'
           f' · without the tail group: N {len(nt)}, BSS vs SQ {fmt(1 - bnt / bsqnt if bsqnt > 0 else float("nan"))}\n')

    def table(title, key):
        groups = defaultdict(lambda: defaultdict(list))
        for w in official:
            groups[key(w[0])][bank.cohort(w[0])].append((w[3] - w[4]) ** 2)
        pr(f'## {title}\n')
        pr('| Group | N v1.0 | Brier v1.0 | N v1.1 | Brier v1.1 |')
        pr('|---|---|---|---|---|')
        for g in sorted(groups, key=lambda x: (len(x), x)):
            a_, b_ = groups[g]['v1.0'], groups[g]['v1.1']
            pr(f'| {g} | {len(a_)} | {fmt(mean(a_))} | {len(b_)} | {fmt(mean(b_))} |')
        pr('')

    table('Drivers', bank.driver)
    table('Forms', bank.form)
    table('Horizon classes (creation to deadline: Q ≤90 days, Y 91–365, M >365)', bank.horizon)
    table('Origins', bank.origin)

    pr('## Importance-weighted Brier (AGG_RT; NEW metadata only; weight = impact)\n')
    wts = [(bank.impact(w[0]), (w[3] - w[4]) ** 2) for w in official]
    wts = [(i, x) for i, x in wts if i]
    if wts:
        pr(f'N {len(wts)} · weighted Brier {fmt(sum(i * x for i, x in wts) / sum(i for i, _ in wts))} · unweighted on the same set {fmt(mean([x for _, x in wts]))}\n')
    else:
        pr('No resolved questions with a NEW importance rating yet.\n')

    pr('## Actor models (CONDITIONAL questions by responding actor, AGG_RT)\n')
    groups = defaultdict(list)
    for w in official:
        if bank.form(w[0]) == 'CONDITIONAL':
            groups[bank.m(w[0]).get('actor') or 'unknown'].append((w[3] - w[4]) ** 2)
    if groups:
        pr('| Actor | N | Brier AGG_RT |')
        pr('|---|---|---|')
        for g in sorted(groups):
            pr(f'| {g} | {len(groups[g])} | {fmt(mean(groups[g]))} |')
        pr('')
    else:
        pr('No resolved CONDITIONAL questions yet.\n')


def bank_report(questions, bank, relations, edition=None):
    """Question-bank counts for stage W, stage 08 and the site (methodology v1.1 §4). No forecasts are read."""
    out = []
    pr = out.append
    active = [k for k, q in questions.items() if q.get('status', '').upper() == 'ACTIVE']
    pr('# Question bank (methodology v1.1 §4)\n')
    pr(f'ACTIVE questions: **{len(active)}** (cap 100)\n')
    panel_sets = sorted({bank.panel(k) for k in questions if bank.panel(k)})
    cur_panel = panel_sets[-1] if panel_sets else ''
    panel = [k for k in active if cur_panel and bank.panel(k) == cur_panel]
    pr(f'Current panel set: {cur_panel or "none yet"} · panel questions active: {len(panel)} (target 40)\n')
    pr('## Driver coverage\n')
    pr('| Driver | Active | Panel (floor 2, cap 6) | Mean impact of active (NEW and RETRO ratings) |')
    pr('|---|---|---|---|')
    for dr in DRIVERS + ['unmapped']:
        a_ = [k for k in active if bank.driver(k) == dr]
        p_ = [k for k in panel if bank.driver(k) == dr]
        imps = [bank.impact(k, new_only=False) for k in a_]
        imps = [i for i in imps if i]
        flag = '' if not cur_panel or 2 <= len(p_) <= 6 else ' ⚠'
        if dr == 'unmapped' and not a_:
            continue
        pr(f'| {dr} | {len(a_)} | {len(p_)}{flag} | {fmt(mean(imps), 1) if imps else "n/a"} |')
    pr('')
    pimps = [bank.impact(k, new_only=False) for k in panel]
    pimps = [i for i in pimps if i]
    if pimps:
        pr(f'Panel mean impact: **{fmt(mean(pimps), 2)}** (floor 3.5){" ⚠" if mean(pimps) < 3.5 else ""}\n')
    for title, key in (('Panel by vector (target 5 each)', lambda k: questions[k].get('vector', '')),
                       ('Panel by horizon class (target about 12 Q / 16 Y / 12 M)', bank.horizon)):
        c = defaultdict(int)
        for k in panel:
            c[key(k)] += 1
        pr(f'{title}: ' + (' · '.join(f'{g} {c[g]}' for g in sorted(c)) or 'n/a') + '\n')
    pr(f'Panel tail questions: {sum(1 for k in panel if bank.tail(k))} (target 3–4)\n')
    clusters = defaultdict(int)
    for k in panel:
        clusters[questions[k].get('cluster', '')] += 1
    over = [c for c, n in clusters.items() if n > 3]
    pr(f'Panel clusters above 3: {", ".join(over) if over else "none"}\n')
    eds = sorted({bank.m(k).get('edition', '') for k in questions if bank.m(k).get('rating', '').upper() == 'NEW'})
    ed = edition or (eds[-1] if eds else None)
    if ed:
        new = [k for k in questions if bank.m(k).get('rating', '').upper() == 'NEW' and bank.m(k).get('edition', '') == ed
               and not bank.panel(k)]
        pr(f'## New open questions of edition {ed}: {len(new)} (target 20–30)\n')
        nos = [k for k in new if bank.form(k) != 'SIGNPOST']
        n = len(nos) or 1
        hz = defaultdict(int)
        for k in nos:
            hz[bank.horizon(k)] += 1
        pr(f'Horizons (signposts excluded): Q {hz["Q"]} ({100 * hz["Q"] // n}%, max 50) · Y {hz["Y"]} ({100 * hz["Y"] // n}%, min 25) · M {hz["M"]} ({100 * hz["M"] // n}%, min 15)\n')
        fm = defaultdict(int)
        og = defaultdict(int)
        for k in new:
            fm[bank.form(k)] += 1
            og[bank.origin(k)] += 1
        m_ = len(new) or 1
        pr('Forms: ' + ' · '.join(f'{g} {fm[g]}' for g in sorted(fm)) + f' (LEVEL {100 * fm["LEVEL"] // m_}%, min 20)\n')
        model = sum(v for g, v in og.items() if g in ('LEDGER', 'CHAIN', 'DRIVER_GAP', 'QUIET', 'TAIL'))
        pr('Origins: ' + ' · '.join(f'{g} {og[g]}' for g in sorted(og)) + f' (from the model {100 * model // m_}%, min 60)\n')
        conds = [k for k in new if bank.form(k) == 'CONDITIONAL']
        linked = {r['question_a'] for r in relations if r.get('relation', '').strip() == 'conditional_on'}
        pr(f'CONDITIONAL questions: {len(conds)} (min 3 pairs when chains are active) · without a conditional_on relation: '
           f'{", ".join(sorted(set(conds) - linked)) or "none"}\n')
        longq = [k for k in active if bank.horizon(k) == 'M' and bank.cohort(k) == 'v1.1']
        sp = defaultdict(int)
        for k in questions:
            if bank.m(k).get('signpost_of'):
                sp[bank.m(k)['signpost_of']] += 1
        short = [k for k in longq if sp[k] < 2]
        pr(f'M questions with fewer than 2 signposts: {", ".join(sorted(short)) or "none"}\n')
    missing = [k for k in active if k not in bank.meta]
    pr(f'ACTIVE questions without a metadata row: {len(missing)}\n')
    return '\n'.join(out)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--to-edition', default=None, help='include forecasts up to and including this edition (e.g. 03)')
    ap.add_argument('--out', default=None)
    ap.add_argument('--bootstrap', nargs=2, metavar=('P1', 'P2'), default=None)
    ap.add_argument('--n-boot', type=int, default=2000)
    ap.add_argument('--editions', default=None, help='comma-separated editions to include (e.g. 02,03)')
    ap.add_argument('--framework', default=None, help='include only editions produced with this framework version')
    ap.add_argument('--add-forecasts', default=None, help='add the rows of this file (e.g. a replay, framework 1.9) to '
                    'the registry forecasts; their runs appear in the diagnostics, not in the official tables')
    ap.add_argument('--as-of', default=None, help='date for the closed cohort (default: today)')
    ap.add_argument('--bank', action='store_true', help='methodology v1.1: question-bank counts (drivers, panel, horizons, '
                    'forms, origins) and stop; reads no forecasts')
    ap.add_argument('--bank-edition', default=None, help='with --bank: the edition whose new questions are counted')
    ap.add_argument('--base-rates', default=None, metavar='OUT',
                    help='write YES rates by question family from the closed cohort to OUT (CSV) and stop')
    a = ap.parse_args()
    fw_of = {r['edition']: r.get('framework_version', '') for r in read('editions.csv')}
    only_editions = {e.strip().zfill(2) for e in a.editions.split(',')} if a.editions else None

    questions = {q['id']: q for q in read('questions.csv')}
    bank = Bank(questions)
    if a.bank:
        text = bank_report(questions, bank, read('relations.csv'), a.bank_edition)
        if a.out:
            with open(a.out, 'w', encoding='utf-8') as f:
                f.write(text)
        print(text)
        return
    forecasts = read('forecasts.csv') + (read_path(a.add_forecasts) if a.add_forecasts else [])
    res = final_resolutions(read('resolutions.csv'))
    bench = read('benchmarks.csv')

    # Scored resolutions: outcome 0/1; those awaiting verification kept separately.
    outcome, pending, void, auto_verified = {}, [], [], []
    for qid, r in res.items():
        o = r['outcome'].strip().upper()
        if o == 'VOID':
            void.append(qid)
            continue
        # user_approved: Y = the user approved; A = confirmed by an independent automatic re-check (stage V,
        # framework 1.8); anything else = still awaiting verification and left out of the scores.
        appr = r.get('user_approved', '').strip().upper()
        if r.get('verify', '').strip().upper() == 'Y' and appr not in ('Y', 'A'):
            pending.append(qid)
            continue
        if o in ('0', '1'):
            outcome[qid] = int(o)
            if appr == 'A':
                auto_verified.append(qid)

    def in_scope(p):
        if a.to_edition and int(p['edition']) > int(a.to_edition):
            return False
        if only_editions and p['edition'].zfill(2) not in only_editions:
            return False
        if a.framework and fw_of.get(p['edition'].zfill(2), '') != a.framework:
            return False
        return True

    # Latest forecast date of each (question, edition): the date the edition's information set closed.
    latest = {}
    for p in forecasts:
        k = (p['question_id'], p['edition'])
        try:
            latest[k] = max(latest.get(k, d(p['date'])), d(p['date']))
        except ValueError:
            pass

    as_of = d(a.as_of) if a.as_of else date.today()
    if a.base_rates:
        write_base_rates(a.base_rates, questions, res, outcome, as_of)
        return

    rows_all = []  # (qid, edition, run, p, o, date)
    known = set()  # (qid, edition) forecast on or after the resolution date
    for p in forecasts:
        qid = p['question_id']
        if qid not in outcome or not in_scope(p):
            continue
        try:
            if d(res[qid]['resolution_date']) <= latest[(qid, p['edition'])]:
                known.add((qid, p['edition']))
                continue
        except (KeyError, ValueError):
            pass
        rows_all.append((qid, p['edition'], p['run'], float(p['p']), outcome[qid], p['date']))

    out = []
    pr = out.append
    pr('# Accuracy scores\n')
    pr(f'Resolved and scored questions: **{len(outcome)}** (of which auto-verified: {len(auto_verified)}) · awaiting verification: {len(pending)} · void: {len(void)}\n')
    if len(outcome) < 30:
        pr('> Fewer than 30 resolved questions — indicative scores, no conclusions about the method.\n')

    # Brier by run (each forecast separately) and BSS vs status quo on the same set.
    pr('## Runs\n')
    pr('| Run | N forecasts | Brier | Brier SQ (same set) | BSS vs SQ | Mean Brier per question |')
    pr('|---|---|---|---|---|---|')
    for run in RUNS:
        rows = [w for w in rows_all if w[2] == run]
        if not rows:
            pr(f'| {run} | 0 | n/a | n/a | n/a | n/a |')
            continue
        b = [(w[3] - w[4]) ** 2 for w in rows]
        bsq = [(float(questions[w[0]]['p_status_quo']) - w[4]) ** 2 for w in rows]
        per_q = defaultdict(list)
        for w, x in zip(rows, b):
            per_q[w[0]].append(x)
        bq = mean([mean(v) for v in per_q.values()])
        bss = 1 - mean(b) / mean(bsq) if mean(bsq) > 0 else float('nan')
        pr(f'| {run} | {len(rows)} | {fmt(mean(b))} | {fmt(mean(bsq))} | {fmt(bss)} | {fmt(bq)} |')
    pr('')

    official = [w for w in rows_all if w[2] == 'AGG_RT']

    # Crowd: EXACT matches from the same edition.
    pr('## AGG_RT vs crowd (EXACT matches only)\n')
    bmap = defaultdict(list)
    for r in bench:
        if r.get('match', '').strip().upper() == 'EXACT':
            bmap[(r['question_id'], r['edition'])].append(float(r['p']))
    pairs = []
    for w in official:
        key = (w[0], w[1])
        if key in bmap:
            pc = mean(bmap[key])
            pairs.append(((w[3] - w[4]) ** 2, (pc - w[4]) ** 2))
    if pairs:
        bm, bc = mean([x[0] for x in pairs]), mean([x[1] for x in pairs])
        bss_c = 1 - bm / bc if bc > 0 else float('nan')
        pr(f'N pairs: {len(pairs)} · Brier AGG_RT: {fmt(bm)} · Brier crowd: {fmt(bc)} · BSS vs crowd: {fmt(bss_c)}\n')
    else:
        pr('No resolved questions with a matched benchmark.\n')

    # AGG_RT calibration.
    pr('## AGG_RT calibration\n')
    pr('| Bin | N | Mean p | YES frequency |')
    pr('|---|---|---|---|')
    bins = defaultdict(list)
    for w in official:
        k = min(int(w[3] * 10), 9)
        bins[k].append(w)
    for k in range(10):
        ws = bins.get(k, [])
        pr(f'| {k*10}–{k*10+10}% | {len(ws)} | {fmt(mean([x[3] for x in ws]), 2)} | {fmt(mean([x[4] for x in ws]), 2)} |')
    pr('')

    # Directional bias.
    pr('## AGG_RT directional bias (mean p − outcome; neutral ≈ 0)\n')
    pr('| who_benefits | N | Mean signed error |')
    pr('|---|---|---|')
    for g in BIAS_GROUPS:
        ws = [w for w in official if questions[w[0]].get('who_benefits', '').strip().upper() == g]
        pr(f'| {g} | {len(ws)} | {fmt(mean([w[3] - w[4] for w in ws]))} |')
    pr('')

    # Breakdowns: cluster (weight 1 per cluster), vector, horizon.
    def breakdown(title, key):
        groups = defaultdict(list)
        for w in official:
            groups[key(w)].append((w[3] - w[4]) ** 2)
        pr(f'## {title}\n')
        pr('| Group | N | Brier AGG_RT |')
        pr('|---|---|---|')
        for g in sorted(groups):
            pr(f'| {g} | {len(groups[g])} | {fmt(mean(groups[g]))} |')
        pr('')
        return groups

    gk = breakdown('Clusters', lambda w: questions[w[0]].get('cluster', '') or 'NONE')
    pr(f'Brier AGG_RT with a weight of 1 per cluster: **{fmt(mean([mean(v) for v in gk.values()]))}**\n')
    breakdown('Vectors', lambda w: questions[w[0]].get('vector', ''))
    breakdown('Editions (forecast made in)', lambda w: w[1])
    breakdown('Framework versions (registry/editions.csv)', lambda w: fw_of.get(w[1].zfill(2), '') or 'unregistered')

    def horizon(w):
        try:
            days = (d(questions[w[0]]['deadline']) - d(w[5])).days
        except Exception:
            return 'unknown'
        return '≤14 days' if days <= 14 else ('≤100 days' if days <= 100 else '>100 days')
    breakdown('Horizons (from forecast date to deadline)', horizon)

    if pending:
        pr('## Awaiting user verification\n')
        pr(', '.join(sorted(pending)) + '\n')
    if auto_verified:
        pr('## Auto-verified (independent automatic re-check, not reviewed by the user)\n')
        pr(', '.join(sorted(auto_verified)) + '\n')

    if known:
        pr('## Left out: forecast on or after the resolution date\n')
        pr(', '.join(f'{q} (edition {e})' for q, e in sorted(known)) + '\n')

    diagnostics(pr, official, forecasts, questions, res, outcome, in_scope)
    diagnostics_19(pr, rows_all, questions, res, outcome, pending, as_of)
    v11_measures(pr, official, questions, bank)

    # Cluster bootstrap for the Brier difference between two runs.
    if a.bootstrap:
        p1, p2 = a.bootstrap
        paired = defaultdict(dict)
        for w in rows_all:
            if w[2] in (p1, p2):
                paired[(w[0], w[1])][w[2]] = (w[3] - w[4]) ** 2
        par = [(k[0], v[p1] - v[p2]) for k, v in paired.items() if p1 in v and p2 in v]
        clusters = defaultdict(list)
        for qid, diff in par:
            clusters[questions[qid].get('cluster', '') or qid].append(diff)
        keys = list(clusters)
        random.seed(12345)
        stats = []
        for _ in range(a.n_boot):
            sample = [x for k in (random.choice(keys) for _ in keys) for x in clusters[k]]
            stats.append(mean(sample))
        stats.sort()
        lo, hi = stats[int(0.025 * len(stats))], stats[int(0.975 * len(stats)) - 1]
        pr(f'## Bootstrap: Brier {p1} − Brier {p2}\n')
        pr(f'Pairs: {len(par)} · clusters: {len(keys)} · mean difference: {fmt(mean([x[1] for x in par]))} · 95% CI: [{fmt(lo)}, {fmt(hi)}]')
        pr('A negative value means the first run is more accurate. An interval that includes 0 = no evidence of a difference.\n')

    text = '\n'.join(out)
    if a.out:
        with open(a.out, 'w', encoding='utf-8') as f:
            f.write(text)
    print(text)


if __name__ == '__main__':
    main()
