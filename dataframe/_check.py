# @author = 'Simon Dirmeier'
# @email = 'rafstraumur@simon-dirmeier.net'

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
    :param warn: the error message that should be thrown when the sets are NOT disjoint
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
    :param warn: the error message that should be thrown when the sets are not containd
    :return: returns true if all values of set2 are in set1
    """
    for elem in set2:
        if elem not in set1:
            raise ValueError(warn)
    return True
