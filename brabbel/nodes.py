import logging

log = logging.getLogger(__name__)

class Node(object):
    """Baseclass for all parsed terms"""

    def evaluate(self, ctx):
        raise NotImplementedError()


class Binary(Node):
    """Binary terms"""

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __eq__(self, other):
        return self.a == other.a and self.b == other.b


class Unary(Node):
    """Unary terms"""

    def __init__(self, a):
        self.a = a

    def __eq__(self, other):
        return self.a == other.a


class Not(Unary):
    """Optimized 'not' terms"""

    def evaluate(self, ctx):
        return not self.a.evaluate(ctx)


class And(Binary):
    """Optimized 'and' terms"""

    def evaluate(self, ctx):
        # Short eval
        return self.a.evaluate(ctx) and self.b.evaluate(ctx)


class Or(Binary):
    """Optimized 'or' terms"""

    def evaluate(self, ctx):
        # Short eval
        return self.a.evaluate(ctx) or self.b.evaluate(ctx)


class Const(Unary):
    """Constant terms"""

    def evaluate(self, ctx):
        return self.a


class Call(Node):
    """Call terms"""
    def __init__(self, fn, a):
        self.fn = fn
        self.a = a

    def evaluate(self, ctx):
        return self.fn(self.a.evaluate(ctx))

    def __eq__(self, other):
        return self.fn == other.fn and self.a == other.a


class Func(Node):
    """Function terms"""

    def __init__(self, fn, args):
        self.fn = fn
        self.args = args

    def evaluate(self, ctx):
        return self.fn(*[a.evaluate(ctx) for a in self.args])

    def __eq__(self, other):
        return self.fn == other.fn and self.args == other.args


class List(Node):
    """List terms"""

    def __init__(self, l):
        self.l = l

    def evaluate(self, ctx):
        return [a.evaluate(ctx) for a in self.l]

    def __eq__(self, other):
        return self.l == other.l


class Variable(Unary):
    """Variable terms"""

    def evaluate(self, ctx):
        try:
            value = ctx[self.a]
            if isinstance(value, basestring):
                value = value.replace("'", "\\'")
        except KeyError:
            log.warning("Variable %s could not found in the values."
                        % self.a)
            value = None
        return value


class Add(Binary):
    """'+' terms"""

    def evaluate(self, ctx):
        return self.a.evaluate(ctx) + self.b.evaluate(ctx)


class Sub(Binary):
    """'-' terms"""

    def evaluate(self, ctx):
        return self.a.evaluate(ctx) - self.b.evaluate(ctx)


class Mul(Binary):
    """'*' terms"""

    def evaluate(self, ctx):
        return self.a.evaluate(ctx) * self.b.evaluate(ctx)


class Div(Binary):
    """'/' terms"""

    def evaluate(self, ctx):
        """Divided a with b. In case a nd b are integer values return a
        integer values. Otherwise a float value will be returned"""
        a, b = self.a.evaluate(ctx), self.b.evaluate(ctx)
        if isinstance(b, int):
            return int(a / b)
        return a / b


class LT(Binary):
    """'<' terms"""

    def evaluate(self, ctx):
        return self.a.evaluate(ctx) < self.b.evaluate(ctx)


class GT(Binary):
    """'>' terms"""

    def evaluate(self, ctx):
        return self.a.evaluate(ctx) > self.b.evaluate(ctx)


class LE(Binary):
    """'<=' terms"""

    def evaluate(self, ctx):
        return self.a.evaluate(ctx) <= self.b.evaluate(ctx)


class GE(Binary):
    """'>=' terms"""

    def evaluate(self, ctx):
        return self.a.evaluate(ctx) >= self.b.evaluate(ctx)


class EQ(Binary):
    """'==' terms"""

    def evaluate(self, ctx):
        return self.a.evaluate(ctx) == self.b.evaluate(ctx)


class NE(Binary):
    """'!=' terms"""

    def evaluate(self, ctx):
        return self.a.evaluate(ctx) != self.b.evaluate(ctx)


class In(Binary):
    """'in' terms"""

    def evaluate(self, ctx):
        return self.a.evaluate(ctx) in self.b.evaluate(ctx)
