# @author = 'Simon Dirmeier'
# @email = 'rafstraumur@simon-dirmeier.net'
from dataframe._callable import Callable


def _is_callable(f):
    if not issubclass(f, Callable):
        raise TypeError("f must be subclass of Callable!")
    return True

def _is_none(val):
    if val is None:
        raise TypeError("None detected")
    return False

def _has_elements(*args):
    if not args:
        raise ValueError("No elements found!")
    return True