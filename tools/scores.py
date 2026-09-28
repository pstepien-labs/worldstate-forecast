#!/usr/bin/env python3
"""Forecast accuracy scoring (methodology v1.0, §8).

The only script in the project. Reads the CSV registry (separator ';', UTF-8
with BOM) and prints the scores as Markdown.

Usage:
  python3 tools/scores.py                             # all editions, output to screen
  python3 tools/scores.py --to-edition 03 --out editions/.../01_scores.md
  python3 tools/scores.py --bootstrap A B             # confidence interval of the Brier difference A−B
"""
import argparse
import csv
import random
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


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--to-edition', default=None, help='include forecasts up to and including this edition (e.g. 03)')
    ap.add_argument('--out', default=None)
    ap.add_argument('--bootstrap', nargs=2, metavar=('P1', 'P2'), default=None)
    ap.add_argument('--n-boot', type=int, default=2000)
    a = ap.parse_args()

    questions = {q['id']: q for q in read('questions.csv')}
    forecasts = read('forecasts.csv')
    res = final_resolutions(read('resolutions.csv'))
    bench = read('benchmarks.csv')

    # Scored resolutions: outcome 0/1; those awaiting verification kept separately.
    outcome, pending, void = {}, [], []
    for qid, r in res.items():
        o = r['outcome'].strip().upper()
        if o == 'VOID':
            void.append(qid)
            continue
        if r.get('verify', '').strip().upper() == 'Y' and r.get('user_approved', '').strip().upper() != 'Y':
            pending.append(qid)
            continue
        if o in ('0', '1'):
            outcome[qid] = int(o)

    rows_all = []  # (qid, edition, run, p, o, date)
    for p in forecasts:
        qid = p['question_id']
        if qid not in outcome:
            continue
        if a.to_edition and int(p['edition']) > int(a.to_edition):
            continue
        rows_all.append((qid, p['edition'], p['run'], float(p['p']), outcome[qid], p['date']))

    out = []
    pr = out.append
    pr('# Accuracy scores\n')
    pr(f'Resolved and scored questions: **{len(outcome)}** · awaiting user verification: {len(pending)} · void: {len(void)}\n')
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
