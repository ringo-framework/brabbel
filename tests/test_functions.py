import unittest
from datetime import date


class TestDate(unittest.TestCase):

    def test_today(self):
        from brabbel.helpers import _date
        result = _date('today')
        self.assertEqual(result, date.today())

    def test_date(self):
        from brabbel.helpers import _date
        result = _date('20000101')
        self.assertEqual(result, date(2000, 1, 1))
