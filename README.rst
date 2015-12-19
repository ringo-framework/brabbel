Brabbel
=======
.. image:: https://travis-ci.org/ringo-framework/brabbel.svg?branch=master
    :target: https://travis-ci.org/ringo-framework/brabbel
.. image:: https://api.codacy.com/project/badge/grade/bf6a0af8b49c47299184bfb31153b1b7
    :target: https://www.codacy.com/app/torsten/brabbel
    
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
