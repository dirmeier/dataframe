# @author = 'Simon Dirmeier'
# @email = 'rafstraumur@simon-dirmeier.net'

from abc import ABCMeta, abstractmethod


class Table(metaclass=ABCMeta):
    @abstractmethod
    def subset(self):
        pass

    @abstractmethod
    def group(self, *args):
        pass

    @abstractmethod
    def aggregate(self):
        pass

    @abstractmethod
    def modify(self, f, new_col, *args):
        pass

