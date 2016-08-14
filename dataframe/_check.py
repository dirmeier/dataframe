# @author = 'Simon Dirmeier'
# @email = 'rafstraumur@simon-dirmeier.net'

import dataframe


def is_callable(f):
    if not issubclass(f, dataframe.Callable):
        raise TypeError("f must be subclass of Callable!")
    return True

def is_none(val):
    if val is None:
        raise TypeError("None detected")
    return False

def has_elements(*args):
    if not args:
        raise ValueError("No elements found!")
    return True

def disjoint(set1, set2):
    for el in set2:
        if el in set1:
            raise ValueError("Cannot aggregate grouping variable(s)!")
    return True
