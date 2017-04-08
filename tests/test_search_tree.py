# dataframe: a data-frame implementation using method piping
#
# Copyright (C) 2016 Simon Dirmeier
#
# This file is part of dataframe.
#
# dataframe is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# dataframe is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with dataframe. If not, see <http://www.gnu.org/licenses/>.
#
#
# @author = 'Simon Dirmeier'
# @email = 'mail@simon-dirmeier.net'


import unittest
import pytest
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
        assert self.tree.find(1, 2) == 0

    def test_insert_error(self):
        with pytest.raises(AssertionError):
            assert self.tree.find(1, 2) == 1

