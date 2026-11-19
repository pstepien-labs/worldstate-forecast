#!/usr/bin/env python3
"""Computed forecasts for numeric threshold questions: shadow run QNT (framework 1.9, WP-10).

  python3 tools/quant.py forecast --edition 04 --cutoff 2026-11-30 [--append]
        one QNT row per mapped ACTIVE question, from harvested data up to the cutoff
        (--append writes them to registry/forecasts.csv; stage 06 does this before the freeze commit)
  python3 tools/quant.py backtest [--out reviews/quant_backtest.md]
        QNT for every resolved mapped question, from data up to each edition's forecast date, scored
        against the lens runs of the same edition

Method: block bootstrap of historical daily changes, centred to zero mean so no past trend is projected
(blocks of 5, last 2 years, 10,000 paths, fixed seed per question). Log changes for positive series, plain differences otherwise. The probability is the share of
paths meeting the condition, clipped to 0.01-0.99. QNT never enters AGG or AGG_RT (methodology v1.0 frozen).

registry/quant_map.csv (append-only; a newer row for the same question replaces an older one):
  question_id; indicator; history_indicator; condition; threshold; window_start; window_end; notes
  condition: last_above | last_below    value on the last observation on or before window_end
             any_above | any_below      any observation in [window_start, window_end]
  history_indicator (optional): a longer series of the same quantity used only for the daily changes
Python standard library only.
"""
import argparse
import csv
import hashlib
import json
import math
import os
import random
import statistics
import sys
from collections import defaultdict
from datetime import date, timedelta

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
OBS = os.path.join(os.environ.get('HARVEST_DATA', os.path.join(ROOT, 'data', 'harvest')), 'datasets', 'observations.jsonl')
MAP = os.path.join(ROOT, 'registry', 'quant_map.csv')
FORECASTS = os.path.join(ROOT, 'registry', 'forecasts.csv')
N_PATHS = 10000
BLOCK = 5
HISTORY_DAYS = 730
MIN_CHANGES = 120


def read_csv(path):
    if not os.path.exists(path):
        return []
    with open(path, encoding='utf-8-sig', newline='') as f:
        return list(csv.DictReader(f, delimiter=';'))


def load_series(path=OBS):
    """indicator -> sorted list of (date, value); the latest fetch wins for a duplicate date; bad dates skipped."""
    by = defaultdict(dict)
    if not os.path.exists(path):
        return {}
    with open(path, encoding='utf-8') as f:
        for line in f:
            try:
                r = json.loads(line)
                dd = date.fromisoformat(str(r['date'])[:10])
                v = float(r['value'])
            except (ValueError, KeyError, TypeError):
                continue
            by[r.get('indicator', '')][dd] = v
    return {k: sorted(v.items()) for k, v in by.items()}


def load_map(path=MAP):
    m = {}
    for r in read_csv(path):
        m[r['question_id']] = r  # later rows win
    return m


def changes(series, cutoff, history_days=HISTORY_DAYS):
    pts = [(d, v) for d, v in series if cutoff - timedelta(days=history_days) <= d <= cutoff]
    if len(pts) < 2:
        return [], False
    positive = all(v > 0 for _, v in pts)
    out = [(math.log(b / a) if positive else b - a) for (_, a), (_, b) in zip(pts, pts[1:])]
    return out, positive


def steps_between(series, start, end):
    """Number of observations expected between two dates, from the series' own frequency."""
    if end <= start:
        return 0
    ds = [d for d, _ in series[-300:]]
    gaps = [(b - a).days for a, b in zip(ds, ds[1:]) if (b - a).days > 0]
    per_obs = statistics.median(gaps) if gaps else 1
    # weekday series: 5 observations per 7 days
    if per_obs <= 1 and len(ds) > 20 and all(d.weekday() < 5 for d in ds[-20:]):
        return int(round((end - start).days * 5 / 7))
    return int(round((end - start).days / max(per_obs, 1)))


def simulate(level, deltas, positive, n_steps, window_offset, condition, threshold, seed):
    """Share of bootstrap paths meeting the condition. window_offset: first step inside the window."""
    rnd = random.Random(seed)
    mu = sum(deltas) / len(deltas)
    deltas = [x - mu for x in deltas]  # no drift: past trend is not projected forward (martingale assumption)
    nb = max(1, len(deltas) - BLOCK + 1)
    hits = 0
    for _ in range(N_PATHS):
        x = level
        hit = False
        step = 0
        while step < n_steps:
            i = rnd.randrange(nb)
            for dlt in deltas[i:i + BLOCK]:
                if step >= n_steps:
                    break
                x = x * math.exp(dlt) if positive else x + dlt
                step += 1
                if step >= window_offset:
                    if condition == 'any_above' and x > threshold:
                        hit = True
                    elif condition == 'any_below' and x < threshold:
                        hit = True
            if hit:
                break
        if condition == 'last_above':
            hit = x > threshold
        elif condition == 'last_below':
            hit = x < threshold
        hits += hit
    return hits / N_PATHS


def forecast_one(m, series_by, cutoff):
    """Return (p, rationale) or (None, reason)."""
    ind = m['indicator']
    s = [(d, v) for d, v in series_by.get(ind, []) if d <= cutoff]
    if not s:
        return None, f'no observations of {ind} up to {cutoff}'
    hist = series_by.get(m.get('history_indicator') or ind, s)
    deltas, positive = changes(hist, cutoff)
    if len(deltas) < MIN_CHANGES:
        return None, f'only {len(deltas)} daily changes of {m.get("history_indicator") or ind} (need {MIN_CHANGES})'
    cond, thr = m['condition'], float(m['threshold'])
    ws, we = date.fromisoformat(m['window_start']), date.fromisoformat(m['window_end'])
    last_d, last_v = s[-1]
    if cond in ('any_above', 'any_below'):
        seen = [v for d, v in s if ws <= d <= cutoff]
        if any((v > thr) if cond == 'any_above' else (v < thr) for v in seen):
            return 0.99, f'condition already met in the window by {cutoff} ({ind})'
    if last_d >= we:
        v = [v for d, v in s if d <= we][-1]
        hit = (v > thr) if cond.endswith('above') else (v < thr)
        return (0.99 if hit else 0.01), f'window closed: last value {v} on or before {we}'
    n = steps_between(s, last_d, we)
    off = max(1, steps_between(s, last_d, ws)) if ws > last_d else 1
    seed = int(hashlib.sha256((m['question_id'] + str(cutoff)).encode()).hexdigest()[:8], 16)
    p = simulate(last_v, deltas, positive, max(n, 1), off, cond, thr, seed)
    p = min(0.99, max(0.01, round(p, 3)))
    why = (f'centred block bootstrap ({BLOCK}-day blocks, {N_PATHS} paths) of {len(deltas)} daily changes of '
           f'{m.get("history_indicator") or ind} to {cutoff}; last {ind} {last_v} on {last_d}; {cond} {thr} '
           f'over {n} steps to {we}')
    return p, why


def cmd_forecast(a):
    cutoff = date.fromisoformat(a.cutoff)
    qs = {q['id']: q for q in read_csv(os.path.join(ROOT, 'registry', 'questions.csv'))}
    series_by = load_series()
    rows, skipped = [], []
    for qid, m in sorted(load_map().items()):
        if qs.get(qid, {}).get('status') != 'ACTIVE':
            continue
        p, why = forecast_one(m, series_by, cutoff)
        if p is None:
            skipped.append(f'{qid}: {why}')
            continue
        rows.append({'question_id': qid, 'edition': a.edition, 'date': cutoff.isoformat(), 'run': 'QNT',
                     'p': f'{p:.2f}',
                     'analytic_confidence': 'medium', 'rationale': why, 'key_indicator': m['indicator']})
    for r in rows:
        print(f"{r['question_id']} QNT {r['p']}  {r['rationale']}")
    for s_ in skipped:
        print('skipped ' + s_)
    if a.append and rows:
        with open(FORECASTS, encoding='utf-8-sig', newline='') as f:
            header = next(csv.reader(f, delimiter=';'))
        with open(FORECASTS, 'a', encoding='utf-8', newline='') as f:
            w = csv.writer(f, delimiter=';', quoting=csv.QUOTE_ALL, lineterminator='\n')
            for r in rows:
                w.writerow([r.get(k, '') for k in header])
        print(f'appended {len(rows)} QNT rows to registry/forecasts.csv')
    return 0


def cmd_backtest(a):
    qs = {q['id']: q for q in read_csv(os.path.join(ROOT, 'registry', 'questions.csv'))}
    res = {}
    for r in read_csv(os.path.join(ROOT, 'registry', 'resolutions.csv')):
        if r['question_id'] not in res or int(r['version']) > int(res[r['question_id']]['version']):
            res[r['question_id']] = r
    fc = read_csv(FORECASTS)
    series_by = load_series()
    lines = ['# QNT back-test (framework 1.9, WP-10)', '',
             'QNT computed for resolved mapped questions from harvested data up to the date of each edition\'s '
             'forecasts, scored against that edition\'s runs. Legitimate as a back-test because the method uses '
             'no model knowledge, only the data before the forecast date. Small N: indicative only.', '',
             '| Question | Edition | Outcome | QNT | A | B | C | AGG_RT | note |', '|---|---|---|---|---|---|---|---|---|']
    sq = defaultdict(list)
    for qid, m in sorted(load_map().items()):
        r = res.get(qid)
        if not r or r['outcome'] not in ('0', '1') or (r.get('verify') == 'Y' and r.get('user_approved') not in ('Y', 'A')):
            continue
        o = int(r['outcome'])
        for ed in sorted({f['edition'] for f in fc if f['question_id'] == qid}):
            runs = {f['run']: float(f['p']) for f in fc if f['question_id'] == qid and f['edition'] == ed}
            fdate = max(date.fromisoformat(f['date']) for f in fc if f['question_id'] == qid and f['edition'] == ed)
            if fdate >= date.fromisoformat(r['resolution_date']):
                continue
            p, why = forecast_one(m, series_by, fdate)
            note = '' if p is not None else why
            for k in ('QNT', 'A', 'B', 'C', 'AGG_RT'):
                v = p if k == 'QNT' else runs.get(k)
                if v is not None and p is not None:
                    sq[k].append((v - o) ** 2)
            fmtp = lambda v: 'n/a' if v is None else f'{v:.2f}'
            lines.append(f'| {qid} | {ed} | {o} | {fmtp(p)} | {fmtp(runs.get("A"))} | {fmtp(runs.get("B"))} | '
                         f'{fmtp(runs.get("C"))} | {fmtp(runs.get("AGG_RT"))} | {note} |')
    lines += ['', '| Run | N | Brier (same questions) |', '|---|---|---|']
    for k in ('QNT', 'A', 'B', 'C', 'AGG_RT'):
        v = sq.get(k, [])
        lines.append(f'| {k} | {len(v)} | {sum(v) / len(v):.3f} |' if v else f'| {k} | 0 | n/a |')
    text = '\n'.join(lines) + '\n'
    if a.out:
        with open(a.out, 'w', encoding='utf-8') as f:
            f.write(text)
    print(text)
    return 0


def main(argv):
    ap = argparse.ArgumentParser(prog='tools/quant.py', description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest='cmd', required=True)
    f = sub.add_parser('forecast')
    f.add_argument('--edition', required=True)
    f.add_argument('--cutoff', required=True, help='INFO_CUTOFF date (YYYY-MM-DD)')
    f.add_argument('--append', action='store_true')
    f.set_defaults(fn=cmd_forecast)
    b = sub.add_parser('backtest')
    b.add_argument('--out')
    b.set_defaults(fn=cmd_backtest)
    a = ap.parse_args(argv)
    return a.fn(a)


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
