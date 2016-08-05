# @author = 'Simon Dirmeier'
# @email = 'rafstraumur@simon.dirmeier.net'
from pytab.subset import subset, _subset_plain_table

from pytab.table_abstract import Table
from pytab.table_row import TableRow
from pytab.table_column import TableColumn
from pytab.group import group, _group_plain_table
from pytab.modify import modify, _modify_plain_table


class PlainTable(Table):
    def __init__(self, **kwargs):
        self.__data_columns = []
        self.__colnames = []
        self.__ncol = len(kwargs)
        self.__append(**kwargs)

    def __iter__(self):
        for i in range(self.__nrow):
            yield TableRow(i, [x[i] for x in self.__data_columns], self.__colnames)

    def __getitem__(self, item):
        if item in self.__colnames:
            return self.__data_columns[item]
        return None

    def aggregate(self, f, new_col, *args):
        return _aggregate_plain_table(self, f, new_col, *args)

    def subset(self, *args):
        return _subset_plain_table(self, *args)

    def group(self, *args):
        return _group_plain_table(self, *args)

    def modify(self, f, new_col, *args):
        return _modify_plain_table(self, f, new_col, *args)

    def _nrow(self):
        return self.__nrow

    def _ncol(self):
        return self.__ncol

    def _cbind(self, **kwargs):
        self.__append(**kwargs)

    def _colnames(self):
        return self.__colnames

    def _columns(self):
        return self.__data_columns

    def _which_colnames(self, *args):
        idx = []
        for i in range(len(self.__colnames)):
            if self.__colnames[i] in args:
                idx.append(i)
        return idx

    def __append(self, **kwargs):
        keys = [x for x in kwargs.keys()]
        keys.sort()
        lens = set()
        for k in keys:
            v = kwargs.get(k)
            if k in self.__colnames:
                print("Appending duplicate colname!")
            self.__colnames.append(k)
            self.__data_columns.append(TableColumn(k, v))
            lens.add(len(v))
        if len(lens) != 1:
            raise ValueError("Columns don't have equal sizes!")
        self.__nrow = list(lens).pop()
