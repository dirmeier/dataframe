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
        self.__table = dataframe.DataFrame(a=list(range(30)),
                                           b=["a", "b", "c"] * 10).group("b")

    def test_callable_error(self):
        with pytest.raises(TypeError):
            self.__table.aggregate(C, "const", "a")

    def test_is_eone_error(self):
        with pytest.raises(TypeError):
            self.__table.aggregate(D, None, "a")

    def test_has_elems_error(self):
        with pytest.raises(ValueError):
            self.__table.aggregate(D, "c")
