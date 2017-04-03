********
Language
********

Types
=====

Number
------
Number in general means float and integers. If possible the given value will
be casted into integer. If casting fails the value will be tried to converted
into a float value.

.. doctest::

        >>> expr = "10"
        >>> Expression(expr).evaluate()
        10
        >>> expr = "10.0"
        >>> Expression(expr).evaluate()
        10.0
        >>> expr = "0"
        >>> Expression(expr).evaluate()
        0
        >>> expr = "0.0"
        >>> Expression(expr).evaluate()
        0
        >>> expr = "012"
        >>> Expression(expr).evaluate()
        12 

String
------
All String are handled internally as a unicode string. Actually they will be
encoded on parsing to ensure that they are unicode. 

.. note::
        Strings currently only have a limited subset of chars.

:BNF:

.. parsed-literal::

        lquote ::= "'"
        rquote ::= lquote
        char   ::= a .. z | A .. Z | "  " | "-" | "_" | ":"
        chars  ::= char | char chars
        string ::= lquote + chars + rquote


:Examples:

.. doctest::

        >>> expr = "'Foo'"
        >>> Expression(expr).evaluate()
        u'Foo'
        >>> expr = "'Foo Bar'"
        >>> Expression(expr).evaluate()
        u'Foo Bar'

Listings
--------
:BNF:
.. parsed-literal::

        lbr     ::= "["
        rbr     ::= rbr
        item    ::= string | number
        items   ::= item | "," + item  items
        listing ::= lbr + items + rbr

:Examples:
.. doctest::

        >>> expr = "[1, 2, 'foo', '42', 23]"
        >>> Expression(expr).evaluate()
        [1, 2, u'foo', u'42', 23]

Variables
---------
Variables can be used as placeholder for dynamically injected values when
evaluating the expression.

:BNF:
.. parsed-literal::

        varsign  ::= "$"
        char     ::= a .. z | A .. Z | "_"
        chars    ::= char | char chars
        variable ::= varsign + chars

:Examples:
.. doctest::

        >>> rule = "$foo < $bar"
        >>> values = {'foo': 23, 'bar': 42}
        >>> Expression(rule).evaluate(values)
        True

The variables `$foo` and `$bar` will be replaced by the values in the values
dictionary before the rule gets evaluated.

Constants
---------
True
^^^^
Will be converted into the Python "True" value.

.. doctest::

        >>> rule = "True == ($foo < $bar)"
        >>> values = {'foo': 23, 'bar': 42}
        >>> Expression(rule).evaluate(values)
        True

False
^^^^^
Will be converted into the Python "False" value.

.. doctest::

        >>> rule = "False == ($foo > $bar)"
        >>> values = {'foo': 23, 'bar': 42}
        >>> Expression(rule).evaluate(values)
        True

None
^^^^
Will be converted into the Python "False" value.

Operators
=========
The following operators are supported:

.. important::

    In general **the operands of the operators must be
    of the same type!** Otherwise a TypeError will be raised. So
    Comparison of String and Integer values can not be done. This is
    escpesially important for None values. See :ref:`pitfall_nonevalue`.

And
---
.. autofunction:: operator.and_

Or
--
.. autofunction:: operator.or_

Not
---
.. autofunction:: operator.not_

==
--
.. autofunction:: operator.eq

!=
--
.. autofunction:: operator.ne

>
--
.. autofunction:: operator.lt


>=
--
.. autofunction:: operator.le

<
--
.. autofunction:: operator.lt

<=
--
.. autofunction:: operator.le

\+
--
.. autofunction:: operator.add

\-
--
.. autofunction:: operator.sub

\*
--
.. autofunction:: operator.mul

\/
--
.. autoclass:: brabbel.operators.Div
   :inherited-members:

In
--
.. autoclass:: brabbel.operators.In
   :inherited-members:


Functions
=========

Bool
----
.. autofunction:: brabbel.functions._bool

Date
----
.. autofunction:: brabbel.functions._date

Len
---
.. autofunction:: brabbel.functions._len

Timedelta
---------
.. autofunction:: brabbel.functions._timedelta

Brabbel Pitfalls
================
Brabbel is not perfect. There are a number things where the Language
might not behave as expected. This can become a pitfall in some cases so
this section will list some of them. If you know more please write me an
Email so I can add these here.

Singlequotes in Strings
-----------------------
Strings are surrounded by singlequotes. This is true for variables and for
static strings. If you want to write a rule including a singlequote with
the string you need to escape the string properly::

       "$string == 'Thats\'s my variable'"


.. _pitfall_nonevalue:

Handling None values
--------------------
Because Brabbel can only use the operators with operands of the same
type you must take care to handle the case that some of the values in an
Expression may be None. This will fail if '$foo' is None::

    $foo < date('today')

Please handle possible None values this way::

    not bool($foo) or $foo < date('today')

None Constant
-------------
Currently the None constant will actually be converted into False.
