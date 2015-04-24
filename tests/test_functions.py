import unittest
from datetime import date, timedelta


class TestDate(unittest.TestCase):

    def test_today(self):
        from brabbel.functions import _date
        result = _date('today')
        self.assertEqual(result, date.today())

    def test_date(self):
        from brabbel.functions import _date
        result = _date('20000101')
        self.assertEqual(result, date(2000, 1, 1))


class TestTime(unittest.TestCase):

    def test_simple(self):
        from brabbel.functions import _timedelta
        result = _timedelta('13:37:42')
        self.assertEqual(result, timedelta(hours=13, minutes=37, seconds=42))

    def test_over(self):
        from brabbel.functions import _timedelta
        result = _timedelta('127:01:00')
        self.assertEqual(result, timedelta(hours=127, minutes=01, seconds=00))
