# @author = 'Simon Dirmeier'
# @email = 'rafstraumur@simon.dirmeier.net'

from pytab.table_grouping import TableGrouping
from pytab.table_column import TableColumn
from pytab.grouped_table import GroupedTable

class Table:
    def __init__(self, **kwargs):
        lens = set()
        self.__data_columns = {}
        self.__colnames = []
        for k, v in kwargs.items():
            self.__colnames.append(k)
            self.__data_columns[k] = TableColumn(k, v)
            lens.add(len(v))
        if len(lens) != 1:
            raise ValueError("Columns don't have equal sizes!")
        for k in lens:
            self.__nrow = k
        self.__ncol = len(kwargs)

    def __iter__(self):
        for i in range(self.__nrow):
            yield Table(i, [x[i] for x in self.__data_columns.values()])

    def nrow(self):
        return self.__nrow

    def ncol(self):
        return self.__ncol

    def select(self, *args):
        cols = {}
        for k in self.__colnames:
            if k in args:
                cols[k] = self.__data_columns[k].values()
        return Table(**cols)

    def colnames(self):
        return self.__colnames

    def group_by(self, *args):
        grp, grping = TableGrouping.group_by(self, *args)
        return GroupedTable(self, grp, grping)

