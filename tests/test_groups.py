# @author = 'Simon Dirmeier'
# @email = 'rafstraumur@simon-dirmeier.net'

# @author = 'Simon Dirmeier'
# @email = 'rafstraumur@simon-dirmeier.net'

import unittest
from nose.tools import raises
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

class TestGroupedDataFrame(unittest.TestCase):
    def setUp(self):
        unittest.TestCase.setUp(self)
        self.__table = DataFrame(a=list(range(30)), b=["a", "b", "c"] * 10).group("b")

    @raises(TypeError)
    def test_aggregate(self):
        self.__table.aggregate(Mean, "c",  "aa")

