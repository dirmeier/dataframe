# @author = 'Simon Dirmeier'
# @email = 'rafstraumur@simon-dirmeier.net'

import unittest
from dataframe.dataframe_dataframe import DataFrame
from dataframe.dataframe_grouped_dataframe import GroupedDataFrame
from dataframe import Callable
from statistics import mean
import scipy.stats as sps


class Mean(Callable):
    def __call__(self, *args):
        vals = args[0].values()
        return mean(vals)


class Zscore(Callable):
    def __call__(self, *args):
        vals = args[0].values()
        return sps.zscore(vals).tolist()


class TestDataFrame(unittest.TestCase):
    def setUp(self):
        unittest.TestCase.setUp(self)
        self.__table = DataFrame(a=[1, 2, 3] * 10, b=["a", "b", "c"] * 10)
        self.__selected = self.__table.subset("a")

    def test_nrow(self):
        self.assertEquals(self.__table.nrow(), 30)

    def test_ncol(self):
        self.assertEquals(self.__table.ncol(), 2)

    def test_colnames(self):
        self.assertEquals(self.__table.colnames(), ["a", "b"])

    def test_select_nrow(self):
        self.assertEquals(self.__selected.nrow(), 30)

    def test_select_ncol(self):
        self.assertEquals(self.__selected.ncol(), 1)

    def test_selected_colnames(self):
        self.assertEquals(self.__selected.colnames(), ["a"])

    def test_grouping_class(self):
        gr = self.__table.group("a")
        self.assertTrue(isinstance(gr, GroupedDataFrame))

    def test_grp_size(self):
        tab = self.__table.group("a")
        self.assertEquals(len(tab.groups()), 3)

    def test_aggregate(self):
        v = self.__table.aggregate(Mean, "mean", "a")
        self.assertEquals(v["mean"][0], 2)

    def test_modify(self):
        v = self.__table.modify(Zscore, "zsc", "a")
        self.assertEquals(v["zsc"][1], 0)

    def test_modify(self):
        v = self.__table.modify(Zscore, "zsc", "a")
        self.assertEquals(v["zsc"][1], 0)
