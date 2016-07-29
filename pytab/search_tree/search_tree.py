# @author = 'Simon Dirmeier'
# @email = 'rafstraumur@simon-dirmeier.net'

from pytab.search_tree.search_tree_node import SearchTreeNode


class SearchTree:
    def __init__(self):
        self.__grp_idx = 0
        self.__root = SearchTreeNode()

    def find(self, *args):
        curr_node = self.__root
        self.__traverse(curr_node, 0,  *args)

    def __traverse(self, curr_node, idx,  *args):
        key = args[idx]
        if curr_node.has_child(args[idx]):
            if idx == len(args) - 1:
                return curr_node.child(args[idx]).value()
            else:
                curr_node = curr_node.child(args[idx])
                self.__traverse(curr_node, idx + 1, args)
        else:
            child = SearchTreeNode(key)
            curr_node.add_child(child)
            if idx == len(args) - 1:
                child.value(self.__idx())
                return child.value()
            else:
                self.__traverse(child, idx + 1, args)

    def __idx(self):
        self.__idx += 1
        return self.__idx


