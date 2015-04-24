from builtins import object
import sys
import logging
import operator
from pyparsing import ParseResults
from brabbel.parser import Parser
from brabbel.helpers import _in, _date, _timedelta, _bool, _len, _div

logging.basicConfig()
log = logging.getLogger(__name__)

functions = {
    "date": _date,
    "timedelta": _timedelta,
    "bool": _bool,
    "len": _len
}
ops = {
    "not": operator.not_,
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": _div,
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
        elif (sys.version_info > (3, 0)):
            # Only evalutate the term if both operators of the operand are
            # of the same type.
            if type(operand[0]) == type(operand[1]):
                return ops[op](operand[0], operand[1])
            else:
                return False
        else:
            # Please note that under Python2 comarison between non equal
            # type are possible but not well defined!
            return ops[op](operand[0], operand[1])

def _resolve_variable(key, values):
    try:
        value = values[key.strip("$")]
    except KeyError:
        log.warning("Variable %s could not found in the values."
                    % key.strip("$"))
        value = None
    return value



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

    def _evaluate(self, tree, values):
        operand = []
        op = None
        func = None
        try:
            for element in tree:
                if func:
                    param = element[0]
                    if isinstance(param, str) and param.startswith("$"):
                        param = _resolve_variable(param, values)
                    result = func(param)
                    operand.append(result)
                    func = None
                elif isinstance(element, ParseResults):
                    operand.append(self._evaluate(element, values))
                elif element in list(ops.keys()):
                    op = element
                    # Short curcuiting "and" and "or" opertator
                    if op == "and" and not bool(operand[0]):
                        return False
                    if op == "or" and bool(operand[0]):
                        return True
                elif element in list(functions.keys()):
                    func = functions[element]
                else:
                    if isinstance(element, str) and element.startswith("$"):
                        element = _resolve_variable(element, values)
                    operand.append(element)

                # Preevaluate here and use the result as the first operand.
                if len(operand) == 2:
                    operand = [_evaluate_term(op, operand)]
                    op = None
            return _evaluate_term(op, operand)
        except:
            log.exception("Can not evaluation expression '%s'"
                          % self._expression)
            raise
