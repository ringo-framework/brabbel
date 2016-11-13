import operator

def _div(a, b):
    """Divided a with b. In case a nd b are integer values return a
    integer values. Otherwise a float value will be returned"""
    if isinstance(b, int):
        return int(a / b)
    return a / b

def _in(a, b):
    """Returns true if a is in list b"""
    return a in b

operators = {
    "not": operator.not_,
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": _div,
    "<": operator.lt,
    "lt": operator.lt,
    "<=": operator.le,
    "le": operator.le,
    ">=": operator.ge,
    "ge": operator.ge,
    ">": operator.gt,
    "gt": operator.gt,
    "==": operator.eq,
    "eq": operator.eq,
    "!=": operator.ne,
    "ne": operator.ne,
    "and": operator.and_,
    "or": operator.or_,
    "in": _in,
}
