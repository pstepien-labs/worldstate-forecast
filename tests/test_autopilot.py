import os
import unittest
from datetime import datetime, timezone

from tools import autopilot as ap

CONF = dict(ap.DEFAULTS)
CLOSED = {'edition': '03', 'edition_closed': True, 'brief_done': True, 'site_done': True, 'state_date': '2026-11-16',
          'earliest_state_date': '2026-11-30', 'can_start_next_edition': False, 'next_edition': '04',
          'harvester': 'Harvester: RUNNING · failing 1 · items 1'}
DONE = {'learn_done_for': '03', 'improve_done_for': '03', 'interim_done_for': '03', 'qprep_done': True}


def st(**kw):
    s = dict(CLOSED)
    s.update(kw)
    return s


class DecideTest(unittest.TestCase):
    def d(self, status, now, state=None, root='/nonexistent'):
        return ap.decide(status, dict(DONE, **(state or {})), CONF, now, root=root)[0]

    def test_start_on_due_date_from_start_hour(self):
        due = st(can_start_next_edition=True)
        self.assertEqual(self.d(due, datetime(2026, 11, 30, 19, 0)), 'none')         # Mon 30.11 19:00
        self.assertEqual(self.d(due, datetime(2026, 11, 30, 20, 0)), 'edition')      # Mon 30.11 20:00
        self.assertNotEqual(self.d(st(), datetime(2026, 11, 29, 21, 0)), 'edition')   # Sun 29.11: not due yet
        self.assertEqual(self.d(due, datetime(2026, 12, 1, 8, 0)), 'none')            # Tue 08:00: before the hour
        self.assertEqual(self.d(due, datetime(2026, 12, 1, 20, 0)), 'edition')        # Tue 20:00

    def test_open_edition_resumes_at_any_hour(self):
        s = st(edition_closed=False, next={'stage': '04', 'arg': 'A'}, directory='x')
        self.assertEqual(self.d(s, datetime(2026, 11, 18, 3, 0)), 'edition')

    def test_finish_brief_and_site(self):
        self.assertEqual(self.d(st(site_done=False), datetime(2026, 11, 18, 3, 0)), 'edition')

    def test_publish_gate(self):
        self.assertEqual(self.d(st(publish_blocked=True, brief_done=False), datetime(2026, 11, 18, 21, 0)), 'none')

    def test_backoff(self):
        now = datetime(2026, 11, 18, 12, 0)
        s = st(edition_closed=False, next={'stage': '01'})
        for fails, hours_ago, expected in ((1, 0.5, 'none'), (1, 1.0, 'edition'), (2, 1.5, 'none'), (2, 2.0, 'edition'),
                                           (3, 3.0, 'none'), (3, 4.0, 'edition'), (6, 23.0, 'none'), (6, 24.0, 'edition')):
            last = (now.timestamp() - hours_ago * 3600)
            state = {'consecutive_failures': fails, 'last_run_end': datetime.fromtimestamp(last).isoformat()}
            self.assertEqual(self.d(s, now, state), expected, (fails, hours_ago))

    def test_usage_limit_wait_is_not_a_failure(self):
        s = st(edition_closed=False, next={'stage': '01'})
        self.assertEqual(self.d(s, datetime(2026, 11, 18, 10, 0), {'wait_until': '2026-11-18T11:05'}), 'none')
        self.assertEqual(self.d(s, datetime(2026, 11, 18, 11, 6), {'wait_until': '2026-11-18T11:05'}), 'edition')

    def test_model_mismatch_refused(self):
        import tempfile, json
        root = tempfile.mkdtemp()
        os.makedirs(os.path.join(root, 'ed'))
        with open(os.path.join(root, 'ed', 'provenance.jsonl'), 'w') as f:
            f.write(json.dumps({'event': 'start', 'stage': '00', 'model': 'claude-older-1'}) + '\n')
        s = st(edition_closed=False, next={'stage': '01'}, directory='ed')
        self.assertEqual(self.d(s, datetime(2026, 11, 18, 21, 0), root=root), 'none')
        with open(os.path.join(root, 'ed', 'provenance.jsonl'), 'w') as f:
            f.write(json.dumps({'event': 'start', 'stage': '00', 'model': CONF['AUTOPILOT_MODEL']}) + '\n')
        self.assertEqual(self.d(s, datetime(2026, 11, 18, 21, 0), root=root), 'edition')

    def test_learn_interim_repair_qprep_order(self):
        now = datetime(2026, 11, 23, 21, 0)  # Monday, 7 days after the state date
        self.assertEqual(ap.decide(st(), {}, CONF, now)[0], 'learn')
        self.assertEqual(ap.decide(st(), {'learn_done_for': '03'}, CONF, now)[0], 'improve')
        self.assertEqual(ap.decide(st(), {'learn_done_for': '03', 'improve_done_for': '03'}, CONF, now)[0], 'interim')
        # never close to the next edition: 29.11 is 1 day before the due date 30.11
        late = datetime(2026, 11, 29, 21, 0)
        self.assertNotEqual(ap.decide(st(), {'learn_done_for': '03', 'interim_done_for': '03'}, CONF, late)[0], 'improve')
        sun = datetime(2026, 11, 22, 21, 0)
        state = {'learn_done_for': '03', 'improve_done_for': '03', 'interim_done_for': '03'}
        self.assertEqual(ap.decide(st(harvester='failing 5'), state, CONF, sun)[0], 'repair')
        self.assertEqual(ap.decide(st(), state, CONF, sun)[0], 'skip-repair')
        state['repair_week'] = sun.strftime('%G-W%V')
        self.assertEqual(ap.decide(st(), state, CONF, sun)[0], 'none')
        self.assertEqual(ap.decide(st(), dict(state, qprep_done=False), CONF, datetime(2026, 12, 19, 21, 0))[0], 'qprep')


class ClassifyTest(unittest.TestCase):
    NOW = datetime(2026, 11, 18, 8, 9)

    def test_complete_and_blocked(self):
        self.assertEqual(ap.classify('x\nAUTOPILOT: complete edition-03', self.NOW), ('ok', None))
        self.assertEqual(ap.classify('AUTOPILOT: blocked 03 why', self.NOW), ('blocked', None))
        self.assertEqual(ap.classify('Traceback', self.NOW), ('failed', None))

    def test_limit_reset_times(self):
        for text, exp in (("You've hit your 5-hour limit · resets 11am (Europe/Warsaw)", '2026-11-18T11:05'),
                          ("You've hit your 5-hour limit · resets 12:40am (Europe/Warsaw)", '2026-11-19T00:45'),
                          ("You've hit your 5-hour limit · resets 7:50pm (Europe/Warsaw)", '2026-11-18T19:55'),
                          ("You've hit your 5-hour limit · resets 4:20am (Europe/Warsaw)", '2026-11-19T04:25')):
            self.assertEqual(ap.classify(text, self.NOW), ('limit', exp), text)


class HeartbeatTest(unittest.TestCase):
    def test_unchanged_is_not_rewritten(self):
        now = datetime(2026, 11, 18, 10, 0, tzinfo=timezone.utc)
        hb = ap.heartbeat(st(), {}, '', {}, now)
        self.assertIsNotNone(hb)
        self.assertIsNone(ap.heartbeat(st(), {}, '', hb, now))
        later = datetime(2026, 11, 21, 11, 0, tzinfo=timezone.utc)
        self.assertIsNotNone(ap.heartbeat(st(), {}, '', hb, later))   # older than 72 h
        self.assertIsNotNone(ap.heartbeat(st(edition='04'), {}, '', hb, now))

    def test_counts_inbox(self):
        inbox = '## Blockers\n- a\n- b\n\n## Waiting for the user\n- c\n'
        hb = ap.heartbeat(st(), {}, inbox, {}, datetime(2026, 11, 18, tzinfo=timezone.utc))
        self.assertEqual((hb['open_blockers'], hb['waiting_for_user']), (2, 1))


class ConfTest(unittest.TestCase):
    def test_env_wins(self):
        import tempfile
        p = os.path.join(tempfile.mkdtemp(), 'c.conf')
        open(p, 'w').write('AUTOPILOT_MODEL=m1 # comment\nBACKUP_DIR=\n')
        self.assertEqual(ap.load_conf(p, env={})['AUTOPILOT_MODEL'], 'm1')
        self.assertEqual(ap.load_conf(p, env={'AUTOPILOT_MODEL': 'm2'})['AUTOPILOT_MODEL'], 'm2')


if __name__ == '__main__':
    unittest.main()


class GateTest(unittest.TestCase):
    def test_classify_paths(self):
        c = ap.classify_paths
        self.assertEqual(c(['sources/harvest/feeds.csv', 'methodology/methodology_changes.md', 'reviews/learning/proposals.csv', 'VERSION']), 'ok')
        self.assertEqual(c(['prompts/02_collection.md', 'tools/harvester/adapters.py']), 'ok')
        self.assertEqual(c(['prompts/04_forecasts.md', 'VERSION']), 'replay')
        self.assertEqual(c(['prompts/05_red_team.md']), 'not-auto')
        self.assertEqual(c(['tools/scores.py']), 'not-auto')
        self.assertEqual(c(['methodology/methodology_v1.0.md']), 'protected')
        self.assertEqual(c(['methodology/methodology_v1.1.md']), 'protected')
        self.assertEqual(c(['world_model/drivers.csv']), 'protected')
        self.assertEqual(c(['prompts/W_world_model.md']), 'not-auto')
        self.assertEqual(c(['world_model/ledger.csv']), 'ok')
        for p in ('CLAUDE.md', 'registry/forecasts.csv', 'tools/blindness_guard.py', 'scripts/autopilot.sh', '.claude/settings.json',
                  '.github/workflows/ci.yml', 'editions/2026-11-16_edition-03/07_report.md', 'docs/index.html', 'autopilot.conf'):
            self.assertEqual(c([p, 'sources/harvest/feeds.csv']), 'protected', p)

    def test_replay_gate_ratchet(self):
        self.assertTrue(ap.replay_gate(0.180, 0.171, 0.011))
        self.assertFalse(ap.replay_gate(0.183, 0.171, 0.011))
