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
import dataframe
import scipy.stats as sps
from dataframe import Callable
from statistics import mean


class Mean(Callable):
    def __call__(self, *args):
        vals = args[0].values
        return mean(vals)


class Zscore(Callable):
    def __call__(self, *args):
        vals = args[0].values
        return sps.zscore(vals).tolist()


class TestDataFrame(unittest.TestCase):
    def setUp(self):
        unittest.TestCase.setUp(self)
        self.__table = dataframe.DataFrame(a=[1, 2, 3] * 10,
                                           b=["a", "b", "c"] * 10)
        self.__selected = self.__table.subset("a")

    def test_nrow(self):
        assert self.__table.nrow == 30

    def test_ncol(self):
        assert self.__table.ncol == 2

    def test_colnames(self):
        assert self.__table.colnames == ["a", "b"]

    def test_select_nrow(self):
        assert self.__selected.nrow == 30

    def test_select_ncol(self):
        assert self.__selected.ncol == 1

    def test_selected_colnames(self):
        assert self.__selected.colnames == ["a"]

    def test_grouping_class(self):
        gr = self.__table.group("a")
        assert isinstance(gr, dataframe.GroupedDataFrame)

    def test_grp_size(self):
        tab = self.__table.group("a")
        assert len(tab.groups) == 3

    def test_aggregate(self):
        v = self.__table.aggregate(Mean, "mean", "a")
        assert v["mean"][0] == 2

    def test_modify(self):
        v = self.__table.modify(Zscore, "zsc", "a")
        assert v["zsc"][1] == 0
