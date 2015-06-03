Getting Started
***************

About
=====
Brabbel is a small expression language able to do some evaluations on a given
set of values.

Brabbel is the German description for the first "language" of a baby and
should emphasise the limited capabilities of the language.

Installation
============
Formbar is available as `Pypi package <https://pypi.python.org/pypi/brabbel>`_.
To install it use the following command::

        <venv> pip install brabbel

The source is availble on `Bitbucket <https://bitbucket.org/ti/brabbel>`_.
You can check of the source and install the library with the following
command::
        
        (venv)> hg clone https://bitbucket.org/ti/brabbel
        (venv)> cd brabbel


Quickstart
==========
Here is a short example on how to use brabbel::

        from brabbel import Expression
        expr = Expression("$foo < $bar")
        values = {"foo": 1, "bar": 2}
        expr.evaluate(values)
        -> True

License
=======
Brabbel is licensed with under the GNU General Public License version >= 2.


Authors
=======
Torsten Irländer <torsten at irlaender dot de>
