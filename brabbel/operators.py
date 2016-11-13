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

def _none_save(op):
    def fn(a, b):
        return None if a is None or b is None else op(a, b)
    return fn

operators = {
    "not": operator.not_,
    "+": _none_save(operator.add),
    "-": _none_save(operator.sub),
    "*": _none_save(operator.mul),
    "/": _none_save(_div),
    "<": _none_save(operator.lt),
    "lt": _none_save(operator.lt),
    "<=": _none_save(operator.le),
    "le": _none_save(operator.le),
    ">=": _none_save(operator.ge),
    "ge": _none_save(operator.ge),
    ">": _none_save(operator.gt),
    "gt": _none_save(operator.gt),
    "==": operator.eq,
    "eq": operator.eq,
    "!=": operator.ne,
    "ne": operator.ne,
    "and": operator.and_,
    "or": operator.or_,
    "in": _in,
}
