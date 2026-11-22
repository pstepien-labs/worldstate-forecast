import os
import subprocess
import sys
import unittest

from tests.helpers import f, q, r, registry

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
SCORES = os.path.join(ROOT, 'tools', 'scores.py')


def run(root, *args):
    out = subprocess.run([sys.executable, SCORES, *args], cwd=root, capture_output=True, text=True, check=True)
    return out.stdout


class ScoresTest(unittest.TestCase):
    def setUp(self):
        qs = [q(1, '2026-10-01'), q(2, '2026-10-01'), q(3, '2026-10-01'), q(4, '2026-10-01'), q(5, '2026-10-01'),
              q(6, '2026-10-01'), q(7, '2026-10-01', status='ACTIVE')]
        fc = []
        for i, p in ((1, 0.8), (2, 0.3), (3, 0.6), (4, 0.5), (5, 0.9), (6, 0.2)):
            for run_ in ('A', 'B', 'C', 'AGG', 'AGG_RT'):
                fc.append(f(i, '01', run_, p))
        fc.append(f(7, '01', 'AGG_RT', 0.5))
        rs = [r(1, 1, '2026-10-01'), r(2, 0, '2026-10-01'),
              r(3, 1, '2026-10-01', verify='Y'),                       # pending: excluded
              r(4, 1, '2026-10-01', verify='Y'), r(4, 1, '2026-10-01', version=2, verify='Y', approved='A'),  # auto-verified
              r(5, 'VOID', '2026-10-01'),
              r(6, 1, '2026-09-20')]                                   # resolved before the forecast date: left out
        self.root = registry(qs, fc, rs)

    def test_official_brier_and_exclusions(self):
        out = run(self.root)
        # scored: Q1 (0.8,1) 0.04; Q2 (0.3,0) 0.09; Q4 (0.5,1) 0.25 -> mean 0.12667
        self.assertIn('| AGG_RT | 3 | 0.127 |', out)
        self.assertIn('auto-verified: 1', out)
        self.assertIn('awaiting verification: 1', out)
        self.assertIn('void: 1', out)
        self.assertIn('Q-0006 (edition 01)', out)  # left out: known before the forecast

    def test_status_quo_bss(self):
        out = run(self.root)
        # SQ 0.10: (0.1-1)^2=0.81, (0.1-0)^2=0.01, 0.81 -> 0.54333; BSS = 1 - 0.12667/0.54333 = 0.767
        self.assertIn('| AGG_RT | 3 | 0.127 | 0.543 | 0.767 |', out)

    def test_highest_version_wins(self):
        out = run(self.root)
        self.assertIn('## Auto-verified', out)
        self.assertNotIn('Q-0004', out.split('## Awaiting user verification')[1].split('##')[0])

    def test_diagnostics_reproducible(self):
        a, b = run(self.root), run(self.root)
        self.assertEqual(a, b)
        self.assertIn('### Closed cohort', a)
        self.assertIn('### Paired difference against AGG_RT', a)

    def test_closed_cohort_as_of(self):
        out = run(self.root, '--as-of', '2026-09-30')
        self.assertIn('| closed cohort | 0 |', out)

    def test_base_rates(self):
        path = os.path.join(self.root, 'br.csv')
        run(self.root, '--base-rates', path, '--as-of', '2026-12-01')
        text = open(path, encoding='utf-8-sig').read()
        self.assertIn('"all"', text)
        # Q1, Q2, Q4 (A), Q6 scored and closed: 3 YES of 4 -> (3+1)/(4+2) = 0.667
        self.assertIn('"all";"";"";"";4;3;0.667', text)


class ScoresV11Test(unittest.TestCase):
    """Methodology v1.1 auxiliary measures and the --bank counts (framework 2.0)."""

    def setUp(self):
        from tests.helpers import write
        qs = [q(1, '2026-12-01', created='2026-11-30', cluster='HORMUZ'), q(2, '2026-12-01', created='2026-11-30'),
              q(3, '2026-12-01', created='2026-11-30'), q(4, '2027-06-01', created='2026-11-30', status='ACTIVE'),
              q(5, '2028-01-31', created='2026-11-30', status='ACTIVE')]
        fc = [f(1, '04', 'AGG_RT', 0.8, date='2026-11-30'), f(2, '04', 'AGG_RT', 0.4, date='2026-11-30'),
              f(3, '04', 'AGG_RT', 0.3, date='2026-11-30')]
        rs = [r(1, 1, '2026-12-01'), r(2, 0, '2026-12-01'), r(3, 1, '2026-12-01')]
        self.root = registry(qs, fc, rs)
        mh = ['id', 'rated_on', 'edition', 'driver', 'impact', 'decision', 'form', 'horizon', 'origin', 'chain_id', 'actor',
              'signpost_of', 'panel', 'tail', 'rating', 'notes']
        meta = [{'id': 'Q-0002', 'edition': '04', 'driver': 'D6', 'impact': '4', 'form': 'CONDITIONAL', 'horizon': 'Q',
                 'origin': 'CHAIN', 'actor': 'CN', 'rating': 'NEW'},
                {'id': 'Q-0003', 'edition': '04', 'driver': 'D2', 'impact': '2', 'form': 'LEVEL', 'horizon': 'Q',
                 'origin': 'LEDGER', 'rating': 'NEW'},
                {'id': 'Q-0004', 'edition': '04', 'driver': 'D2', 'impact': '5', 'form': 'SIGNPOST', 'horizon': 'Y',
                 'origin': 'LEDGER', 'signpost_of': 'Q-0005', 'rating': 'NEW', 'panel': 'v1.1-2026Q4'},
                {'id': 'Q-0005', 'edition': '04', 'driver': 'D4', 'impact': '5', 'form': 'EVENT', 'horizon': 'M',
                 'origin': 'TAIL', 'tail': 'Y', 'rating': 'NEW', 'panel': 'v1.1-2026Q4'}]
        write(os.path.join(self.root, 'registry', 'question_meta.csv'), mh, meta)
        write(os.path.join(self.root, 'world_model', 'drivers.csv'), ['code', 'clusters'], [{'code': 'D5', 'clusters': 'HORMUZ|OIL_PRICE'}])

    def test_cohorts_drivers_weighting_actor_models(self):
        out = run(self.root)
        self.assertIn('Cohort v1.0: N 1', out)       # Q-0001 has no metadata row
        self.assertIn('Cohort v1.1: N 2', out)
        self.assertIn('| D5 | 1 | 0.040 | 0 | n/a |', out)  # driver from the cluster mapping
        # weighted: Q2 (0.4-0)^2=0.16 w4; Q3 (0.3-1)^2=0.49 w2 -> (0.64+0.98)/6 = 0.270; unweighted 0.325
        self.assertIn('weighted Brier 0.270 · unweighted on the same set 0.325', out)
        self.assertIn('| CN | 1 | 0.160 |', out)

    def test_bank_counts(self):
        out = run(self.root, '--bank')
        self.assertIn('ACTIVE questions: **2**', out)
        self.assertIn('panel questions active: 2', out)
        self.assertIn('Panel tail questions: 1', out)
        self.assertIn('| D2 | 1 | 1 ⚠ |', out)
        self.assertIn('M questions with fewer than 2 signposts: Q-0005', out)


if __name__ == '__main__':
    unittest.main()
