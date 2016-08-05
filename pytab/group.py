# @author = 'Simon Dirmeier'
# @email = 'rafstraumur@simon-dirmeier.net'

from pytab import GroupedTable, table_abstract
from pytab._check import _is_table


def group(obj, *args):
    if _is_table(obj):
        return _group_plain_table(obj, *args)


def _group_plain_table(obj, *args):
    return GroupedTable(obj, *args)
