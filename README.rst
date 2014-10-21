Brabbel
=======

How to start:

{{{
from brabbel import Expression

expr = Expression("(4 + 6) * $var")
result = expr.evaluate({"var": 10})
print result
>>> 100.0

}}}
