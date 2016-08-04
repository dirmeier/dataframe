# @author = 'Simon Dirmeier'
# @email = 'rafstraumur@simon-dirmeier.net'

from pytab import GroupedTable, Table
from pytab._check import _is_table


def group(obj, *args):
    if _is_table(obj):
        return GroupedTable(obj, *args)

