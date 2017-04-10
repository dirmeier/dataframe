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


import numpy
import tabulate
from ._dataframe_group import DataFrameGroup
from dataframe.search_tree import SearchTree

__DISJOINT_SETS_ERROR__ = "Subsetting on non-available columns!"


class DataFrameGrouping:
    """
    Class that holds information o how every row in a data frame is grouped
    into subsets.
    """

    def __init__(self, obj, *args):
        self.__dataframe = obj
        for arg in args:
            if arg not in obj.colnames:
                raise ValueError("Argument '{}' not in colnames".format(arg))
        # the indexes of the columns of the original table
        # that are used for grouping
        self.__grouping_col_idx = obj.which_colnames(*args)
        # the column names of the original table that are used for grouping
        self.__grouping_col_names = [x for x in args]
        # the array if values that produces a group
        # ( e.g. 0 -> [0,1], 1 -> [1,0], etc.)
        self.__grouping_values = {}
        # indexing tree for logarithmic lookup of group index
        self.__search_tree = SearchTree()
        # array of group indexes for every row,
        # i.e. every element is the group index the row belongs to
        self.__group_idxs = numpy.zeros(obj.nrow).astype(int)
        # groups: maps from grp index to group object
        self.__groups = dict()
        self.__group_by()

    def __iter__(self):
        for key, value in self.__groups.items():
            yield key, value

    def __getitem__(self, item):
        if isinstance(item, str):
            return self.__groups[item]

    def __str__(self):
        stri = "\nA dataframe grouped by (" + \
              ", ".join(self.__grouping_col_names) + ")"
        ta = []
        for i, group in enumerate(self.__groups.values()):
            if i > 1:
                break
            for j, row in enumerate(group):
                if j < 5:
                    ta.append(row.values())
            if i == 0:
                ta.append(["---"] * len(self.__dataframe.colnames))
        ta = tabulate.tabulate(ta, headers=self.__dataframe.colnames)
        return stri + "\n\n" + ta.__str__()

    @property
    def grouping_colnames(self):
        """
        Getter for the grouping column names.

        :return: returns the grouping column names
        """
        return self.__grouping_col_names

    @property
    def groups(self):
        """
        Getter the values of the group dictionary, i.e. the Group objects

        :return: returns the groupings of the rows
        :rtype: list(DataFrameGroup)
        """
        return self.__groups.values()

    def ungroup(self):
        """
        Getter for the normal DataFrame object without grouping information.

        :return: returns the ungrouped DataFrame
        :rtype: DataFrame
        """
        return self.__dataframe

    def __group_by(self):
        self.__set_grp_idxs()
        self.__set_groups()

    def __set_grp_idxs(self):
        # iterate over all rows from the dataframe and
        # assign each row a group index
        for row in self.__dataframe:
            els = [row[x] for x in self.__grouping_col_idx]
            grp_idx = self.__search_tree.find(*els)
            self.__group_idxs[row.idx] = grp_idx
            self.__grouping_values[str(grp_idx)] = els

    def __set_groups(self):
        # iterate over the array of group assignments
        # add each row of the original DataFrame to the specific group
        # get unique group indexes
        for grp_idx in numpy.unique(self.__group_idxs):
            # get the row indexes of the original data frame that belong
            # to group 'grp_idx' and cast to list
            row_idxs = list(numpy.where(self.__group_idxs == grp_idx)[0])
            # get the columns with the respective indexes from the dataframe
            group_columns = {x: self.__dataframe[x][row_idxs]
                             for x in self.__dataframe.colnames}
            # add the rows to a new group
            self.__groups[str(grp_idx)] = \
                DataFrameGroup(grp_idx,
                               row_idxs,
                               self.__grouping_values[str(grp_idx)],
                               self.__grouping_col_names,
                               **group_columns)
