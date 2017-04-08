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


class SearchTreeNode:
    """
    Class that represents a node in the search tree.

    """
    def __init__(self, nid):
        self.__id = nid
        self.__children = dict()
        self.__value = -1

    def __hash__(self):
        return hash(self.__id)

    def __eq__(self, other):
        if isinstance(other, SearchTreeNode):
            return self.__id == other.__id
        return False

    @property
    def get_value(self):
        """
        Getter for the value of the node.

        :return: returns the value of the node
        """
        return self.__value

    def set_value(self, val):
        self.__value = val

    def add_child(self, node):
        """
        Add a child to the node.

        :param node: the node to be added as child
        """
        self.__children[node.__id] = node

    def has_child(self, val):
        """
        Checks if the node has a child with a given value.

        :param val: value of the child to be tested
        :return: returns true if the node has the child with value val
        """
        return val in self.__children

    def get_child(self, nid):
        return self.__children[nid]
