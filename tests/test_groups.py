# @author = 'Simon Dirmeier'
# @email = 'rafstraumur@simon-dirmeier.net'

# @author = 'Simon Dirmeier'
# @email = 'rafstraumur@simon-dirmeier.net'
from collections import Counter
import unittest
import pytest
import dataframe
from statistics import mean


class Mean(dataframe.Callable):
    def __call__(self, *args):
        vals = args[0].values()
        return mean(vals)


class Exp(dataframe.Callable):
    def __call__(self, *args):
        vals = args[0].values()
        a = map(lambda x: x * x, vals)
        return list(a)


class TestGroupedDataFrame(unittest.TestCase):
    def setUp(self):
        unittest.TestCase.setUp(self)
        self.__table = dataframe.DataFrame(a=list(range(30)), b=["a", "b", "c"] * 10).group("b")

    def test_aggregate_error(self):
        with pytest.raises(TypeError):
            self.__table.aggregate(Mean, "c", "aa")

    def test_aggregate(self):
        a = self.__table.aggregate(Mean, "mean", "a")
        assert Counter(a["mean"]) == Counter([13.5, 14.5, 15.5])

    def test_subset_ncol(self):
        a = self.__table.subset("b")
        assert a.ungroup().ncol() == 1

    def test_selected_colnames(self):
        assert self.__table.subset("b").colnames() == ["b"]

    def test_modify(self):
        a = self.__table.modify(Exp, "mean", "a")
        for i in a:
            assert (i["mean"][0] == i["a"][0] ** 2)

    def test_group(self):
        a = self.__table.group("a")
        assert len(a.groups()) == 30

    def test_group_error(self):
        with pytest.raises(ValueError):
            self.__table.group("as")
