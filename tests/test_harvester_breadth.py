"""Framework 2.0 (methodology v1.1 §10): new concepts, emerging concepts, breadth report, GDELT events and World Bank adapters."""
import io
import json
import os
import tempfile
import unittest
import zipfile
from datetime import date, timedelta
from unittest import mock

from tools.harvester import adapters, config, digest
from tools.harvester.digest import Matcher


class NewConceptsTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.m = Matcher()

    def test_swing_states_and_structural_concepts(self):
        cases = [('India buys more Russian oil', 'india_south_asia'), ('Japanese Self-Defense Forces expand', 'japan'),
                 ('Erdogan hosts talks in Ankara', 'turkey'), ('UAE and Saudi Arabia sign a deal', 'gulf_states'),
                 ('Doctrine change raises nuclear test fears', 'arms_control'), ('Rheinmetall opens new shell plant', 'defence_industry'),
                 ('Drought hits the wheat harvest', 'climate_shocks'), ('Migrants cross the Channel', 'demography_migration'),
                 ('Wydatki na obronność rosną', 'defence_industry'), ('Россия и Индия подписали соглашение', 'india_south_asia')]
        for text, concept in cases:
            self.assertIn(concept, self.m.match(text), text)

    def test_false_positives(self):
        self.assertNotIn('turkey', self.m.match('Turkey dinner recipes for Thanksgiving'))
        self.assertNotIn('india_south_asia', self.m.match('Indiana Jones returns'))


class EmergingConceptsTest(unittest.TestCase):
    def test_only_unexpired_emerging_concepts_match(self):
        d = tempfile.mkdtemp()
        for name in ('keywords.csv',):
            with open(os.path.join(config.config_dir(), name), encoding='utf-8-sig') as src, open(os.path.join(d, name), 'w', encoding='utf-8-sig') as dst:
                dst.write(src.read())
        today = date.today()
        with open(os.path.join(d, 'keywords_emerging.csv'), 'w', encoding='utf-8-sig') as f:
            f.write('concept;label;groups;vectors;pir;actors;lang;terms;driver;added;expires;reason\n')
            f.write(f'em_bridge;Kerch bridge;G1;;;;en;kerch bridge;D1;{today};{today + timedelta(days=30)};surge\n')
            f.write(f'em_old;Old;G1;;;;en;zzyzx;D1;{today - timedelta(days=40)};{today - timedelta(days=10)};expired\n')
        with mock.patch.dict(os.environ, {'HARVEST_CONFIG': d}):
            m = Matcher()
        self.assertIn('em_bridge', m.match('Strike on the Kerch bridge'))
        self.assertNotIn('em_old', m.match('zzyzx'))

    def test_terms_skip_stopwords_and_make_bigrams(self):
        t = digest._terms('The Crimean bridge was hit again')
        self.assertIn('crimean bridge', t)
        self.assertNotIn('the', t)


class AdapterTest(unittest.TestCase):
    def _zip(self, rows):
        buf = io.BytesIO()
        with zipfile.ZipFile(buf, 'w') as z:
            z.writestr('x.export.CSV', '\n'.join('\t'.join(r) for r in rows) + '\n')
        return buf.getvalue()

    def _row(self, day, a1, a2, quad, gold, root='1'):
        c = [''] * 58
        c[1], c[7], c[17], c[25], c[29], c[30] = day, a1, a2, root, quad, gold
        return c

    def test_gdelt_events_dyads(self):
        y = (adapters.now().date() - timedelta(days=1)).strftime('%Y%m%d')
        rows = [self._row(y, 'USA', 'CHN', '1', '2.0')] * 4 + [self._row(y, 'USA', 'CHN', '4', '-8.0')] + \
               [self._row(y, 'USA', 'CHN', '1', '3.0', root='0')] + [self._row('20160101', 'USA', 'CHN', '4', '-10')] + \
               [self._row(y, 'RUS', 'UKR', '4', '-9.0')] * 2
        body = self._zip(rows)

        class R:
            status, skipped, error, not_modified, headers = 200, None, None, False, {}
        R.body = body
        f = mock.Mock(max_bytes=8_000_000)
        f.get.return_value = R
        t = {'id': 'g', 'kind': 'dataset', 'adapter': 'gdelt_events', 'params': 'countries=USA,CHN,RUS,UKR|min_events=5|catch_up_days=1'}
        res = adapters.run_task(t, f, {}, {})
        got = {o['indicator']: o['value'] for o in res.observations}
        self.assertEqual(got['gdelt:USA>CHN:q1'], 4)
        self.assertEqual(got['gdelt:USA>CHN:q4'], 1)
        self.assertEqual(got['gdelt:USA>CHN:goldstein'], 0.0)   # (4*2 - 8) / 5
        self.assertNotIn('gdelt:RUS>UKR:q4', got)              # below min_events
        self.assertEqual(f.max_bytes, 8_000_000)               # restored
        self.assertTrue(res.state['gdelt_last_day'])

    def test_worldbank(self):
        payload = json.dumps([{'page': 1}, [
            {'countryiso3code': 'POL', 'date': '2025', 'value': 4.5, 'country': {'id': 'PL'}},
            {'countryiso3code': 'CHN', 'date': '2025', 'value': None, 'country': {'id': 'CN'}}]]).encode()

        class R:
            status, skipped, error, not_modified, headers = 200, None, None, False, {}
            body = payload

            def text(self):
                return payload.decode()
        f = mock.Mock()
        f.get.return_value = R()
        t = {'id': 'wb_t', 'kind': 'dataset', 'adapter': 'worldbank', 'url': 'https://api.worldbank.org/x', 'indicator': 'milex_pct_gdp',
             'unit': '%', 'params': ''}
        with mock.patch.object(adapters, '_save_raw', return_value=True):
            res = adapters.run_task(t, f, {}, {})
        self.assertEqual([(o['indicator'], o['date'], o['value']) for o in res.observations], [('milex_pct_gdp:POL', '2025-12-31', 4.5)])


if __name__ == '__main__':
    unittest.main()


class ProbeCheckTest(unittest.TestCase):
    def test_check_probes_when_a_harvester_runs(self):
        from tools.harvester import __main__ as hm
        args = mock.Mock(only='x')
        with mock.patch.object(hm, '_running_harvester_pid', return_value=12345), \
                mock.patch.object(hm, 'cmd_probe', return_value=0) as probe:
            self.assertEqual(hm.cmd_check(args), 0)
        probe.assert_called_once_with(['x'])
