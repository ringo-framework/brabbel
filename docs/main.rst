Language
========

Operands
--------

Number
""""""
All numbers numbers are internally handled as floating point number.

*BNF*:  [ "-" ] '0' .. '9'+ | '.'

Examples::

        100 -> 100.0
        1.98 -> 1.98
        -23 -> -23

String
""""""
*BNF*:  ( 'a' .. 'z' | 'A' .. 'Z' | '0' .. '9')+ | '_' | ' ' | '-'

Variable
""""""""
Variables can be used as placeholder for dynamically injected values when
evaluating the expression.

*BNF*:  '$' ( 'a' .. 'z' | 'A' .. 'Z' | '0' .. '9' )+ | '_' | '-'

Listing
"""""""
*BNF*: [ ( Number | String )? + ( ',' ( Number | String) )* ]

Examples::

        ['a', 'b', 'c'] -> ['a', 'b', 'c']
        [1, 'b', ''] -> [1.0, 'b', '']
        [] -> []

Constants
"""""""""

 * True
 * False


Operators
---------
The following operators are supported

 * not
 * \+
 * \-
 * \*
 * /
 * <
 * <=
 * >=
 * >
 * ==
 * !=
 * and
 * or
 * in

Expamples::

        4 + 6 -> 10
        'foo' < 'foobar' -> True
        ka' in ['b', 'c'] -> False
        ( 2 > 3 ) or ( 'foo' != 'bar') -> True
        not ( 5 > 2 ) -> False

Functions
---------

date
""""
The date function can be used to craft a date in the expression.

Examples::

        date('today') -> date of today
        date('20150118') -> 18.01.2015

timedelta
"""""""""
The timedelta function can be used for handling intervals in form of 
"hh:mm:ss". 

Examples::
        timedelta('00:42:00') < timedelta('01:00:00')
        timedelta('04:00:00') + timedelta('01:00:00') == timedelta('05:00:00')
        
bool
""""
Returns True if the given value v is set and not empty. Empty means:

 * For String: No value or empty String
 * For Lists: No value or empty Lists
 * For Numbers: No value (0 is consideret as valid value)

Examples::

        bool("foo") -> True 
        bool("") -> False
        bool(['']) -> True
        bool([]) -> False
        bool(0) -> True

len
"""
Returns the length of a given list.

Examples::

        bool([1,2,3]) -> 3
        bool([]) -> 0
