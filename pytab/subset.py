# @author = 'Simon Dirmeier'
# @email = 'rafstraumur@simon-dirmeier.net'
from pytab import Table
from pytab._check import _is_table


def columns(obj, *args):
    if _is_table(obj):
        return __columns(obj, *args)

def __columns(obj, *args):
    cols = {}
    for k in obj.__colnames:
        if k in args:
            cols[k] = obj.__data_columns[k]._values()
    return Table(**cols)

