# @author = 'Simon Dirmeier'
# @email = 'rafstraumur@simon-dirmeier.net'

import unittest
import collections
from dataframe.dataframe import DataFrame
from dataframe.dataframe_row import DataFrameRow


class TestRow(unittest.TestCase):
    def setUp(self):
        unittest.TestCase.setUp(self)
        self.compare = lambda x, y: collections.Counter(x) == collections.Counter(y)
        self.__table = DataFrame(a=[1, 2, 3], b=["a", "b", "c"])
        self.__row = DataFrameRow(1, [1, 2, 3], self.__table._colnames())

