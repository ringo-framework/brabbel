from builtins import object
import logging
from pyparsing import ParseResults
from brabbel.parser import Parser
from brabbel.functions import functions

logging.basicConfig()
log = logging.getLogger(__name__)

from threading import Lock

class Expression(object):

    lock = Lock()
    cache = {}

    """Docstring for Expression. """
    def __init__(self, expression):
        """Initialise a Expression object

        :expression: String representation of an Expression

        """
        with Expression.lock:
            try:
                tree = Expression.cache[expression]
            except KeyError:
                tree = Parser().parse(expression)[0]
                Expression.cache[expression] = tree

        self._expression = expression
        self._expression_tree = tree

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
        try:
            return tree.evaluate(values)
        except:
            log.exception("Can not evaluate expression '%s'"
                          % self._expression)
            raise
