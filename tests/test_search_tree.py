# __author__ = 'Simon Dirmeier'
# __email__  = 'simon.dirmeier@bsse.ethz.ch'
# __date__   = 29/07/16

import unittest
from dataframe.search_tree import SearchTree


class TestSearchTree(unittest.TestCase):
    def setUp(self):
        unittest.TestCase.setUp(self)
        self.tree = SearchTree()
        self.tree.find(1, 2)
        self.tree.find(13, 7)
        self.tree.find(2, 3)
        self.tree.find(1, 3)
        self.tree.find(2, 3)
        self.tree.find(2, 4)
        self.tree.find(1, 4)

    def test_insert(self):
        self.assertEquals(self.tree.find(1, 2), 0)

    def test_insert_error(self):
        self.assertNotEqual(self.tree.find(1, 2), 2)