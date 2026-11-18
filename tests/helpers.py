"""Shared fixtures: a small registry in a temporary folder (framework 1.9, WP-04)."""
import csv
import os
import tempfile

QH = ['id', 'created', 'edition_created', 'type', 'vector', 'region', 'cluster', 'question', 'resolution_criterion',
      'resolution_source', 'deadline', 'p_status_quo', 'who_benefits', 'pir', 'key_indicator', 'status', 'notes']
FH = ['question_id', 'edition', 'date', 'run', 'p', 'analytic_confidence', 'rationale', 'key_indicator']
RH = ['question_id', 'version', 'resolution_date', 'outcome', 'evidence_url', 'evidence_publisher', 'second_source_url',
      'resolution_confidence', 'verify', 'user_approved', 'notes']


def write(path, header, rows):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w', encoding='utf-8-sig', newline='') as f:
        w = csv.writer(f, delimiter=';', quoting=csv.QUOTE_ALL)
        w.writerow(header)
        for r in rows:
            w.writerow([r.get(k, '') for k in header])


def q(i, deadline, psq='0.10', status='RESOLVED', vector='MIL', cluster=None, created='2026-09-23'):
    return {'id': f'Q-{i:04d}', 'created': created, 'edition_created': '01', 'type': 'OPEN', 'vector': vector,
            'cluster': cluster or f'C{i}', 'question': f'question {i}', 'deadline': deadline, 'p_status_quo': psq,
            'who_benefits': 'NONE', 'status': status}


def f(i, edition, run, p, date='2026-09-23'):
    return {'question_id': f'Q-{i:04d}', 'edition': edition, 'date': date, 'run': run, 'p': str(p)}


def r(i, outcome, date, version=1, verify='N', approved=''):
    return {'question_id': f'Q-{i:04d}', 'version': str(version), 'resolution_date': date, 'outcome': str(outcome),
            'verify': verify, 'user_approved': approved}


def registry(questions, forecasts, resolutions):
    root = tempfile.mkdtemp(prefix='wf-test-')
    write(os.path.join(root, 'registry', 'questions.csv'), QH, questions)
    write(os.path.join(root, 'registry', 'forecasts.csv'), FH, forecasts)
    write(os.path.join(root, 'registry', 'resolutions.csv'), RH, resolutions)
    write(os.path.join(root, 'registry', 'benchmarks.csv'), ['question_id', 'edition', 'date', 'source', 'p', 'url', 'match', 'notes'], [])
    write(os.path.join(root, 'registry', 'editions.csv'), ['edition', 'framework_version'], [])
    return root
