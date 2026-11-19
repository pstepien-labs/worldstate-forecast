import os
import subprocess
import tempfile
import unittest

from tests.helpers import FH, QH, RH, f, q, r, write
from tools import registry_guard as rg


class GuardTest(unittest.TestCase):
    def setUp(self):
        self.root = tempfile.mkdtemp()
        g = lambda *a: subprocess.run(['git', '-C', self.root, *a], check=True, capture_output=True)
        self.g = g
        g('init', '-q')
        g('config', 'user.email', 't@example.invalid')
        g('config', 'user.name', 't')
        self.write([q(1, '2026-10-01', status='ACTIVE')], [f(1, '01', 'A', 0.3)], [r(1, 0, '2026-10-01')])
        g('add', '-A')
        g('commit', '-qm', 'base')
        self._root = rg.ROOT
        rg.ROOT = self.root

    def tearDown(self):
        rg.ROOT = self._root

    def write(self, qs, fs, rs):
        write(os.path.join(self.root, 'registry', 'questions.csv'), QH, qs)
        write(os.path.join(self.root, 'registry', 'forecasts.csv'), FH, fs)
        write(os.path.join(self.root, 'registry', 'resolutions.csv'), RH, rs)

    def test_append_and_status_change_pass(self):
        self.write([q(1, '2026-10-01', status='RESOLVED'), q(2, '2026-11-01')],
                   [f(1, '01', 'A', 0.3), f(1, '02', 'A', 0.4)], [r(1, 0, '2026-10-01'), r(1, 0, '2026-10-01', version=2)])
        self.assertEqual(rg.check('HEAD'), [])

    def test_edited_forecast_fails(self):
        self.write([q(1, '2026-10-01', status='ACTIVE')], [f(1, '01', 'A', 0.35)], [r(1, 0, '2026-10-01')])
        problems = rg.check('HEAD')
        self.assertTrue(any('forecasts.csv: line 2 changed' in p for p in problems), problems)

    def test_removed_resolution_fails(self):
        self.write([q(1, '2026-10-01', status='ACTIVE')], [f(1, '01', 'A', 0.3)], [])
        self.assertTrue(any('resolutions.csv' in p for p in rg.check('HEAD')))

    def test_question_text_change_fails(self):
        x = q(1, '2026-10-01', status='ACTIVE')
        x['question'] = 'changed'
        self.write([x], [f(1, '01', 'A', 0.3)], [r(1, 0, '2026-10-01')])
        self.assertTrue(any("field 'question' changed" in p for p in rg.check('HEAD')))


if __name__ == '__main__':
    unittest.main()
