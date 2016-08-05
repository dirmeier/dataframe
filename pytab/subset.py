# @author = 'Simon Dirmeier'
# @email = 'rafstraumur@simon-dirmeier.net'
from pytab.table_plain import PlainTable
from pytab._check import _is_table


def subset(obj, *args):
    if _is_table(obj):
        return _subset_plain_table(obj, *args)

def _subset_plain_table(obj, *args):
    cols = {}
    for k in obj.__colnames:
        if k in args:
            cols[k] = obj.__data_columns[k]._values()
    return PlainTable(**cols)

