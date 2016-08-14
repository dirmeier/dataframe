# __author__ = 'Simon Dirmeier'
# __email__  = 'simon.dirmeier@bsse.ethz.ch'
# __date__   = 29/07/16

import unittest
import pytest
import dataframe

class TestSearchTree(unittest.TestCase):
    def setUp(self):
        unittest.TestCase.setUp(self)
        self.tree = dataframe.SearchTree()
        self.tree.find(1, 2)
        self.tree.find(13, 7)
        self.tree.find(2, 3)
        self.tree.find(1, 3)
        self.tree.find(2, 3)
        self.tree.find(2, 4)
        self.tree.find(1, 4)

    def test_insert(self):
        assert self.tree.find(1, 2) == 0

    def test_insert_error(self):
        with pytest.raises(AssertionError):
            assert self.tree.find(1, 2) == 1

