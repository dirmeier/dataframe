# dataframe: a data-frame implementation using method piping
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


from enum import Enum
import dataframe

from ._piping_exception import PipingException


class PipingMethod(Enum):
    GROUP = 0
    MODIFY = 1
    AGGREGATE = 2
    SUBSET = 3


class Pipeable:
    """
    Class that allows piping of methods.     

    """

    def __init__(self, piping_method, *args):
        """
        Constructor for chainable. Takes a tuple which is either a dataframe
        and column names to group by or only the column names

        :param args: tuple of params
        """

        self.__piping_method = piping_method
        if args and isinstance(args[0], dataframe.DataFrame):
            raise PipingException("Wrong instantiation.")
        elif not args:
            raise ValueError("No arguments provided.")
        else:
            self.__args = args

    def __rrshift__(self, other):
        if self.__piping_method == PipingMethod.GROUP:
            return other.group(*self.__args)
        if self.__piping_method == PipingMethod.AGGREGATE:
            return other.aggregate(self.__args[0],
                                   self.__args[1],
                                   *self.__args[2:])
        if self.__piping_method == PipingMethod.SUBSET:
            return other.subset(*self.__args)
        if self.__piping_method == PipingMethod.MODIFY:
            return other.modify(self.__args[0],
                                self.__args[1],
                                *self.__args[2:])
        raise PipingException("Error when executing pipe.")
