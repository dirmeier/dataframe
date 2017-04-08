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
from dataframe import pipeable


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

    if args and isinstance(args[0], dataframe.DataFrame):
        return args[0].group(*args[1:])
    elif not args:
        raise ValueError("No arguments provided")
    else:
        return pipeable.Pipeable(pipeable.PipingMethod.GROUP, *args)


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
    elif not args:
        raise ValueError("No arguments provided")
    else:
        return pipeable.Pipeable(pipeable.PipingMethod.AGGREGATE, *args)


def subset(*args):
    """
    Chainable subset method. Takes either a dataframe and a list of 
    arguments required for aggregation or only the latter if a 
    dataframe has already been piped into.

    :param args: tuple of arguments
    :type args: tuple of (DataFrame, clazz, str, ...) or tuple of (clazz, str, 
    ...)
    :return: returns a dataframe
    :rtype: DataFrame
    """

    if args and isinstance(args[0], dataframe.DataFrame):
        return args[0].subset(*args[1:])
    elif not args:
        raise ValueError("No arguments provided")
    else:
        return pipeable.Pipeable(pipeable.PipingMethod.SUBSET, *args)


def modify(*args):
    """
    Chainable subset method. Takes either a dataframe and a list of 
    arguments required for aggregation or only the latter if a 
    dataframe has already been piped into.

    :param args: tuple of arguments
    :type args: tuple of (DataFrame, clazz, str, ...) or tuple of (clazz, str, 
    ...)
    :return: returns a dataframe
    :rtype: DataFrame
    """

    if args and isinstance(args[0], dataframe.DataFrame):
        return args[0].modify(args[1], args[2], *args[3:])
    elif not args:
        raise ValueError("No arguments provided")
    else:
        return pipeable.Pipeable(pipeable.PipingMethod.MODIFY, *args)
