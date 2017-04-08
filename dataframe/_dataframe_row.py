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


class DataFrameRow:
    def __init__(self, idx, vals, colnames):
        self.__idx = idx
        self.__colnames = colnames
        self.__vals = vals

    def __hash__(self):
        return hash(self.__idx)

    def __eq__(self, other):
        if isinstance(other, DataFrameRow):
            return self.__idx == other.__idx
        return False

    def __getitem__(self, index):
        return self.__vals[index]

    def __str__(self):
        return str(self.idx()) + ":\t" + "\t".join(str(x) for x in self.__vals)

    def __repr__(self):
        return self.__str__()

    @property
    def idx(self):
        """
        Getter for the index of the DataFrameRow.

        :return: returns the index of the row
        """
        return self.__idx

    def values(self):
        return self.__vals

    def colnames(self):
        return self.__colnames
