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


import copy
import dataframe
from ._dataframe_abstract import ADataFrame
from ._dataframe_grouping import DataFrameGrouping
from ._check import is_callable, is_none, has_elements, is_disjoint
from ._piping_exception import PipingException

__DISJOINT_SETS_ERROR__ = "Cannot aggregate grouping variable(s)!"


class GroupedDataFrame(ADataFrame):
    """
    The base GroupedDataFrame class.
    Subsets a DataFrame object into several groups given several columns.
    """

    def __init__(self, obj, *args):
        self.__grouping = DataFrameGrouping(obj, *args)

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        """
        ToString method for GroupedDataFrame.

        :return: returns the string representation
        :rtype: str
        """
        return self.__grouping.__str__()

    def __iter__(self):
        for _, group in self.__grouping:
            yield group

    def __rrshift__(self, other):
        raise PipingException("")

    @property
    def colnames(self):
        """
        Getter for the column names of the DataFrame.

        :return: returns column names
        :rtype: list(str)
        """
        return self.__grouping.ungroup().colnames

    @property
    def groups(self):
        """
        Getter for all groups.

        :return: returns the groups
        :rtype: list(DataFrameGroup)
        """
        return self.__grouping.groups

    def ungroup(self):
        """
        Undo the grouping and return the DataFrame.

        :return: returns the original DataFrame
        :rtype: DataFrame
        """
        return self.__grouping.ungroup()

    def subset(self, *args):
        """
        Subset only some of the columns of the DataFrame.

        :param args: list of column names of the object that should be subsetted
        :type args: tuple
        :return: returns DataFrame with only the columns you selected
        :rtype: DataFrame
        """
        args = list(args)
        args.extend([x for x in
                     self.__grouping.grouping_colnames if x not in args])
        return GroupedDataFrame(self.__grouping.ungroup().subset(*args),
                                *self.__grouping.grouping_colnames)

    def group(self, *args):
        """
        Group the DataFrame into row-subsets.

        :param args: list of column names taht should be used for grouping
        :type args: tuple
        :return: returns a dataframe that has grouping information
        :rtype: GroupedDataFrame
        """
        args = list(args)
        args.extend([x for x in
                     self.__grouping.grouping_colnames if x not in args])
        return GroupedDataFrame(self.__grouping.ungroup(), *args)

    def modify(self, clazz, new_col, *args):
        """
        Modify some columns (i.e. apply a function)
         and add the result to the table.

        :param clazz: name of a class that extends class Callable
        :type clazz: class
        :param new_col: name of the new column
        :type new_col: str
        :param args: list of column names of the object that
         function should be applied to
        :type args: tuple
        :return: returns a new GroupedDataFrame object with the modified
          values, i.e. the new column of values
        :rtype: GroupedDataFrame
        """
        if is_callable(clazz) \
                and not is_none(new_col) \
                and has_elements(*args) \
                and is_disjoint(self.__grouping.grouping_colnames,
                                args,
                                __DISJOINT_SETS_ERROR__):
            return self.__do_modify(clazz, new_col, *args)

    def __do_modify(self, clazz, new_col, *col_names):
        dfr = copy.deepcopy(self.__grouping.ungroup())
        new_rows = [None] * dfr.nrow
        for _, group in self.__grouping:
            colvals = [group[x] for x in col_names]
            res = clazz()(*colvals)
            if len(res) != len(colvals[0].values):
                raise ValueError("The function you provided yields " +
                                 "an array of false length!")
            for i, row in enumerate(group.row_idxs):
                new_rows[row] = res[i]
        return dfr.cbind(**{new_col: new_rows}).group(
            *self.__grouping.grouping_colnames)

    def aggregate(self, clazz, new_col, *args):
        """
        Aggregate the rows of each group into a single value.

        :param clazz: name of a class that extends class Callable
        :type clazz: class
        :param new_col: name of the new column
        :type new_col: str
        :param args: list of column names of the object that
         function should be applied to
        :type args: varargs
        :return: returns a new dataframe object with the aggregated value
        :rtype: DataFrame
        """
        if is_callable(clazz) \
                and not is_none(new_col) \
                and has_elements(*args) \
                and is_disjoint(self.__grouping.grouping_colnames,
                                args,
                                __DISJOINT_SETS_ERROR__):
            return self.__do_aggregate(clazz, new_col, *args)

    def __do_aggregate(self, clazz, new_col, *col_names):
        # init a dictionary of lists where the keys are the grouping
        # colnames + the new column name
        resvals = {i: [] for i in self.__grouping.grouping_colnames}
        resvals[new_col] = []
        # iterate over every group
        for _, group in self.__grouping:
            # get the columns that should be used for aggregation
            colvals = [group[x] for x in col_names]
            # cal the result
            res = clazz()(*colvals)
            if hasattr(res, "__len__"):
                raise ValueError(
                    "The function you provided yields an array " +
                    "of false length!")
            resvals[new_col].append(res)
            for i, colname in enumerate(group.grouping_colnames):
                resvals[colname].append(group.grouping_values[i])
        # create a new UN-GROUPED data-frame object
        return dataframe.DataFrame(**resvals)
