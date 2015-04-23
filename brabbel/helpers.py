from __future__ import division
from builtins import str
from datetime import date, timedelta

########################################################################
#                              Operators                               #
########################################################################


def _in(a, b):
    return a in b

def _div(a, b):
    """Returns float in all cases"""
    return a / b

########################################################################
#                              Functions                               #
########################################################################


def _date(ds):
    if ds in ["'today'", 'today']:
        return date.today()
    else:
        ds = ds.strip("'")
        y = int(ds[0:4])
        m = int(ds[4:6])
        d = int(ds[6:8])
    return date(y, m, d)


def _timedelta(s):
    interval  = s.split(":")
    hours = int(interval[0])
    minutes = int(interval[1])
    seconds = int(interval[2])
    td = timedelta(hours=hours, minutes=minutes, seconds=seconds)
    return td


def _bool(v):
    """Returns True if the given value v is set and not empty. Empty
    means:

     * For String: No value or empty String
     * For Lists: No value or empty Lists
     * For Numbers: No value (0 is consideret as valid value)

    """
    if v is None:
        return False
    if isinstance(v, str):
        if v == "''":
            return False
        else:
            return bool(v)
    elif isinstance(v, list):
        if len(v) == 0:
            return False
        elif v[0] == '':
            # FIXME: check why empty lists become [''] after parsing.
            # (ti) <2014-10-23 10:56>
            return False
        else:
            return True
    else:
        return bool(str(v))


def _len(v):
    if isinstance(v, float):
        v = str(int(v))
    return len(v)
