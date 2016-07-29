# __author__ = 'Simon Dirmeier'
# __email__  = 'simon.dirmeier@bsse.ethz.ch'
# __date__   = 29/07/16

import unittest

from pytab.search_tree.search_tree import SearchTree


class TestSearchTree(unittest.TestCase):
    def test_insert(self):
        tree = SearchTree()
        val = tree.find(1, 1)
        assert(val == 1)
