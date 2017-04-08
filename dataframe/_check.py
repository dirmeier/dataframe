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


import dataframe


def is_callable(func):
    """
    Check if a function extends callable.

    :param func: the function to be checked
    :return: returns true if the function is callable
    """
    if not issubclass(func, dataframe.Callable):
        raise TypeError("f must be subclass of Callable!")
    return True


def is_none(val):
    """
    Check if a value is None.

    :param val: the value to be tested
    :return: returns false if the value is not none
    """
    if val is None:
        raise TypeError("None detected")
    return False


def has_elements(*args):
    """
    Check if args has elements.

    :param args: a tuple
    :return: returns true if args has elements
    """
    if not args:
        raise ValueError("No elements found!")
    return True


def is_disjoint(set1, set2, warn):
    """
    Checks if elements of set2 are in set1.

    :param set1: a set of values
    :param set2: a set of values
    :param warn: the error message that should be thrown
     when the sets are NOT disjoint
    :return: returns true no elements of set2 are in set1
    """
    for elem in set2:
        if elem in set1:
            raise ValueError(warn)
    return True


def contains_all(set1, set2, warn):
    """
    Checks if all elements from set2 are in set1.

    :param set1:  a set of values
    :param set2:  a set of values
    :param warn: the error message that should be thrown 
     when the sets are not containd
    :return: returns true if all values of set2 are in set1
    """
    for elem in set2:
        if elem not in set1:
            raise ValueError(warn)
    return True
