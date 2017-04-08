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
# @email = 'mail@simon-dirmeier.net''


from ._dataframe_column_set import DataFrameColumnSet


class DataFrameGroup:
    """
    Class that represents a group within a DataFrame given a grouping vector.

    """
    def __init__(self, grp_idx, row_idxs, grouping_values,
                 grouping_colnames, **kwargs):
        self.__grp_idx = grp_idx
        self.__row_idxs = row_idxs
        self.__grouping_values = grouping_values
        self.__grouping_colnames = grouping_colnames
        self.__data_columns = DataFrameColumnSet(**kwargs)

    def __getitem__(self, item):
        """
        Getter method for DataFrame. Returns the column with name item.

        :param item: the name of a column
        :type item: str
        :return: returns a column from the DataFrame
        :rtype: DataFrameColumn
        """

        if isinstance(item, str) and item in self.__data_columns.colnames:
            return self.__data_columns[self.__data_columns.colnames.index(item)]
        raise TypeError("Wrong idx " +
                        "(either no string or item is not in DataFrame!")

    def __iter__(self):
        for i in range(self.__data_columns.nrow):
            yield self.__data_columns.row(i)

    def cbind(self, **kwargs):
        self.__data_columns.cbind(**kwargs)

    @property
    def grp_idx(self):
        return self.__grp_idx

    @property
    def grouping_values(self):
        return self.__grouping_values

    @property
    def grouping_colnames(self):
        """
        Getter for the grouping column names.

        :return: returns the grouping column names
        """
        return self.__grouping_colnames

    @property
    def row_idxs(self):
        return self.__row_idxs
