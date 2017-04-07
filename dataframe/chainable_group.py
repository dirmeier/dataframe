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


from dataframe import DataFrame


def group(*args):
    """
    Chainable group method. Takes either a dataframe and a list of strings for
    grouping or only a list of strings if a dataframe has already been piped
    into.
    
    :param args: tuple of arguments
    :type args: tuple of (DataFrame, str, str, ...) or tuple of (str, str, ...)
    :return: returns a grouped dataframe
    :rtype: DataFrame
    """

    if args and isinstance(args[0], DataFrame):
        return args[0].group(*args[1:])
    else:
        return ChainableGroup(*args)


class ChainableGroup:
    """
    Class that allows chaining of methods. 

    """

    def __init__(self, *args):
        """
        Constructor for chainable. Takes a tuple which is either a dataframe
        and column names to group by or only the column names
        
        :param args: tuple of params
        """
        if args and isinstance(args[0], DataFrame):
            self.__df = args[0]
        else:
            self.__args = args

    def __call__(self, *args):
        return self.__df.group(*args)

    def __rrshift__(self, other):
        return other.group(*self.__args)
