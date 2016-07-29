# @author = 'Simon Dirmeier'
# @email = 'rafstraumur@simon-dirmeier.net'


class SearchTreeNode:
    def __init__(self, id):
        self.__id = id
        self.__children = set()
        self.__value = -1

    def __eq__(self, other):
        if isinstance(other, SearchTreeNode):
            return self.__value == other.__value
        return False

    def value(self, val=None):
        if val is not None:
            self.__value = val
        return self.__value

    def add_child(self, node):
        self.__children.add(node)

    def has_child(self, val):
        return val in self.__children
