from builtins import str
from datetime import date, timedelta

def _date(ds):
    """Will convert a given string into a date object. The given date can have the following format:

    today
        Will generate to current date
    YYYYMMDD
        Will generate the date of year (YYYY) month (MM) day (DD)

    :v: Value to be checked
    :returns: Date object

    """
    if ds in ["'today'", 'today']:
        return date.today()
    else:
        ds = ds.strip("'")
        y = int(ds[0:4])
        m = int(ds[4:6])
        d = int(ds[6:8])
    return date(y, m, d)


def _timedelta(s):
    """Will convert a given string into a timedelte object. The given
    date can have the following format:

    HH:MM:SS
        Will generate the timedelta of hours (HH) minutes (MM) and
        seconds (SS)

    :v: Value to be checked
    :returns: Timedelta object

    """
    interval  = s.split(":")
    hours = int(interval[0])
    minutes = int(interval[1])
    seconds = int(interval[2])
    td = timedelta(hours=hours, minutes=minutes, seconds=seconds)
    return td


def _bool(v):
    """Will check if the given value is set and not empty. Empty means:

    * For String: No value or empty String
    * For Lists: No value or empty Lists
    * For Numbers: No value (0 is consideret as valid value)

    >>> _bool(None)
    False
    >>> _bool(False)
    False
    >>> _bool(True)
    True
    >>> _bool('')
    False
    >>> _bool('  ')
    True
    >>> _bool([])
    False
    >>> _bool(0)
    True
    >>> _bool('foo')
    True

    :v: Value to be checked
    :returns: True or False

    """
    if v is None:
        return False
    if isinstance(v, bool):
        return v
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
    """Will return of the given value. For all values except a list the
    value will be converted into a string first and the length of the
    string will be returned. In case of a None value the length will be
    0.

    >>> _len(1.0)
    3
    >>> _len(1234)
    4
    >>> _len([1,2,3,4,5])
    5
    >>> _len('')
    0
    >>> _len(None)
    0

    :v: Value to be checked
    :returns: True or False

    """
    if isinstance(v, list):
        return len(v)
    elif v is None:
        return 0
    return len(unicode(v))

functions = {
    "date": _date,
    "timedelta": _timedelta,
    "bool": _bool,
    "len": _len
}
