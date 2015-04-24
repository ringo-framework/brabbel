********
Language
********

Types
=====

Number
------

String
------

Listings
--------

Constants
---------
 * True
 * False
 * None

Variable
--------
Variables can be used as placeholder for dynamically injected values when
evaluating the expression.

Operators
=========
The following operators are supported:

And
---

Or
--

Not
---

==
--

!=
--
>
--


>=
--

<
--

<=
--

+
--

-
--

*
--

/
--

In
--


Functions
=========

Bool
----
.. autofunction:: brabbel.helpers._bool


Date
----
.. autofunction:: brabbel.helpers._date

Len
---
.. autofunction:: brabbel.helpers._len

timedelta
---------
The timedelta function can be used for handling intervals in form of 
"hh:mm:ss". 

Examples::
        timedelta('00:42:00') < timedelta('01:00:00')
        timedelta('04:00:00') + timedelta('01:00:00') == timedelta('05:00:00')
