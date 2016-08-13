# @author = 'Simon Dirmeier'
# @email = 'rafstraumur@simon-dirmeier.net'

# @author = 'Simon Dirmeier'
# @email = 'rafstraumur@simon-dirmeier.net'
from collections import Counter

import unittest
import pytest
from dataframe.dataframe_dataframe import DataFrame
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

class TestGroupedDataFrame(unittest.TestCase):
    def setUp(self):
        unittest.TestCase.setUp(self)
        self.__table = DataFrame(a=list(range(30)), b=["a", "b", "c"] * 10).group("b")

    def test_aggregate_error(self):
        with pytest.raises(TypeError):
            self.__table.aggregate(Mean, "c",  "aa")

    def test_aggregate(self):
        a = self.__table.aggregate(Mean, "c",  "a")
        assert Counter(a["c"]) == Counter([13.5, 14.5, 15.5])

    def test_modify(self):
        #a = self.__table.modify(Zscore, "ysc", "a")
        print(1)

