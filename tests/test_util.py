# @author = 'Simon Dirmeier'
# @email = 'rafstraumur@simon-dirmeier.net'

import unittest
import pytest
import dataframe


class C:
    def __call__(self, *args):
        return 1

class D(dataframe.Callable):
    def __call__(self, *args):
        return 1

class TestUtil(unittest.TestCase):
    def setUp(self):
        unittest.TestCase.setUp(self)
        self.__table = dataframe.DataFrame(a=list(range(30)), b=["a", "b", "c"] * 10).group("b")

    def test_callable_error(self):
        with pytest.raises(TypeError):
            self.__table.aggregate(C, "const", "a")

    def test_is_eone_error(self):
        with pytest.raises(TypeError):
            self.__table.aggregate(D, None, "a")

    def test_has_elems_error(self):
        with pytest.raises(TypeError):
            self.__table.aggregate(D, "c")
