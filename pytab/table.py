# @author = 'Simon Dirmeier'
# @email = 'rafstraumur@simon.dirmeier.net'


from pytab.group_by import group_by_
from pytab.table_row import TableRow


class Table:
    def __init__(self):
        self._nrow = -1
        self._ncol = -1
        self._data_columns = {}

    def __iter__(self):
        for i in range(self._nrow):
            yield TableRow([x[i] for x in self._data_columns.values()])

    def group_by(self, *args):
        return group_by_(self, *args)

