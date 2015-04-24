from __future__ import division

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
