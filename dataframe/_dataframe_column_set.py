# dataframe: a data-frame implementation using method piping
#
# Copyright (C) 2016 Simon Dirmeier
#
# This file is part of dataframe.
#
# dataframe is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# dataframe is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with dataframe. If not, see <http://www.gnu.org/licenses/>.
#
#
# @author = 'Simon Dirmeier'
# @email = 'mail@simon-dirmeier.net'


from itertools import chain
import tabulate
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
        stri = "\nA dataframe"
        ta = []
        for col in self.__data_columns:
            vals = col.values
            if len(vals) > 10:
                vals = list(chain(vals[:3], "...", vals[-3:]))
            ta.append(vals)
        ta = tabulate.tabulate(zip(*ta), headers=self.colnames)
        return stri + "\n\n" + ta.__str__()

    @property
    def nrow(self):
        return self.__nrow

    @property
    def ncol(self):
        return len(self.colnames)

    @property
    def colnames(self):
        return [x.colname for x in self.__data_columns]

    def rows(self, idxs):
        return [self.row(i) for i in idxs]

    def row(self, idx):
        """
        Returns DataFrameRow of the DataFrame given its index.

        :param idx: the index of the row in the DataFrame.
        :return: returns a DataFrameRow
        """
        return DataFrameRow(idx, [x[idx] for x in self], self.colnames)

    def which_colnames(self, *args):
        idx = []
        for i in range(len(self.__data_columns)):
            if self.colnames[i] in args:
                idx.append(i)
        return idx

    def cbind(self, **columns):
        keys = sorted([x for x in columns.keys()])
        for k in keys:
            self.__cbind(DataFrameColumn(str(k), columns.get(k)))

    def __cbind(self, column):
        if column.colname in self.colnames:
            ValueError("Appending duplicate col-name!")
        self.__data_columns.append(column)
        self.__nrow = self.__data_columns[-1].size()
        for col in self.__data_columns:
            if col.size() != self.__nrow:
                raise ValueError("Columns do not have equal lengths!")
