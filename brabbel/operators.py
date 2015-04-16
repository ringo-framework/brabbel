from __future__ import division

class Operator(object):
    """Baseclass for all operators"""

    def eval(self):
        return False

class Binary(Operator):
    """Baseclass for Binary operators"""

    def __init__(self):
        """"""
        Operator.__init__(self)

    def eval(self, a, b):
        return False

class Unary(Operator):
    """Baseclass for Unary operators"""

    def __init__(self): 
        """"""
        Operator.__init__(self)

    def eval(self, a):
        return False

class Div(Binary):

    """Docstring for Div. """

    def __init__(self):
        """TODO: to be defined1. """
        Binary.__init__(self)

    def eval(self, a, b):
        if isinstance(b, int):
            return int(a / b)
        else:
            return a / b
