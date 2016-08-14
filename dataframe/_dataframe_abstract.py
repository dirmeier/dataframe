# @author = 'Simon Dirmeier'
# @email = 'rafstraumur@simon-dirmeier.net'

from abc import ABCMeta, abstractmethod


class ADataFrame(metaclass=ABCMeta):
    @abstractmethod
    def subset(self, *args):
        pass

    @abstractmethod
    def group(self, *args):
        pass

    @abstractmethod
    def aggregate(self, clazz, new_col, *args):
        pass

    @abstractmethod
    def modify(self, clazz, new_col, *args):
        pass

    @abstractmethod
    def colnames(self):
        pass
