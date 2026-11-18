import math
import random
import unittest
from datetime import date, timedelta

from tools import quant


def phi(x):
    return 0.5 * (1 + math.erf(x / math.sqrt(2)))


class QuantTest(unittest.TestCase):
    def setUp(self):
        rnd = random.Random(7)
        self.deltas = [rnd.gauss(0, 1) for _ in range(3000)]

    def test_symmetric_walk_ends_above_start_half_the_time(self):
        p = quant.simulate(0.0, self.deltas, False, 60, 1, 'last_above', 0.0, seed=1)
        self.assertAlmostEqual(p, 0.5, delta=0.03)

    def test_touch_probability_matches_reflection(self):
        n, k = 100, 1.0
        level = k * math.sqrt(n)
        p = quant.simulate(0.0, self.deltas, False, n, 1, 'any_above', level, seed=2)
        expected = 2 * (1 - phi(k + 0.5826 / math.sqrt(n)))  # reflection with the discrete-step correction
        self.assertAlmostEqual(p, expected, delta=0.03)

    def test_condition_already_met_and_closed_window(self):
        start = date(2026, 1, 1)
        series = [(start + timedelta(days=i), 100 + (i % 7)) for i in range(400)]
        sb = {'X': series}
        m = {'question_id': 'Q-1', 'indicator': 'X', 'history_indicator': '', 'condition': 'any_above', 'threshold': '105',
             'window_start': '2026-12-01', 'window_end': '2027-03-01'}
        p, why = quant.forecast_one(m, sb, date(2027, 1, 20))
        self.assertEqual(p, 0.99)
        m2 = dict(m, condition='last_above', threshold='200', window_start='2026-06-01', window_end='2026-06-01')
        self.assertEqual(quant.forecast_one(m2, sb, date(2026, 12, 1))[0], 0.01)

    def test_too_short_history_is_skipped(self):
        sb = {'X': [(date(2026, 1, 1) + timedelta(days=i), 1.0 + i / 100) for i in range(30)]}
        m = {'question_id': 'Q-1', 'indicator': 'X', 'history_indicator': '', 'condition': 'last_above', 'threshold': '2',
             'window_start': '2026-03-01', 'window_end': '2026-03-01'}
        p, why = quant.forecast_one(m, sb, date(2026, 1, 30))
        self.assertIsNone(p)
        self.assertIn('need', why)

    def test_bad_dates_ignored(self):
        import json, os, tempfile
        path = os.path.join(tempfile.mkdtemp(), 'o.jsonl')
        with open(path, 'w') as f:
            f.write(json.dumps({'indicator': 'X', 'date': '    <link ', 'value': 1}) + '\n')
            f.write(json.dumps({'indicator': 'X', 'date': '2026-01-02', 'value': 2}) + '\n')
        self.assertEqual(quant.load_series(path)['X'], [(date(2026, 1, 2), 2.0)])


if __name__ == '__main__':
    unittest.main()
