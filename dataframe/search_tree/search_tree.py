# @author = 'Simon Dirmeier'
# @email = 'rafstraumur@simon-dirmeier.net'

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
            if curr_node.get_value() == -1:
                curr_node.set_value(self.idx())
            return curr_node.get_value()
        else:
            return self.__traverse(curr_node.get_child(key), idx + 1, *args)

    def idx(self):
        """
        Getter and incrementer for idx. Increases the current index by one and returns it.

        :return: returns the current index
        """
        self.__grp_idx += 1
        return self.__grp_idx




