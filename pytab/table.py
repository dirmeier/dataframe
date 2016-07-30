# @author = 'Simon Dirmeier'
# @email = 'rafstraumur@simon.dirmeier.net'

from pytab import TableRow, TableGrouping


class Table:
    def __init__(self):
        self._nrow = -1
        self._ncol = -1
        self._data_columns = {}

    def __iter__(self):
        for i in range(self._nrow):
            yield TableRow([x[i] for x in self._data_columns.values()])

    def group_by(self, *args):
        grp, grping = TableGrouping.group_by(self, *args)
        return GroupedTable(self, grp, grping)

class GroupedTable(Table):
    def __init__(self, groups, grouping):
        super().__init__()
        self.groups = groups
        self.grouping = grouping