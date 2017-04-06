# __author__ = 'Simon Dirmeier'
# __email__  = 'simon.dirmeier@bsse.ethz.ch'
# __date__   = 06.04.17

from dataframe import DataFrame
from sklearn import datasets
import re

iris_data = datasets.load_iris()
features = [re.sub("\s|cm|\(|\)", "", x) for x in iris_data.feature_names]

data = {features[i]: iris_data.data[:, i] for i in
        range(len(iris_data.data[1, :]))}
data["target"] = iris_data.target
frame = DataFrame(**data)


def group(*args, **kwargs):
    if args and issubclass(args[0], DataFrame):
        return args[0].group(*args[1:])
    elif issubclass(args[0], DataFrame):
        raise ValueError("todo")
    else:
        return ChainableGroup(*args)


class ChainableGroup:
    """
    Class that allows chaining of methods.

    """

    def __init__(self, *args):
        """
        Constructor for chainable.

        :param func: the function to be called
        :param args: tuple of params        
        """
        self.__df = args[0]

    def __call__(self, *args):
        return self.__df.group(*args)

    def __rshift__(self, other):
        return 1


k = group(frame, "target")
print(k)
k = frame >> group("target")
print(k)
