# @author = 'Simon Dirmeier'
# @email = 'rafstraumur@simon-dirmeier.net'

import numpy
from io import StringIO
from dataframe.dataframe_abstract import ADataFrame
from dataframe.search_tree.search_tree import SearchTree


class GroupedDataFrame(ADataFrame):
    def __init__(self, obj, *args):
        self.__table = obj
        self.__search_col_idx = obj._which_colnames(*args)
        self.__search_tree = SearchTree()
        self.__group_idxs = numpy.zeros(obj._nrow()).astype(int)
        self.__grouping = {}
        self.__group_by()

    def __iter__(self):
        for _, v in self.__grouping.items():
            yield v

    def __getitem__(self, idx):
        return self.__grouping[idx]

    def subset(self):
        pass

    def group(self, *args):
        pass

    def modify(self, f, new_col, *args):
        pass

    def aggregate(self, f, new_col, *args):
        pass

    def _group_indexes(self):
        return self.__group_idxs

    def _groups(self):
        return self.__grouping.values()

    def __group_by(self, ):
        for row in self.__table:
            self.__add_grp(row)

    def __add_grp(self, row):
        els = [row[x] for x in self.__search_col_idx]
        grp_idx = self.__search_tree.find(*els)
        self.__group_idxs[row.idx()] = grp_idx
        if grp_idx not in self.__grouping:
            # TODO: more clever idea here
            self.__grouping[grp_idx] = Group(grp_idx)
        self.__grouping[grp_idx]._append(row)

class Group:
    def __init__(self, grp_idx):
        self.__grp_idx = grp_idx
        self.__rows = []

    def __str__(self):
        buf = StringIO()
        buf.write("Group " + str(self.__grp_idx) + ":")
        for i in self.__rows:
            buf.write(" " + i.__str__())
        return buf.getvalue()

    def __repr__(self):
        return self.__str__()

    def __getitem__(self, idx):
        return self.__rows[idx]

    def __iter__(self):
        for i in self.__rows:
            yield i

    def _append(self, el):
        self.__rows.append(el)

    def _grp_index(self):
        return self.__grp_idx

    def _values(self):
        return self.__rows
