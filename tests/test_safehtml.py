import unittest

from tools import safehtml


class SafeHtmlTest(unittest.TestCase):
    def test_active_content_refused(self):
        for bad in ('<p>x</p><script>alert(1)</script>', '<img src=x onerror="alert(1)">', '<a href="javascript:x()">a</a>',
                    '<iframe src="https://example.org"></iframe>', '<a href="https://polymarket.com/x">p</a>'):
            self.assertTrue(safehtml.problems(bad), bad)

    def test_clean_page_and_allow_list(self):
        page = '<p class="d">fine <b class="pv" data-q="Q-1"></b></p><a href="https://github.com/x">r</a>'
        self.assertEqual(safehtml.problems(page, allowed_hosts={'github.com'}), [])
        self.assertTrue(safehtml.problems('<a href="https://evil.example/">x</a>', allowed_hosts={'github.com'}))

    def test_own_template_script_accepted(self):
        own = '<script>copy()</script>'
        self.assertEqual(safehtml.problems('<p>x</p>' + own, allow_scripts=[own]), [])


if __name__ == '__main__':
    unittest.main()
