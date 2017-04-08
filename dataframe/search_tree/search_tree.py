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


from .search_tree_node import SearchTreeNode


class SearchTree:
    """
    Implementation of an efficient tree-like recursive data-structure for indexing.

    """
    def __init__(self):
        self.__grp_idx = -1
        self.__root = SearchTreeNode(None)

    def find(self, *args):
        """
        Find a node in the tree. If the node is not found it is added first and then returned.

        :param args: a tuple
        :return: returns the node
        """
        curr_node = self.__root
        return self.__traverse(curr_node, 0,  *args)

    def __traverse(self, curr_node, idx,  *args):
        key = args[idx]
        if not curr_node.has_child(key):
                child = SearchTreeNode(key)
                curr_node.add_child(child)
        if idx == len(args) - 1:
            curr_node = curr_node.get_child(key)
            if curr_node.get_value == -1:
                curr_node.set_value(self.idx())
            return curr_node.get_value
        else:
            return self.__traverse(curr_node.get_child(key), idx + 1, *args)

    def idx(self):
        """
        Getter and incrementer for idx. Increases the current index by one and returns it.

        :return: returns the current index
        """
        self.__grp_idx += 1
        return self.__grp_idx




