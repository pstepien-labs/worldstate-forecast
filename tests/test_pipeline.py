import os
import subprocess
import sys
import tempfile
import unittest

from tests.helpers import f, q, r, registry
from tools import pipeline

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))


class PipelineTest(unittest.TestCase):
    def test_critical_gate(self):
        d = tempfile.mkdtemp()
        p = os.path.join(d, '08.md')
        open(p, 'w').write('# QC\n\nCritical discrepancies open: 2\n')
        self.assertTrue(pipeline.critical_open(p))
        open(p, 'w').write('Critical discrepancies open: **0**\n')
        self.assertFalse(pipeline.critical_open(p))
        self.assertFalse(pipeline.critical_open(os.path.join(d, 'missing.md')))

    def test_pending_verification_split(self):
        root = registry([q(1, '2026-10-01'), q(2, '2026-10-01'), q(3, '2026-10-01')], [],
                        [r(1, 1, '2026-10-01', verify='Y'),
                         r(2, 1, '2026-10-01', verify='Y'), dict(r(2, 1, '2026-10-01', version=2, verify='Y', approved='N'), notes='autoverify 17.11: DISPUTED'),
                         r(3, 1, '2026-10-01', verify='Y', approved='A')])
        old = pipeline.ROOT
        pipeline.ROOT = root
        try:
            self.assertEqual(pipeline.pending_verification(), {'unchecked': ['Q-0001'], 'disputed': ['Q-0002'], 'retry': []})
        finally:
            pipeline.ROOT = old

    def test_unreadable_source_is_retried_three_times(self):
        unread = lambda v: dict(r(4, 1, '2026-10-01', version=v, verify='Y', approved='N'),
                                notes='autoverify 17.11: DISPUTED, re-check says UNDETERMINED, HTTP 429 quota exceeded')
        rows = [r(4, 1, '2026-10-01', verify='Y'), unread(2)]
        root = registry([q(4, '2026-10-01')], [], rows)
        old = pipeline.ROOT
        pipeline.ROOT = root
        try:
            self.assertEqual(pipeline.pending_verification()['retry'], ['Q-0004'])
            root2 = registry([q(4, '2026-10-01')], [], rows + [unread(3), unread(4)])
            pipeline.ROOT = root2
            p = pipeline.pending_verification()
            self.assertEqual((p['retry'], p['disputed']), ([], ['Q-0004']))  # third failed attempt goes to the user
        finally:
            pipeline.ROOT = old

    def test_edition_framework(self):
        self.assertEqual(pipeline.edition_framework([{'framework_version': '1.8.0'}]), (1, 8, 0))
        self.assertGreaterEqual(pipeline.edition_framework([{'framework_version': '1.9.0'}]), (1, 9, 0))


class AppendForecastsTest(unittest.TestCase):
    def setUp(self):
        self.root = registry([q(1, '2026-12-01', status='ACTIVE')], [f(1, '01', 'A', 0.3)], [])
        os.makedirs(os.path.join(self.root, 'tools'))
        for name in ('pipeline.py',):
            with open(os.path.join(ROOT, 'tools', name)) as src, open(os.path.join(self.root, 'tools', name), 'w') as dst:
                dst.write(src.read())

    def run_append(self, rows, *extra):
        path = os.path.join(self.root, 'rows.csv')
        with open(path, 'w', encoding='utf-8') as fh:
            fh.write('\n'.join(rows) + '\n')
        return subprocess.run([sys.executable, 'tools/pipeline.py', 'append-forecasts', path, *extra],
                              cwd=self.root, capture_output=True, text=True)

    def test_valid_rows_appended(self):
        res = self.run_append(['"Q-0001";"04";"2026-11-30";"A";"0.42";"low";"r";"k"'], '--run', 'A')
        self.assertEqual(res.returncode, 0, res.stderr)
        text = open(os.path.join(self.root, 'registry', 'forecasts.csv'), encoding='utf-8-sig').read()
        self.assertTrue(text.rstrip().endswith('"Q-0001";"04";"2026-11-30";"A";"0.42";"low";"r";"k"'))

    def test_invalid_rows_refused(self):
        for row in ('"Q-0009";"04";"2026-11-30";"A";"0.42";"low";"r";"k"',   # unknown question
                    '"Q-0001";"04";"2026-11-30";"A";"1.0";"low";"r";"k"',    # p outside 0.01-0.99
                    '"Q-0001";"04";"30.11.2026";"A";"0.4";"low";"r";"k"',    # date format
                    '"Q-0001";"04";"2026-11-30";"B";"0.4";"low";"r";"k"'):   # wrong run for --run A
            res = self.run_append([row], '--run', 'A')
            self.assertNotEqual(res.returncode, 0, row)


if __name__ == '__main__':
    unittest.main()
