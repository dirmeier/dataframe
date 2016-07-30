# @author = 'Simon Dirmeier'
# @email = 'rafstraumur@simon-dirmeier.net'

from pytab.search_tree.search_tree import SearchTree
import numpy

class TableGrouping:
    def __init__(self, n):
        self.__search_tree = SearchTree()
        self.__groups = numpy.zeros(n)
        self.__grouping = {}

    def __add_grp(self, row, *args):
        grp_idx = self.__search_tree.find(*args)
        self.__groups[row.idx()] = grp_idx
        if grp_idx not in self.__grouping:
            self.__grouping[grp_idx] = set()
        self.__grouping[grp_idx].add(row)

    @staticmethod
    def group_by(obj, *args):
        grp = TableGrouping(obj.nrow())
        for row in obj:
            grp.__add_grp(row, *args)
        return grp.__groups, grp.__grouping


