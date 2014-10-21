import operator
from pyparsing import ParseResults
from brabbel.parser import Parser
from brabbel.helpers import _in

ops = {
    "not": operator.not_,
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.div,
    "<": operator.lt,
    "<=": operator.le,
    ">=": operator.ge,
    ">": operator.gt,
    "==": operator.eq,
    "!=": operator.ne,
    "and": operator.and_,
    "or": operator.or_,
    "in": _in
}


def _evaluate_term(op, operand):
        if op is None:
            return operand[0]
        elif op == "not":
            return ops[op](operand[0])
        else:
            return ops[op](operand[0], operand[1])


class Expression(object):

    """Docstring for Expression. """

    def __init__(self, expression):
        """Initialise a Expression object

        :expression: String representation of an Expression

        """
        self._expression = expression
        self._expression_tree = Parser().parse(self._expression)

    def evaluate(self, values=None):
        """Returns the result auf the evaluation of the expression.

        :values: Dictionary with key value pairs containing values which
        can be used while evaluation
        :returns: Result of the evaluation

        """
        if values is None:
            values = {}
        return self._evaluate(self._expression_tree, values)

    def _resolve_variable(self, key, values):
        value = values[key.strip("$")]
        if isinstance(value, basestring):
            value = "'%s'" % value
        else:
            try:
                value = float(value)
            except:
                pass
        return value

    def _evaluate(self, tree, values):
        operand = []
        op = None
        for element in tree:
            if isinstance(element, ParseResults):
                operand.append(self._evaluate(element, values))
            elif element in ops.keys():
                op = element
            else:
                if str(element).startswith("$"):
                    element = self._resolve_variable(element, values)
                operand.append(element)

            # Preevaluate here and use the result as the first operand.
            if len(operand) == 2:
                operand = [_evaluate_term(op, operand)]
                op = None
        return _evaluate_term(op, operand)
