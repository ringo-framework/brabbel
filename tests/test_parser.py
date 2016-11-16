import unittest
from brabbel.parser import Parser
from brabbel.functions import functions
from brabbel.nodes import (
    Const, Variable,
    List, In,
    Add, Sub, Mul, Div,
    And, Or, Not,
    LT, GT, LE, GE, EQ, NE,
    Call)


class TestAtom(unittest.TestCase):

    def setUp(self):
        self.parser = Parser()

    def test_number(self):
        result = self.parser.parse("1")[0]
        want = Const(1)
        self.assertEqual(result, want)

    def test_string(self):
        result = self.parser.parse("'xyz'")[0]
        want = Const("xyz")
        self.assertEqual(result, want)

    def test_variable(self):
        result = self.parser.parse("$xyz")[0]
        want = Variable("xyz")
        self.assertEqual(result, want)

    def test_true(self):
        result = self.parser.parse("True")[0]
        want = Const(True)
        self.assertEqual(result, want)

    def test_false(self):
        result = self.parser.parse("False")[0]
        want = Const(False)
        self.assertEqual(result, want)

    def test_listing(self):
        result = self.parser.parse("[1,2,3]")[0]
        want = List([Const(1), Const(2), Const(3)])
        self.assertEqual(result, want)

class TestOperator(unittest.TestCase):

    def setUp(self):
        self.parser = Parser()

    def test_not_number(self):
        result = self.parser.parse("not 123")[0]
        want = Not(Const(123))
        self.assertEqual(result, want)

    def test_not_string(self):
        result = self.parser.parse("not 'xyz'")[0]
        want = Not(Const("xyz"))
        self.assertEqual(result, want)

    def test_not_var(self):
        result = self.parser.parse("not $xyz")[0]
        want = Not(Variable("xyz"))
        self.assertEqual(result, want)

    def test_not_true(self):
        result = self.parser.parse("not True")[0]
        want = Not(Const(True))
        self.assertEqual(result, want)

    def test_not_false(self):
        result = self.parser.parse("not False")[0]
        want = Not(Const(False))
        self.assertEqual(result, want)

    def test_plus(self):
        result = self.parser.parse("1 + 1")[0]
        want = Add(Const(1), Const(1))
        self.assertEqual(result, want)

    def test_plusplus(self):
        result = self.parser.parse("1 + 1 + 3")[0]
        want = Add(
            Add(
                Const(1),
                Const(1)),
            Const(3))
        self.assertEqual(result, want)

    def test_minus(self):
        result = self.parser.parse("1 - 1")[0]
        want = Sub(Const(1), Const(1))
        self.assertEqual(result, want)

    def test_mul(self):
        result = self.parser.parse("1 * 1")[0]
        want = Mul(Const(1), Const(1))
        self.assertEqual(result, want)

    def test_div(self):
        result = self.parser.parse("1 / 1")[0]
        want = Div(Const(1), Const(1))
        self.assertEqual(result, want)

    def test_plusmul(self):
        result = self.parser.parse("1 + 1 * 3")[0]
        want = Add(
            Const(1),
            Mul(Const(1), Const(3)))
        self.assertEqual(result, want)

    def test_plusmulparent(self):
        result = self.parser.parse("(1 + 1) * 3")[0]
        want = Mul(
            Add(Const(1), Const(1)),
            Const(3))
        self.assertEqual(result, want)

    def test_lt(self):
        result = self.parser.parse("1 < 2")[0]
        want = LT(Const(1), Const(2))
        self.assertEqual(result, want)

    def test_le(self):
        result = self.parser.parse("1 <= 2")[0]
        want = LE(Const(1), Const(2))
        self.assertEqual(result, want)

    def test_ge(self):
        result = self.parser.parse("2 >= 1")[0]
        want = GE(Const(2), Const(1))
        self.assertEqual(result, want)

    def test_gt(self):
        result = self.parser.parse("2 > 1")[0]
        want = GT(Const(2), Const(1))
        self.assertEqual(result, want)

    def test_gtstring(self):
        result = self.parser.parse("'foo and bar' lt 'baz'")[0]
        want = LT(Const('foo and bar'), Const('baz'))
        self.assertEqual(result, want)

    def test_eq(self):
        result = self.parser.parse("2 == 2")[0]
        want = EQ(Const(2), Const(2))
        self.assertEqual(result, want)

    def test_ne(self):
        result = self.parser.parse("2 != 1")[0]
        want = NE(Const(2), Const(1))
        self.assertEqual(result, want)

    def test_plusnediv(self):
        result = self.parser.parse("2 + 2 != 8 / 2")[0]
        want = NE(
            Add(Const(2), Const(2)),
            Div(Const(8), Const(2)))
        self.assertEqual(result, want)

    def test_and(self):
        result = self.parser.parse("True and True")[0]
        want = And(Const(True), Const(True))
        self.assertEqual(result, want)

    def test_or(self):
        result = self.parser.parse("False or True")[0]
        want = Or(Const(False), Const(True))
        self.assertEqual(result, want)

    def test_eqandgt(self):
        result = self.parser.parse("2 == 2 and 8 > 2")[0]
        want = And(
            EQ(Const(2), Const(2)),
            GT(Const(8), Const(2)))
        self.assertEqual(result, want)

    def test_eqorgt(self):
        result = self.parser.parse("2 != 2 or 8 > 2")[0]
        want = Or(
            NE(Const(2), Const(2)),
            GT(Const(8), Const(2)))
        self.assertEqual(result, want)

    def test_notand(self):
        result = self.parser.parse("not False and True")[0]
        want = And(
            Not(Const(False)),
            Const(True))
        self.assertEqual(result, want)

    def test_in(self):
        result = self.parser.parse("'foo' in ['foo','bar']")[0]
        want = In(
            Const('foo'),
            List([Const('foo'), Const('bar')]))
        self.assertEqual(result, want)

    def test_date_date(self):
        result = self.parser.parse("date('20000101')")[0]
        want = Call(functions['date'], Const('20000101'))
        self.assertEqual(result, want)

    def test_date_today(self):
        result = self.parser.parse("date('today')")[0]
        want = Call(functions['date'], Const('today'))
        self.assertEqual(result, want)

    def test_varlttoday(self):
        result = self.parser.parse("$xxx < date('today')")[0]
        want = LT(
            Variable("xxx"),
            Call(functions['date'], Const('today')))
        self.assertEqual(result, want)

    def test_bool(self):
        result = self.parser.parse("bool(1)")[0]
        want = Call(functions['bool'], Const(1))
        self.assertEqual(result, want)
