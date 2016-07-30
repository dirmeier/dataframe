# @author = 'Simon Dirmeier'
# @email = 'rafstraumur@simon-dirmeier.net'

import unittest
from pytab import Table


class TestTable(unittest.TestCase):
    def setUp(self):
        unittest.TestCase.setUp(self)
        self.__table = Table(a=[1, 2, 3], b=["a", "b", "c"])
        self.__selected = self.__table.select("a")

    def test_nrow(self):
        assert self.__table.nrow() == 3

    def test_ncol(self):
        assert self.__table.ncol() == 2

    def test_colnames(self):
        assert self.__table.colnames() == ["a", "b"]

    def test_select_nrow(self):
            assert self.__selected.nrow() == 3

    def test_select_ncol(self):
        assert self.__selected.ncol() == 1

    def test_selected_colnames(self):
        assert self.__selected.colnames() == ["a"]
