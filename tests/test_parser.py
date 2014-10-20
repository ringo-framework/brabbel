import unittest
from brabbel.parser import Parser


class TestAtom(unittest.TestCase):

    def setUp(self):
        self.parser = Parser()

    def test_number(self):
        result = self.parser.parse("1").asList()
        self.assertEqual(result, [1.0])

    def test_string(self):
        result = self.parser.parse("'xyz'").asList()
        self.assertEqual(result, ["'xyz'"])

    def test_variable(self):
        result = self.parser.parse("$xyz").asList()
        self.assertEqual(result, ["$xyz"])

    def test_true(self):
        result = self.parser.parse("True").asList()
        self.assertEqual(result, [True])

    def test_false(self):
        result = self.parser.parse("False").asList()
        self.assertEqual(result, [False])

    def test_listing(self):
        result = self.parser.parse("[1,2,3]").asList()
        self.assertEqual(result, [[1.0,2.0,3.0]])

class TestOperator(unittest.TestCase):

    def setUp(self):
        self.parser = Parser()

    def test_not_number(self):
        result = self.parser.parse("not 123").asList()
        self.assertEqual(result, [["not", 123]])

    def test_not_string(self):
        result = self.parser.parse("not 'xyz'").asList()
        self.assertEqual(result, [["not", "'xyz'"]])

    def test_not_var(self):
        result = self.parser.parse("not $xyz").asList()
        self.assertEqual(result, [["not", "$xyz"]])

    def test_not_true(self):
        result = self.parser.parse("not True").asList()
        self.assertEqual(result, [["not", True]])

    def test_not_false(self):
        result = self.parser.parse("not False").asList()
        self.assertEqual(result, [["not", False]])

    def test_plus(self):
        result = self.parser.parse("1 + 1").asList()
        self.assertEqual(result, [[1.0, "+", 1.0]])

    def test_plusplus(self):
        result = self.parser.parse("1 + 1 + 3").asList()
        self.assertEqual(result, [[1.0, "+", 1.0, "+", 3.0]])

    def test_minus(self):
        result = self.parser.parse("1 - 1").asList()
        self.assertEqual(result, [[1.0, "-", 1.0]])

    def test_mul(self):
        result = self.parser.parse("1 * 1").asList()
        self.assertEqual(result, [[1.0, "*", 1.0]])

    def test_div(self):
        result = self.parser.parse("1 / 1").asList()
        self.assertEqual(result, [[1.0, "/", 1.0]])

    def test_plusmul(self):
        result = self.parser.parse("1 + 1 * 3").asList()
        self.assertEqual(result, [[1.0, "+", [1.0, "*", 3.0]]])

    def test_plusmulparent(self):
        result = self.parser.parse("(1 + 1) * 3").asList()
        self.assertEqual(result, [[[1.0, '+', 1.0], '*', 3.0]])

    def test_lt(self):
        result = self.parser.parse("1 < 2").asList()
        self.assertEqual(result, [[1.0, "<", 2.0]])

    def test_le(self):
        result = self.parser.parse("1 <= 2").asList()
        self.assertEqual(result, [[1.0, "<=", 2.0]])

    def test_ge(self):
        result = self.parser.parse("2 >= 1").asList()
        self.assertEqual(result, [[2.0, ">=", 1.0]])

    def test_gt(self):
        result = self.parser.parse("2 > 1").asList()
        self.assertEqual(result, [[2.0, ">", 1.0]])

    def test_eq(self):
        result = self.parser.parse("2 == 2").asList()
        self.assertEqual(result, [[2.0, "==", 2.0]])

    def test_ne(self):
        result = self.parser.parse("2 != 1").asList()
        self.assertEqual(result, [[2.0, "!=", 1.0]])

    def test_plusnediv(self):
        result = self.parser.parse("2 + 2 != 8 / 2").asList()
        self.assertEqual(result, [[[2.0, "+", 2.0], "!=", [8.0, "/", 2.0]]])

    def test_and(self):
        result = self.parser.parse("True and True").asList()
        self.assertEqual(result, [[True, "and", True]])

    def test_or(self):
        result = self.parser.parse("False or True").asList()
        self.assertEqual(result, [[False, "or", True]])

    def test_eqandgt(self):
        result = self.parser.parse("2 == 2 and 8 > 2").asList()
        self.assertEqual(result, [[[2.0, "==", 2.0], "and", [8.0, ">", 2.0]]])

    def test_eqorgt(self):
        result = self.parser.parse("2 != 2 or 8 > 2").asList()
        self.assertEqual(result, [[[2.0, "!=", 2.0], "or", [8.0, ">", 2.0]]])

    def test_notand(self):
        result = self.parser.parse("not False and True").asList()
        self.assertEqual(result, [[["not", False], "and", True]])

    def test_in(self):
        result = self.parser.parse("'foo' in ['foo','bar']").asList()
        self.assertEqual(result, [["'foo'", "in", ["'foo'","'bar'"]]])
