#!/usr/bin/env python3
"""Mechanical coherence check of the lens mean before the red team (framework 1.9, WP-12).

  python3 tools/coherence.py <NN> [--out <edition dir>/05_coherence.md]

Reads registry/relations.csv (append-only) and the A, B, C rows of edition NN in registry/forecasts.csv,
computes their mean per question (the future AGG) and lists every violated relation with its size:
  implies                    P(a) <= P(b)   (if a then b)
  same_event_later_deadline  P(a) <= P(b)   (a: earlier deadline, b: later deadline)
  higher_threshold           P(a) <= P(b)   (a: above the higher threshold, b: above the lower one)
  exclusive                  P(a) + P(b) <= 1
Stage 05 reads the output first; a violation is a "logic" adjustment (limit ±0.15 unchanged).
Python standard library only.
"""
import argparse
import csv
import os
import sys
from collections import defaultdict

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
ORDER = ('implies', 'same_event_later_deadline', 'higher_threshold')


def read(path):
    if not os.path.exists(path):
        return []
    with open(path, encoding='utf-8-sig', newline='') as f:
        return list(csv.DictReader(f, delimiter=';'))


def lens_mean(forecasts, edition):
    by = defaultdict(dict)
    for f in forecasts:
        if f['edition'].zfill(2) == edition.zfill(2) and f['run'] in ('A', 'B', 'C'):
            by[f['question_id']][f['run']] = float(f['p'])
    return {q: sum(v.values()) / 3 for q, v in by.items() if len(v) == 3}


def violations(relations, p, tol=0.005):
    out = []
    for r in relations:
        a, b, kind = r['question_a'], r['question_b'], r['relation'].strip()
        if a not in p or b not in p:
            continue
        if kind in ORDER and p[a] > p[b] + tol:
            out.append((a, kind, b, p[a], p[b], round(p[a] - p[b], 3)))
        elif kind == 'exclusive' and p[a] + p[b] > 1 + tol:
            out.append((a, kind, b, p[a], p[b], round(p[a] + p[b] - 1, 3)))
    return sorted(out, key=lambda x: -x[5])


def main(argv):
    ap = argparse.ArgumentParser(prog='tools/coherence.py', description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('edition')
    ap.add_argument('--out')
    a = ap.parse_args(argv)
    rel = read(os.path.join(ROOT, 'registry', 'relations.csv'))
    p = lens_mean(read(os.path.join(ROOT, 'registry', 'forecasts.csv')), a.edition)
    v = violations(rel, p)
    usable = sum(1 for r in rel if r['question_a'] in p and r['question_b'] in p)
    lines = [f'# Coherence check, edition {a.edition.zfill(2)} (mean of A, B, C)', '',
             f'Relations in registry/relations.csv: {len(rel)} · with both questions forecast in this edition: {usable} · '
             f'violated: {len(v)}', '',
             'A violation is a logic error by definition: the red team proposes an adjustment for it (limit ±0.15).', '',
             '| Question a | Relation | Question b | mean p(a) | mean p(b) | Size |', '|---|---|---|---|---|---|']
    lines += [f'| {x[0]} | {x[1]} | {x[2]} | {x[3]:.3f} | {x[4]:.3f} | {x[5]:.3f} |' for x in v]
    text = '\n'.join(lines) + '\n'
    if a.out:
        with open(a.out, 'w', encoding='utf-8') as f:
            f.write(text)
    print(text)
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
