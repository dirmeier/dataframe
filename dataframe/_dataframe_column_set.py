# @author = 'Simon Dirmeier'
# @email = 'rafstraumur@simon-dirmeier.net'
from itertools import chain
from prettytable import PrettyTable

from ._dataframe_column import DataFrameColumn
from ._dataframe_row import DataFrameRow


class DataFrameColumnSet:
    def __init__(self, **kwargs):
        self.__data_columns = []
        self.__nrow = -1
        self.cbind(**kwargs)

    def __getitem__(self, item):
        if isinstance(item, int):
            return self.__data_columns[item]
        raise ValueError("Item should be integer!")

    def __iter__(self):
        for col in self.__data_columns:
            yield col

    def __str__(self):
        pta = PrettyTable()
        for col in self.__data_columns:
            vals = col.values()
            if len(vals) > 10:
                vals = list(chain(vals[:3], "...", vals[-3:]))
            pta.add_column(col.colname(), vals)
        return pta.__str__()

    def nrow(self):
        return self.__nrow

    def ncol(self):
        return len(self.colnames())

    def colnames(self):
        return [x.colname() for x in self.__data_columns]

    def rows(self, idxs):
        return [self.row(i) for i in idxs]

    def row(self, idx):
        """
        Returns DataFrameRow of the DataFrame given its index.

        :param idx: the index of the row in the DataFrame.
        :return: returns a DataFrameRow
        """
        return DataFrameRow(idx, [x[idx] for x in self], self.colnames())

    def which_colnames(self, *args):
        idx = []
        for i in range(len(self.__data_columns)):
            if self.colnames()[i] in args:
                idx.append(i)
        return idx

    def cbind(self, **columns):
        keys = sorted([x for x in columns.keys()])
        for k in keys:
            self.__cbind(DataFrameColumn(str(k), columns.get(k)))

    def __cbind(self, column):
        if column.colname in self.colnames():
            ValueError("Appending duplicate col-name!")
        self.__data_columns.append(column)
        self.__nrow = self.__data_columns[-1].size()
        for col in self.__data_columns:
            if col.size() != self.__nrow:
                raise ValueError("Columns do not have equal lengths!")
