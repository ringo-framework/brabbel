import unittest


class TestInOperator(unittest.TestCase):

    def test_ok(self):
        from brabbel.operators import In
        result = In().eval(1, [1, 2])
        self.assertEqual(result, True)

    def test_fail(self):
        from brabbel.operators import In
        result = In().eval(3, [1, 2])
        self.assertEqual(result, False)
