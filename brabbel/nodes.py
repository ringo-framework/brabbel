import logging

log = logging.getLogger(__name__)

class Node(object):
    """Baseclass for all parsed terms"""

    def evaluate(self, ctx):
        raise NotImplementedError()


class Binary(Node):
    """Binary terms"""

    def __init__(self, op, a, b):
        self.op = op
        self.a = a
        self.b = b

    def evaluate(self, ctx):
        return self.op(self.a.evaluate(ctx), self.b.evaluate(ctx))


class Unary(Node):
    """Unary terms"""

    def __init__(self, op, a):
        self.op = op
        self.a = a

    def evaluate(self, ctx):
        return self.op(self.a.evaluate(ctx))


class Const(Node):
    """Constant terms"""

    def __init__(self, a):
        self.a = a

    def evaluate(self, ctx):
        return self.a


class Func(Node):
    """Function terms"""

    def __init__(self, fn, args):
        self.fn = fn
        self.args = args

    def evaluate(self, ctx):
        return self.fn(*[a.evaluate(ctx) for a in self.args])


class List(Node):
    """List terms"""

    def __init__(self, l):
        self.l = l

    def evaluate(self, ctx):
        return [a.evaluate(ctx) for a in self.l]


class Variable(Node):
    """Variable terms"""

    def __init__(self, var):
        self.var = var

    def evaluate(self, ctx):
        try:
            value = ctx[self.var]
        except KeyError:
            log.warning("Variable %s could not found in the values."
                        % self.var)
            value = None
        return value
