import unittest
from brabbel.expression import Expression

class TestExpression(unittest.TestCase):

    def setUp(self):
        pass

    def test_number(self):
        expression = Expression("1")
        result = expression.evaluate()
        self.assertEqual(result, 1.0)

    def test_string(self):
        expression = Expression("'1'")
        result = expression.evaluate()
        self.assertEqual(result, "'1'")

    def test_variable(self):
        expression = Expression("$string")
        result = expression.evaluate({"string": "string"})
        self.assertEqual(result, "'string'")

    def test_true(self):
        expression = Expression("True")
        result = expression.evaluate()
        self.assertEqual(result, True)

    def test_false(self):
        expression = Expression("False")
        result = expression.evaluate()
        self.assertEqual(result, False)

    def test_listing(self):
        expression = Expression("[1,2,3]")
        result = expression.evaluate()
        self.assertEqual(result, [1.0,2.0,3.0])

    def test_nottrue(self):
        expression = Expression("not True")
        result = expression.evaluate()
        self.assertEqual(result, False)

    def test_notfalse(self):
        expression = Expression("not False")
        result = expression.evaluate()
        self.assertEqual(result, True)

    def test_plus(self):
        expression = Expression("1 + 1")
        result = expression.evaluate()
        self.assertEqual(result, 2.0)

    def test_plusplus(self):
        expression = Expression("1 + 1 + 1")
        result = expression.evaluate()
        self.assertEqual(result, 3.0)

    def test_sub(self):
        expression = Expression("7 - 4")
        result = expression.evaluate()
        self.assertEqual(result, 3.0)

    def test_mul(self):
        expression = Expression("7 * 7")
        result = expression.evaluate()
        self.assertEqual(result, 49.0)

    def test_div(self):
        expression = Expression("49 / 7")
        result = expression.evaluate()
        self.assertEqual(result, 7.0)

    def test_addmul(self):
        expression = Expression("4 + 3 * 7")
        result = expression.evaluate()
        self.assertEqual(result, 25.0)

    def test_addmulpar(self):
        expression = Expression("(4 + 3) * 7")
        result = expression.evaluate()
        self.assertEqual(result, 49.0)

    def test_plusnediv(self):
        expression = Expression("2 + 2 != 8 / 2")
        result = expression.evaluate()
        self.assertEqual(result, False)

    def test_eqandgt(self):
        expression = Expression("2 == 2 and 8 > 2")
        result = expression.evaluate()
        self.assertEqual(result, True)

    def test_eqorgt(self):
        expression = Expression("2 != 2 or 8 > 2")
        result = expression.evaluate()
        self.assertEqual(result, True)

    def test_notand(self):
        expression = Expression("not False and True")
        result = expression.evaluate()
        self.assertEqual(result, True)

    def test_in(self):
        expression = Expression("'foo' in ['foo','bar']")
        result = expression.evaluate()
        self.assertEqual(result, True)

    def test_notin(self):
        expression = Expression("not ('foo' in ['foo','bar'])")
        result = expression.evaluate()
        self.assertEqual(result, False)

    def test_datetoday(self):
        from datetime import date
        expression = Expression("date('today')")
        result = expression.evaluate()
        self.assertEqual(result, date.today())

    def test_datexlttoday(self):
        from datetime import date
        expression = Expression("date('20000101') < date('today')")
        result = expression.evaluate()
        self.assertEqual(result, True)

    def test_datexgttoday(self):
        from datetime import date
        expression = Expression("date('20000101') > date('today')")
        result = expression.evaluate()
        self.assertEqual(result, False)

    def test_bool(self):
        expression = Expression("bool(1)")
        result = expression.evaluate()
        self.assertEqual(result, True)

    def test_boolorTrue(self):
        expression = Expression("bool(0) or True")
        result = expression.evaluate()
        self.assertEqual(result, True)

    def test_boolandFalse(self):
        expression = Expression("bool(0) and False")
        result = expression.evaluate()
        self.assertEqual(result, False)

    def test_notboolor(self):
        expression = Expression("(not bool(0)) or False")
        result = expression.evaluate()
        self.assertEqual(result, True)

    def test_boolvar(self):
        expression = Expression("bool($float)")
        result = expression.evaluate({"float": 1})
        self.assertEqual(result, True)

class TestReallife(unittest.TestCase):
    def test_boolvar(self):
        expression = Expression("( 'antragsteller' in       ['institutionen_einsicht', 'user', 'antragsteller']   ) == False")
        result = expression.evaluate()
        self.assertEqual(result, False)
