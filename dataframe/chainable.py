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


class Chainable:
    """
    Class that allows chaining of methods.

    """

    def __init__(self, func, args=(), kwargs=None, minargs=None):
        """
        Constructor for chainable.

        :param func: the function to be called
        :param args: tuple of params
        :param kwargs: dictionary of named params
        """
        self.__func = func
        self.__args = args
        self.__kwargs = kwargs
        self.__minargs = minargs

    def __call__(self, *args, **kwargs):
        if args or kwargs:
            new_args = self.__args + args
            new_kwargs = dict.copy(self.__kwargs)
            new_kwargs.update(kwargs)
            # Evaluate function
            if self.__minargs is not None and \
               self.__minargs <= len(new_args) + len(new_kwargs):
                return self.__func(*new_args, **new_kwargs)
            # create new chainable
            else:
                return Chainable(self.__func,
                                 new_args,
                                 new_kwargs,
                                 self.__minargs)
        # do call
        else:
            return self.__func(*self.__args, **self.__kwargs)

    def __ror__(self, arg):
        return self.__func(*(self.__args + (arg,)), **self.__kwargs)


def chain(func, min_args=None):
    """
    Definition for chainable functions.

    :param func: function to be made chainable
    :param min_args: minimal arguments of the function
    :return: returns the function as chainable function
    """
    return Chainable(func, (), {}, min_args)
