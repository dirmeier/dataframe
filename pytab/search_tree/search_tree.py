# @author = 'Simon Dirmeier'
# @email = 'rafstraumur@simon-dirmeier.net'

from pytab.search_tree.search_tree_node import SearchTreeNode


class SearchTree:
    def __init__(self):
        self.__grp_idx = 0
        self.__root = SearchTreeNode(None)

    def find(self, *args):
        curr_node = self.__root
        return self.__traverse(curr_node, 0,  *args)

    def __traverse(self, curr_node, idx,  *args):
        key = args[idx]
        if not curr_node.has_child(key):
                child = SearchTreeNode(key)
                curr_node.add_child(child)
        if idx == len(args) - 1:
            curr_node = curr_node.get_child(key)
            if curr_node.get_value() == -1:
                curr_node.set_value(self.idx())
            return curr_node.get_value()
        else:
            return self.__traverse(curr_node.get_child(key), idx + 1, *args)

    def idx(self):
        self.__grp_idx += 1
        return self.__grp_idx




