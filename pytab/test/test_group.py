# @author = 'Simon Dirmeier'
# @email = 'rafstraumur@simon-dirmeier.net'

import unittest
from pytab import Table

class TestGroup(unittest.TestCase):
    def setUp(self):
        unittest.TestCase.setUp(self)
        self.__table = Table(a=[1, 2, 3, 1, 2, 3],
                             b=["a", "b", "c", "c", "a", "b"],
                             c=["x", "x", "x", "x", "x", "x"])

    def test_grp(self):
        tab = self.__table.group_by("a")
        for k, v in tab:
            print(k, v)
            for a in v:
                print(a)
            print("")

