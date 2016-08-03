# @author = 'Simon Dirmeier'
# @email = 'rafstraumur@simon.dirmeier.net'

from pytab.table_row import TableRow
from pytab.table_column import TableColumn
from pytab.grouped_table import GroupedTable

class Table:
    def __init__(self, **kwargs):
        lens = set()
        self.__data_columns = []
        self.__colnames = []
        keys = [x for x in kwargs.keys()]
        keys.sort()
        for k in keys:
            v = kwargs.get(k)
            self.__colnames.append(k)
            self.__data_columns.append(TableColumn(k, v))
            lens.add(len(v))
        if len(lens) != 1:
            raise ValueError("Columns don't have equal sizes!")
        for k in lens:
            self.__nrow = k
        self.__ncol = len(kwargs)

    def __iter__(self):
        for i in range(self.__nrow):
            yield TableRow(i, [x[i] for x in self.__data_columns], self.__colnames)

    def nrow(self):
        return self.__nrow

    def ncol(self):
        return self.__ncol

    def select(self, *args):
        cols = {}
        for k in self.__colnames:
            if k in args:
                cols[k] = self.__data_columns[k]._values()
        return Table(**cols)

    def colnames(self):
        return self.__colnames

    def columns(self):
        return self.__data_columns

    def mutate(self):
        pass

    def group_by(self, *args):
        return GroupedTable(self, *args)

    def _which_colnames(self, *args):
        idx = []
        for i in range(len(self.__colnames)):
            if self.__colnames[i] in args:
                idx.append(i)
        return idx


