# __author__ = 'Simon Dirmeier'
# __email__  = 'simon.dirmeier@bsse.ethz.ch'
# __date__   = 29/07/16

import unittest

from pytab.search_tree.search_tree import SearchTree


class TestSearchTree(unittest.TestCase):
    def test_insert(self):
        tree = SearchTree()
        tree.find(1, 2)
        tree.find(13, 7)
        tree.find(2, 3)
        tree.find(1, 3)
        tree.find(2, 3)
        tree.find(2, 4)
        tree.find(1, 4)
        assert(tree.find(1, 2) == 1)
