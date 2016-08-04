# @author = 'Simon Dirmeier'
# @email = 'rafstraumur@simon-dirmeier.net'
from pytab._check import _is_table, _is_callable, _has_elements, _is_none
from pytab.callable import Callable


def modify(obj, f, new_col=None, *args):
    if _is_table(obj) and not _is_none(new_col) and _has_elements(*args):
        return _modify(obj, f, new_col, *args)

def _modify(obj, f, new_col, *args):
    if _is_callable(f):
        _do_modify(obj, f,  new_col, *args)
    return obj

def _do_modify(obj, f, new_col, *col_names):
    # TODO
    colval = obj[oc]
    if colval is None:
        return
    res = f()(colval)
    #if res.size != len(colval):
    #   raise ValueError("The function you provided yields an array of false length!")
   # obj._cbind(**{nc: colval})
    return res

import numpy as np

class s(Callable):
    def __call__(self, *args):
        return np.mean(args)

print (_do_modify({"a": np.array([1, 2,3, 4])}, s, "b", "a" ))