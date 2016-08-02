# @author = 'Simon Dirmeier'
# @email = 'rafstraumur@simon-dirmeier.net'
import numpy
from pytab.search_tree.search_tree import SearchTree


class GroupedTable:
    def __init__(self, obj, *args):
        self.__search_col_idx = obj._which_colnames(*args)
        self.__search_tree = SearchTree()
        self.__group_idxs = numpy.zeros(obj.nrow()).astype(int)
        self.__grouping = {}
        self.__group_by(obj)

    def __iter__(self):
        for k, v in self.__grouping.items():
            yield k, v

    def __group_by(self, obj):
        for row in obj:
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
    def __init__(self, idx):
        self.__idx = idx
        self.__rows = []

    def append(self, el):
        self.__rows.append(el)

    def __str__(self):
        pass
