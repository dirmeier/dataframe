# @author = 'Simon Dirmeier'
# @email = 'rafstraumur@simon-dirmeier.net'


class SearchTreeNode:
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

    def get_value(self):
        return self.__value

    def set_value(self, val):
        self.__value = val

    def add_child(self, node):
        self.__children[node.__id] = node

    def has_child(self, val):
        return val in self.__children

    def get_child(self, nid):
        return self.__children[nid]
