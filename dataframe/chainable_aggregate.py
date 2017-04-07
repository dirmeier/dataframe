# __author__ = 'Simon Dirmeier'
# __email__  = 'simon.dirmeier@bsse.ethz.ch'
# __date__   = 07.04.17

# dataframe: an efficient data-frame implementation in python
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


import dataframe
from ._piping_exception import PipingException
from sklearn import datasets
import re

iris_data = datasets.load_iris()
features = [re.sub("\s|cm|\(|\)", "", x) for x in iris_data.feature_names]

data = {features[i]: iris_data.data[:, i] for i in
        range(len(iris_data.data[1, :]))}
data["target"] = iris_data.target
frame = DataFrame(**data)


def aggregate(*args):
    """
    Chainable aggregation method. Takes either a dataframe and a list of 
    arguments required for aggregation or only the latter if a 
    dataframe has already been piped into.

    :param args: tuple of arguments
    :type args: tuple of (DataFrame, clazz, str, ...) or tuple of (clazz, str, 
    ...)
    :return: returns a dataframe
    :rtype: DataFrame
    """

    if args and isinstance(args[0], dataframe.DataFrame):
        return args[0].aggregate(args[1], args[2], *args[3:])
    else:
        return ChainableAggregate(*args)


class ChainableAggregate:
    """
    Class that allows chaining of methods. 

    """

    def __init__(self, *args):
        """
        Constructor for chainable. Takes a tuple which is either a dataframe
        and column names to group by or only the column names

        :param args: tuple of params
        """
        if args and isinstance(args[0], dataframe.DataFrame):
            raise PipingException("Wrong instantiation")
        else:
            self.__args = args

    def __call__(self, *args):
        return self.__df.group(*args)

    def __rrshift__(self, other):
        return other.group(*self.__args)


k = group(frame, "target")
print(k)
k = frame >> group("target")
print(k)