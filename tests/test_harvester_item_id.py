"""P-0037: each change of a watched page (and each snapshot-list addition) gets its own item ID."""
import os
import tempfile
import unittest
from unittest import mock

from tools.harvester import adapters, store


class _Resp:
    def __init__(self, html):
        self.status = 200
        self.skipped = None
        self.error = None
        self.not_modified = False
        self.headers = {}
        self._html = html

    def text(self):
        return self._html


class _Fetcher:
    def __init__(self):
        self.html = ''

    def get(self, url, **kw):
        return _Resp(self.html)


def _page(*paras):
    return '<html><body>' + ''.join(f'<p>{p}</p>' for p in paras) + '</body></html>'


class ItemIdTest(unittest.TestCase):
    def test_change_fragments_give_distinct_ids(self):
        a = store.item_id('https://www.mfa.example/press#change-aaaa111111')
        b = store.item_id('https://mfa.example/press/#change-bbbb222222')
        self.assertNotEqual(a, b)

    def test_added_fragments_give_distinct_ids(self):
        a = store.item_id('https://list.example/sdn.csv#added-2026-11-01-3')
        b = store.item_id('https://list.example/sdn.csv#added-2026-11-02-3')
        self.assertNotEqual(a, b)

    def test_same_change_is_deduplicated(self):
        self.assertEqual(store.item_id('https://www.mfa.example/press#change-aaaa111111'),
                         store.item_id('https://mfa.example/press/?utm_source=x#change-aaaa111111'))

    def test_ordinary_fragment_still_deduplicates(self):
        self.assertEqual(store.item_id('https://news.example/a1#comments'),
                         store.item_id('https://www.news.example/a1?utm_medium=rss'))
        self.assertEqual(store.item_id('https://news.example/a1#comments'),
                         store.item_id('https://news.example/a1'))

    def test_fallback_without_url(self):
        self.assertEqual(store.item_id('', 'src|title|2026-11-01'), store.item_id(None, 'src|title|2026-11-01'))


class RunPageTest(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.env = mock.patch.dict(os.environ, {'HARVEST_DATA': self.tmp.name})
        self.env.start()
        self.task = {'id': 't_page', 'name': 'Test MFA page', 'url': 'https://mfa.example/press', 'kind': 'page'}
        self.fetcher = _Fetcher()
        self.seen = store.Seen()

    def tearDown(self):
        self.env.stop()
        self.tmp.cleanup()

    def sweep(self, html):
        self.fetcher.html = html
        res = adapters.run_page(self.task, self.fetcher, {}, {})
        return res, store.store_items(res.items, self.seen)

    def test_two_changes_two_items_unchanged_none(self):
        res, n = self.sweep(_page('Statement one about sanctions.'))
        self.assertEqual((len(res.items), n), (0, 0))  # baseline
        res, n = self.sweep(_page('Statement one about sanctions.', 'Statement two on tariffs.'))
        self.assertEqual((len(res.items), n), (1, 1))
        res, n = self.sweep(_page('Statement one about sanctions.', 'Statement two on tariffs.'))
        self.assertEqual((len(res.items), n), (0, 0))  # unchanged page
        res, n = self.sweep(_page('Statement one about sanctions.', 'Statement two on tariffs.',
                                  'Statement three on export controls.'))
        self.assertEqual((len(res.items), n), (1, 1))  # a second change is stored, not deduplicated away


if __name__ == '__main__':
    unittest.main()
