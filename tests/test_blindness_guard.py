import unittest

from tools.blindness_guard import decide

B = lambda cmd: ('Bash', {'command': cmd})
R = lambda path: ('Read', {'file_path': path})


class GuardTest(unittest.TestCase):
    def blocked(self, call, stage, arg=None):
        return decide(call[0], call[1], stage, arg) is not None

    def test_incident_of_edition_03_is_blocked(self):
        self.assertTrue(self.blocked(B('tail -2 registry/forecasts.csv'), '04', 'A'))

    def test_lens_tools_allowed_only_for_own_lens(self):
        self.assertFalse(self.blocked(B('python3 tools/pipeline.py lens-rows A'), '04', 'A'))
        self.assertTrue(self.blocked(B('python3 tools/pipeline.py lens-rows B'), '04', 'A'))
        self.assertFalse(self.blocked(B('python3 tools/pipeline.py append-forecasts editions/x/04_rows_A.csv --run A'), '04', 'A'))
        self.assertTrue(self.blocked(B('python3 tools/pipeline.py lens-rows A; cat registry/forecasts.csv'), '04', 'A'))

    def test_other_lens_files(self):
        self.assertTrue(self.blocked(R('/r/editions/e/04_forecasts_B.md'), '04', 'A'))
        self.assertFalse(self.blocked(R('/r/editions/e/04_forecasts_A.md'), '04', 'A'))
        self.assertFalse(self.blocked(R('/r/editions/e/04_forecasts_B.md'), '05'))

    def test_common_blindness(self):
        for path in ('/r/registry/benchmarks.csv', '/r/editions/e/06_aggregation.md', '/r/docs/data/forecasts.json',
                     '/r/reviews/learning/x.md', '/r/social/drafts/a.md', '/r/editions/e/07_annex_benchmarks.md'):
            self.assertTrue(self.blocked(R(path), '03'), path)
            self.assertFalse(self.blocked(R(path), '07'), path)

    def test_web_rules(self):
        self.assertTrue(self.blocked(('WebFetch', {'url': 'https://polymarket.com/event/x'}), '02', 'G1'))
        self.assertFalse(self.blocked(('WebFetch', {'url': 'https://polymarket.com/event/x'}), '06'))
        self.assertTrue(self.blocked(('WebSearch', {'query': 'Brent odds December'}), '04', 'B'))
        self.assertFalse(self.blocked(('WebSearch', {'query': 'Brent price December'}), '04', 'B'))

    def test_b2_sees_only_questions_and_base_rates(self):
        self.assertTrue(self.blocked(R('/r/editions/e/02_facts/G1.md'), '04', 'B2'))
        self.assertTrue(self.blocked(R('/r/editions/e/03_analysis.md'), '04', 'B2'))
        self.assertTrue(self.blocked(('WebSearch', {'query': 'x'}), '04', 'B2'))
        self.assertFalse(self.blocked(R('/r/registry/questions.csv'), '04', 'B2'))
        self.assertFalse(self.blocked(B('python3 tools/scores.py --base-rates editions/e/04_base_rates.csv'), '04', 'B2'))

    def test_secrets_in_every_stage(self):
        for call in (B('cat .env'), R('/r/.env'), B('gh auth token'), B('git push origin main'), B('git -C . push'),
                     B('launchctl list'), B('security find-generic-password -s x'), B('git remote set-url origin x')):
            self.assertTrue(self.blocked(call, None), call)
        self.assertFalse(self.blocked(R('/r/.env.example'), None))
        self.assertFalse(self.blocked(B('git commit -m "edition-04 stage-02"'), None))

    def test_replay_mode(self):
        import os
        os.environ['BLINDNESS_REPLAY_DIR'] = 'editions/2026-10-07_edition-02'
        os.environ['BLINDNESS_REPLAY_OUT'] = 'reviews/replay/x'
        try:
            self.assertFalse(self.blocked(R('editions/2026-10-07_edition-02/02_facts/G1.md'), 'R'))
            self.assertTrue(self.blocked(R('editions/2026-11-16_edition-03/02_facts/G1.md'), 'R'))
            self.assertTrue(self.blocked(R('registry/resolutions.csv'), 'R'))
            self.assertTrue(self.blocked(R('editions/2026-10-07_edition-02/07_report.md'), 'R'))
            self.assertFalse(self.blocked(R('reviews/replay/x/questions.csv'), 'R'))
            self.assertFalse(self.blocked(R('prompts/04_forecasts.md'), 'R'))
            self.assertFalse(self.blocked(R('editions/2026-10-07_edition-02/03_analysis.md'), 'R'))
            self.assertTrue(self.blocked(R('editions/2026-10-07_edition-02/04_forecasts_B.md'), 'R'))
            self.assertTrue(self.blocked(R('editions/2026-10-07_edition-02/01_resolutions.md'), 'R'))
            self.assertTrue(self.blocked(R('editions/2026-10-07_edition-02/log.md'), 'R'))
        finally:
            del os.environ['BLINDNESS_REPLAY_DIR'], os.environ['BLINDNESS_REPLAY_OUT']


if __name__ == '__main__':
    unittest.main()
