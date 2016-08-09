# @author = 'Simon Dirmeier'
# @email = 'rafstraumur@simon-dirmeier.net'

import unittest

from dataframe.dataframe import DataFrame


class TestGroup(unittest.TestCase):
    def setUp(self):
        unittest.TestCase.setUp(self)
        self.__table = DataFrame(a=[1, 2, 3, 1, 2, 3],
                             b=["a", "b", "c", "c", "a", "b"],
                             c=["x", "x", "x", "x", "x", "x"])

    def test_grp_size(self):
        tab = self.__table.group("a")
        assert len(tab._groups()) == 3

    def test_grp_elems(self):
        tab = self.__table.group("a")
        v = tab.__iter__().__next__()
        assert len(v._values()) == 2