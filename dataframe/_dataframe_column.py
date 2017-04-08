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


class DataFrameColumn:
    """
    Class that represents one column in a dataframe.

    """
    def __init__(self, colname, vals):
        self.__colname = colname
        self.__vals = vals

    def size(self):
        """
        Getter for number if items in the column.

        :return: returns the number of items
        """
        return len(self.__vals)

    @property
    def values(self):
        """
        Getter for the column values.

        :return: returns the values of the column
        """
        return self.__vals

    @property
    def colname(self):
        """
        Getter for the column name.

        :return: returns the column name
        """
        return self.__colname

    def __getitem__(self, index):
        if isinstance(index, slice) or isinstance(index, int):
            return self.__vals[index]
        elif isinstance(index, tuple):
            return [self.__vals[x] for x in list(index)]
        elif isinstance(index, list):
            return [self.__vals[x] for x in index]
        return self.__vals[index]

    def __len__(self):
        return len(self.__vals)
