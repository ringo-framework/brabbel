Brabbel
=======
Brabbel is a simple python based expression language. Brabbel can be used to
evaluate basic arithmetic and boolean expression on a given set of python
values in a save way.

Example::

        from brabbel import Expression
        expr = Expression("$foo < $bar")
        values = {"foo": 1, "bar": 2}
        expr.evaluate(values)
        -> True

For more information please read the documentation on
http://brabbel.readthedocs.org/en/latest
