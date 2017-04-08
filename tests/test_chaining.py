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
# @email = 'mail@simon-dirmeier.net'


import pytest
import unittest
import dataframe
import scipy.stats as sps
from dataframe import group, modify, subset, aggregate
from sklearn import datasets
from statistics import mean
import re


class Mean(dataframe.Callable):
    def __call__(self, *args):
        vals = args[0].values
        return mean(vals)


class Zscore(dataframe.Callable):
    def __call__(self, *args):
        vals = args[0].values
        return sps.zscore(vals).tolist()


class TestPipes(unittest.TestCase):
    def setUp(self):
        iris_data = datasets.load_iris()
        features = [re.sub("\s|cm|\(|\)", "", x) for x in
                    iris_data.feature_names]
        data = {features[i]: iris_data.data[:, i] for i in
                range(len(iris_data.data[1, :]))}
        data["target"] = iris_data.target
        self.__frame = dataframe.DataFrame(**data)

    def test_group_piped(self):
        tab = self.__frame >> group("target")
        assert len(tab.groups) == 3

    def test_group(self):
        tab = group(self.__frame, "target")
        assert len(tab.groups) == 3

    def test_group_double(self):
        tab = group(self.__frame, "target") >> group("petalwidth")
        assert isinstance(tab, dataframe.GroupedDataFrame)

    def test_aggregate(self):
        tab = aggregate(self.__frame, Mean, "mean", "petalwidth")
        assert len(tab["mean"]) == 1

    def test_aggregate_piped(self):
        tab = self.__frame >> aggregate(Mean, "mean", "petalwidth")
        assert len(tab["mean"]) == 1

    def test_group_aggregate(self):
        tab = self.__frame >> \
              group("target") >> \
              aggregate(Mean, "mean", "petalwidth")
        assert len(tab["mean"]) == 3

    def test_modify_piped(self):
        tab = self.__frame >> modify(Zscore, "z", "petalwidth")
        assert tab.nrow == self.__frame.nrow

    def test_modify(self):
        tab = modify(self.__frame, Zscore, "z", "petalwidth")
        assert tab.nrow == self.__frame.nrow

    def test_subset_piped(self):
        tab = self.__frame >> subset("petalwidth")
        assert tab.ncol == 1

    def test_subset(self):
        tab =  subset(self.__frame , "petalwidth")
        assert tab.ncol == 1

    def test_modify_subset(self):
        tab = modify(self.__frame, Zscore, "z", "target") >> \
              subset("z")
        assert tab.ncol == 1

    def test_modify_subset(self):
        tab = modify(self.__frame, Zscore, "z", "target") >> \
              subset("z")
        assert tab.ncol == 1

    def test_aggregate_subset(self):
        tab = aggregate(self.__frame, Mean, "m", "target") >> \
              subset("m")
        assert tab.nrow == 1

    def test_random_pipeing(self):
        tab = self.__frame >> \
                group("target") >> \
                modify(Zscore, "z", "petalwidth") >> \
                subset("z") >> \
                aggregate(Mean, "m", "z")
        assert tab.ncol == 2 and tab.nrow == 3

