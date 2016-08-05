# @author = 'Simon Dirmeier'
# @email = 'rafstraumur@simon-dirmeier.net'

import unittest
import collections
from pytab import TableRow, table_abstract

class TestRow(unittest.TestCase):
    def setUp(self):
        unittest.TestCase.setUp(self)
        self.compare = lambda x, y: collections.Counter(x) == collections.Counter(y)
        self.__table = table_abstract(a=[1, 2, 3], b=["a", "b", "c"])
        self.__row = TableRow(1, [1, 2, 3], self.__table._colnames())

    def test_idx(self):
        assert self.__row.idx() == 1

    def test_vals(self):
        assert self.__row.values() == [1, 2, 3]

    def test_hash(self):
        s = set()
        s.add(self.__row)
        assert self.__row in s

    def test_set(self):
        s = set()
        s.add(self.__row)
        s.add(TableRow(1, [1, 2, 3], self.__table._colnames()))
        assert len(s) == 1

    def test_eq(self):
        r1 = TableRow(1, [1, 2, 3], self.__table._colnames())
        assert self.__row == r1

    def test_iter(self):
        itr = self.__table.__iter__()
        row = itr.__next__()
        assert row.idx() == 0 and self.compare(row._values(), [1, "a"])