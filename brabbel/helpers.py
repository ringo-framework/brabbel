from datetime import date

########################################################################
#                              Operators                               #
########################################################################


def _in(a, b):
    return a in b

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


def _bool(v):
    if v == "''":
        return False
    return bool(v)
