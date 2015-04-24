from __future__ import division
import operator

class Operator(object):
    """Baseclass for all operators"""

    def eval(self):
        raise NotImplementedError()

class Binary(Operator):
    """Baseclass for Binary operators"""

class Unary(Operator):
    """Baseclass for Unary operators"""

class Div(Binary):

    def eval(self, a, b):
        if isinstance(b, int):
            return int(a / b)
        else:
            return a / b

class In(Binary):

    def eval(self, a, b):
        return a in b

operators = {
    "not": operator.not_,
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": Div().eval,
    "<": operator.lt,
    "<=": operator.le,
    ">=": operator.ge,
    ">": operator.gt,
    "==": operator.eq,
    "!=": operator.ne,
    "and": operator.and_,
    "or": operator.or_,
    "in": In().eval
}
