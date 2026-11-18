import unittest

from tools import coherence


class CoherenceTest(unittest.TestCase):
    def test_relations(self):
        p = {'Q-1': 0.6, 'Q-2': 0.4, 'Q-3': 0.7, 'Q-4': 0.5}
        rel = [{'question_a': 'Q-1', 'relation': 'implies', 'question_b': 'Q-2'},                  # 0.6 > 0.4: violated
               {'question_a': 'Q-2', 'relation': 'same_event_later_deadline', 'question_b': 'Q-1'},  # fine
               {'question_a': 'Q-3', 'relation': 'exclusive', 'question_b': 'Q-4'},                 # 1.2 > 1: violated
               {'question_a': 'Q-2', 'relation': 'higher_threshold', 'question_b': 'Q-9'}]          # unknown: skipped
        v = coherence.violations(rel, p)
        self.assertEqual([(x[0], x[1], x[5]) for x in v], [('Q-1', 'implies', 0.2), ('Q-3', 'exclusive', 0.2)])

    def test_lens_mean_needs_three(self):
        fc = [{'question_id': 'Q-1', 'edition': '04', 'run': r, 'p': p} for r, p in (('A', '0.3'), ('B', '0.6'), ('C', '0.6'))]
        fc.append({'question_id': 'Q-2', 'edition': '04', 'run': 'A', 'p': '0.5'})
        fc.append({'question_id': 'Q-1', 'edition': '04', 'run': 'AGG', 'p': '0.9'})
        self.assertEqual(coherence.lens_mean(fc, '4'), {'Q-1': 0.5})


if __name__ == '__main__':
    unittest.main()
