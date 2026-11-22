#!/usr/bin/env python3
"""Append-only guard for the public track record (framework 1.9, WP-05). Python standard library only.

  python3 tools/registry_guard.py <base-ref> [<head-ref>]     head defaults to the working tree

Fails (exit 1) if, between base and head:
  - any existing line of registry/forecasts.csv, benchmarks.csv, resolutions.csv, question_meta.csv (methodology v1.1 §4.6)
    or relations.csv changed, moved or disappeared
    (new lines may only be appended at the end);
  - the header of any registry CSV changed;
  - any field of an existing row of registry/questions.csv other than `status` and `notes` changed, or a row disappeared.
CLAUDE.md rule 3.7. Runs in CI on every push and locally before publishing.
"""
import csv
import io
import os
import subprocess
import sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
APPEND_ONLY = ('forecasts.csv', 'benchmarks.csv', 'resolutions.csv', 'question_meta.csv', 'relations.csv')
MUTABLE_QUESTION_FIELDS = {'status', 'notes'}


def load(ref, name):
    rel = f'registry/{name}'
    if ref is None:
        p = os.path.join(ROOT, rel)
        if not os.path.exists(p):
            return None
        with open(p, encoding='utf-8-sig', newline='') as f:
            return f.read()
    r = subprocess.run(['git', '-C', ROOT, 'show', f'{ref}:{rel}'], capture_output=True)
    if r.returncode != 0:
        return None
    return r.stdout.decode('utf-8-sig')


def lines(text):
    return [l for l in text.replace('\r\n', '\n').split('\n') if l.strip()]


def check(base_ref, head_ref=None):
    problems = []
    for name in APPEND_ONLY:
        b, h = load(base_ref, name), load(head_ref, name)
        if b is None:
            continue
        if h is None:
            problems.append(f'{name}: file removed')
            continue
        bl, hl = lines(b), lines(h)
        for i, line in enumerate(bl):
            if i >= len(hl):
                problems.append(f'{name}: line {i + 1} removed: {line[:160]}')
                break
            if hl[i] != line:
                problems.append(f'{name}: line {i + 1} changed\n    was: {line[:160]}\n    now: {hl[i][:160]}')
                break
    b, h = load(base_ref, 'questions.csv'), load(head_ref, 'questions.csv')
    if b is not None:
        if h is None:
            problems.append('questions.csv: file removed')
        else:
            br = list(csv.DictReader(io.StringIO(b), delimiter=';'))
            hr = {r['id']: r for r in csv.DictReader(io.StringIO(h), delimiter=';')}
            if br and hr and list(br[0].keys()) != list(next(iter(hr.values())).keys()):
                problems.append('questions.csv: header changed')
            for r in br:
                n = hr.get(r['id'])
                if n is None:
                    problems.append(f"questions.csv: question {r['id']} removed")
                    continue
                for k, v in r.items():
                    if k not in MUTABLE_QUESTION_FIELDS and n.get(k) != v:
                        problems.append(f"questions.csv: {r['id']} field '{k}' changed")
    for name in ('editions.csv',) + APPEND_ONLY:
        b, h = load(base_ref, name), load(head_ref, name)
        if b and h and lines(b)[:1] != lines(h)[:1]:
            problems.append(f'{name}: header changed')
    return problems


def main(argv):
    if not argv:
        print(__doc__)
        return 2
    problems = check(argv[0], argv[1] if len(argv) > 1 else None)
    if problems:
        print('REGISTRY GUARD FAILED (CLAUDE.md rule 3.7):')
        for p in problems:
            print(' - ' + p)
        return 1
    print(f'registry guard OK: {argv[0]} -> {argv[1] if len(argv) > 1 else "working tree"} is append-only')
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
