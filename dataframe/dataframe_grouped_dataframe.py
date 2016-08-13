# @author = 'Simon Dirmeier'
# @email = 'rafstraumur@simon-dirmeier.net'
import itertools
import numpy

from ._dataframe_abstract import ADataFrame
from ._check import is_callable, is_none, has_elements, disjoint
from ._dataframe_grouping import DataFrameGrouping
import dataframe.dataframe_dataframe


class GroupedDataFrame(ADataFrame):
    """
    The base GroupedDataFrame class. Subsets a dataframe object into several groups given several columns.
    """

    def __init__(self, obj, *args):
        self.__grouping = DataFrameGrouping(obj, *args)

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        """
        ToString method for GroupedDataFrame

        :return: returns the string representation
        :rtype: str
        """
        return self.__grouping.__str__()

    def __iter__(self):
        for _, v in self.__grouping:
            yield v

    def groups(self):
        return self.__grouping.groups()

    def ungroup(self):
        """
        Undo the grouping and return the DataFrame.

        :return: returns the original DataFrame
        :rtype: DataFrame
        """
        return self.__grouping.ungroup()

    def subset(self, *args):
        """
        Subset only some of the columns of the dataframe

        :param args: list of column names of the object that should be subsetted
        :type args: varargs
        :return: returns dataframe with only the columns you selected
        :rtype: DataFrame
        """
        return GroupedDataFrame(self.__grouping.ungroup().subset(*args),
                                *self.__grouping.grouping_column_names())

    def group(self, *args):
        """
        Group the dataframe into row-subsets.

        :param args: list of column names taht should be used for grouping
        :type args: varargs
        :return: returns a dataframe that has grouping information
        :rtype: GroupedDataFrame
        """
        list(args).append(x for x in self.__grouping.grouping_column_names() if x not in args)
        return GroupedDataFrame(self.__grouping.ungroup(), *args)

    def modify(self, clazz, new_col, *args):
        """
        Modify some columns (i.e. apply a function) and add the result to the table

        :param clazz: name of a class that extends class Callable
        :type clazz: class
        :param new_col: name of the new column
        :type new_col: str
        :param args: list of column names of the object that function should be applied to
        :type args: varargs
        :return: returns a new dataframe object with the aggregated value
        :rtype: DataFrame
        """
        if is_callable(clazz) \
                and not is_none(new_col) \
                and has_elements(*args) \
                and disjoint(self.__grouping.grouping_colnames(), *args):
            return self.__do_modify(clazz, new_col, *args)

    def __do_modify(self, clazz, new_col, *col_names):
        pass

    def aggregate(self, clazz, new_col, *args):
        """
        Aggregate the rows of each group into a single value.

        :param clazz: name of a class that extends class Callable
        :type clazz: class
        :param new_col: name of the new column
        :type new_col: str
        :param args: list of column names of the object that function should be applied to
        :type args: varargs
        :return: returns a new dataframe object with the aggregated value
        :rtype: DataFrame
        """
        if is_callable(clazz) \
                and not is_none(new_col) \
                and has_elements(*args) \
                and disjoint(self.__grouping.grouping_colnames(), *args):
            return self.__do_aggregate(clazz, new_col, *args)

    def __do_aggregate(self, clazz, new_col, *col_names):
        resvals = {i: [] for i in itertools.chain(self.__grouping.grouping_colnames(), new_col)}
        for _, group in self.__grouping:
            colvals = [group[x] for x in col_names]
            res = clazz()(*colvals)
            if hasattr(res, "__len__"):
                raise ValueError("The function you provided yields an array of false length!")
            resvals[new_col].append(res)
            for i, e in enumerate(group.grouping_colnames()):
                resvals[e].append(group.grouping_values()[i])
        return dataframe.DataFrame(**resvals)
