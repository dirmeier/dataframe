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

from collections import Counter
import unittest
import pytest
import dataframe
from statistics import mean


class Mean(dataframe.Callable):
    def __call__(self, *args):
        vals = args[0].values
        return mean(vals)


class Exp(dataframe.Callable):
    def __call__(self, *args):
        vals = args[0].values
        a = map(lambda x: x * x, vals)
        return list(a)


class TestGroupedDataFrame(unittest.TestCase):
    def setUp(self):
        unittest.TestCase.setUp(self)
        self.__table = dataframe.DataFrame(a=list(range(30)),
                                           b=["a", "b", "c"] * 10).group("b")

    def test_aggregate_error(self):
        with pytest.raises(TypeError):
            self.__table.aggregate(Mean, "c", "aa")

    def test_aggregate(self):
        a = self.__table.aggregate(Mean, "mean", "a")
        assert Counter(a["mean"]) == Counter([13.5, 14.5, 15.5])

    def test_subset_ncol(self):
        a = self.__table.subset("b")
        assert a.ungroup().ncol == 1

    def test_selected_colnames(self):
        assert self.__table.subset("b").colnames == ["b"]

    def test_modify(self):
        a = self.__table.modify(Exp, "mean", "a")
        for i in a:
            assert (i["mean"][0] == i["a"][0] ** 2)

    def test_group(self):
        a = self.__table.group("a")
        assert len(a.groups) == 30

    def test_group_error(self):
        with pytest.raises(ValueError):
            self.__table.group("as")
