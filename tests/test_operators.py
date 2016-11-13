import unittest


class TestInOperator(unittest.TestCase):

    def test_ok(self):
        from brabbel.operators import _in
        result = _in(1, [1, 2])
        self.assertEqual(result, True)

    def test_fail(self):
        from brabbel.operators import _in
        result = _in(3, [1, 2])
        self.assertEqual(result, False)
