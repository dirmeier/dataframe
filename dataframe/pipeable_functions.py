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
    Pipeable grouping method.

    Takes either
      - a dataframe and a tuple of strings for grouping,
      - a tuple of strings if a dataframe has already been piped into.
    
    :Example:
        
    group(dataframe, "column")
    
    :Example:
    
    dataframe >> group("column")
    
    :param args: tuple of arguments
    :type args: tuple
    :return: returns a grouped dataframe object
    :rtype: GroupedDataFrame
    """

    if args and isinstance(args[0], dataframe.DataFrame):
        return args[0].group(*args[1:])
    elif not args:
        raise ValueError("No arguments provided")
    else:
        return pipeable.Pipeable(pipeable.PipingMethod.GROUP, *args)


def aggregate(*args):
    """
    Pipeable aggregation method.
    
    Takes either 
     - a dataframe and a tuple of arguments required for aggregation,
     - a tuple of arguments if a dataframe has already been piped into.
    In any case one argument has to be a class that extends callable.

    :Example:

    aggregate(dataframe, Function, "new_col_name", "old_col_name")

    :Example:

    dataframe >> aggregate(Function, "new_col_name", "old_col_name")

    :param args: tuple of arguments
    :type args: tuple
    :return: returns a dataframe object
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
    Pipeable subsetting method.

    Takes either
     - a dataframe and a tuple of arguments required for subsetting,
     - a tuple of arguments if a dataframe has already been piped into.

    :Example:
        
    subset(dataframe, "column")
    
    :Example:
    
    dataframe >> subset("column")

    :param args: tuple of arguments
    :type args: tuple
    :return: returns a dataframe object
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
    Pipeable modification method 
    
    Takes either 
     - a dataframe and a tuple of arguments required for modification,
     - a tuple of arguments if a dataframe has already been piped into.
    In any case one argument has to be a class that extends callable.

    :Example:

    modify(dataframe, Function, "new_col_name", "old_col_name")
    
    :Example:

    dataframe >> modify(Function, "new_col_name", "old_col_name")

    :param args: tuple of arguments
    :type args: tuple
    :return: returns a dataframe object
    :rtype: DataFrame
    """

    if args and isinstance(args[0], dataframe.DataFrame):
        return args[0].modify(args[1], args[2], *args[3:])
    elif not args:
        raise ValueError("No arguments provided")
    else:
        return pipeable.Pipeable(pipeable.PipingMethod.MODIFY, *args)
