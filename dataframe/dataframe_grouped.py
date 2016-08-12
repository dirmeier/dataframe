# @author = 'Simon Dirmeier'
# @email = 'rafstraumur@simon-dirmeier.net'
import numpy
from prettytable import PrettyTable

from ._dataframe_abstract import ADataFrame
from ._check import is_callable, is_none, has_elements
from .search_tree.search_tree import SearchTree


class GroupedDataFrame(ADataFrame):
    """
    The base GroupedDataFrame class. Subsets a dataframe object into several groups given several columns.
    """

    def __init__(self, obj, *args):
        self.__table = obj
        self.__search_col_idx = obj.which_colnames(*args)
        self.__group_col_names = args
        self.__search_tree = SearchTree()
        self.__group_idxs = numpy.zeros(obj.nrow()).astype(int)
        self.__grouping = {}
        self.__group_by()

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        """
        ToString method for GroupedDataFrame

        :return: returns the string representation
        :rtype: str
        """
        pt = PrettyTable(self.__table.colnames())
        for i, groups in enumerate(self.__grouping.values()):
            if i > 1:
                break
            rows = groups.values()
            for j, row in enumerate(rows):
                if j < 5:
                    pt.add_row(row.values())
            if i == 0:
                pt.add_row(["---"] * len(self.__table.colnames()))
        return pt.__str__()

    def __iter__(self):
        for _, v in self.__grouping.items():
            yield v

    def __getitem__(self, idx):
        return self.__grouping[idx]

    def ungroup(self):
        """
        Undo the grouping and return the DataFrame.

        :return: returns the original DataFrame
        :rtype: DataFrame
        """
        return self.__table

    def subset(self, *args):
        """
        Subset only some of the columns of the dataframe

        :param args: list of column names of the object that should be subsetted
        :type args: varargs
        :return: returns dataframe with only the columns you selected
        :rtype: DataFrame
        """
        pass

    def group(self, *args):
        """
        Group the dataframe into row-subsets.

        :param args: list of column names taht should be used for grouping
        :type args: varargs
        :return: returns a dataframe that has grouping information
        :rtype: GroupedDataFrame
        """
        pass

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
        if is_callable(clazz) and not is_none(new_col) and has_elements(*args):
            return self.__do_aggregate(clazz, new_col, *args)

    def __do_aggregate(self, clazz, new_col, *col_names):
        gr = []
        new_col_names = [x for x in self.__group_col_names if x not in col_names]
        # get columns
        df = self.__table.subset(*col_names)
        for group_idx in numpy.unique(self.__group_idxs):
            # get the rows that have index group_idx
            row_idxs = numpy.where(self.__group_idxs == group_idx)[0]
            colvals = [df[colname][row_idxs]for colname in df.colnames()]
            if colvals is None:
                return None
            # instantiate class and call
            res = [clazz()(*colvals)]
            if len(res) != 1:
                raise ValueError("The function you provided yields an array of false length!")

        #return DataFrame(**{new_col: res})

    def __group_indexes(self):
        return self.__group_idxs

    def groups(self):
        return self.__grouping.values()

    def __group_by(self ):
        for row in self.__table:
            self.__add_grp(row)

    def __add_grp(self, row):
        els = [row[x] for x in self.__search_col_idx]
        grp_idx = self.__search_tree.find(*els)
        self.__group_idxs[row.idx()] = grp_idx
        if grp_idx not in self.__grouping:
            # TODO: more clever idea here
            self.__grouping[grp_idx] = Group(grp_idx)
        self.__grouping[grp_idx].append(row)


class Group:
    def __init__(self, grp_idx):
        self.__grp_idx = grp_idx
        self.__data

    def __str__(self):
        buf = "Group " + str(self.__grp_idx) + ":"
        for i in self.__rows:
            buf += " " + i.__str__()
        return buf

    def __repr__(self):
        return self.__str__()

    def __getitem__(self, idx):
        return self.__rows[idx]

    def __iter__(self):
        for i in self.__rows:
            yield i

    def append(self, el):
        self.__rows.append(el)

    def __grp_index(self):
        return self.__grp_idx

    def values(self):
        return self.__rows
