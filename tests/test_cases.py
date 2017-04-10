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


import pytest
import unittest
import dataframe
import scipy.stats as sps
from dataframe import group, modify, subset, aggregate
from sklearn import datasets
import re

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


iris_data = datasets.load_iris()
features = [re.sub("\s|cm|\(|\)", "", x) for x in
            iris_data.feature_names]
data = {features[i]: iris_data.data[:, i] for i in
        range(len(iris_data.data[1, :]))}
data["target"] = iris_data.target
frame = dataframe.DataFrame(**data) >> group("target")

print(frame)

# k = frame >> group("target")
# print(k)
#
# k = frame >> group("target") >> group("petalwidth")
# print(k)
#
# k = group(frame, "target")
# print(k)
#
# k = aggregate(frame, Mean, "mean", "petalwidth")
# print(k)
#
# k = frame >> aggregate(Mean, "mean", "petalwidth")
# print(k)
#
# k = frame >> group("target") >> aggregate(Mean, "mean", "petalwidth")
# print(k)
#
# k = frame >> group("target") >> modify(Zscore, "zscore", "petalwidth")
# print(k)
#
# k = group(frame, "target") >> modify(Zscore, "zscore", "petalwidth")
# print(k)
#
# k = modify(frame, Zscore, "zscore", "petalwidth")
# print(k)
#
# k = frame >> modify(Zscore, "zscore", "petalwidth")
# print(k)
#
# k = frame >> modify(Zscore, "zscore", "petalwidth") >> subset("zscore")
# print(k)
# print(k.ncol)

# k = frame >> subset("petalwidth")
# print(k)
#
# k = frame >> modify(Zscore, "zscore", "petalwidth") >> group("target") >> \
#        aggregate(Mean, "mz", "zscore")
# print(k)

# k = frame >> \
#      group("target") >> \
#      modify(Zscore, "z", "petalwidth") >> \
#      subset("z") >> \
#      aggregate(Mean, "m", "z")
#
# print(k)
# frame = dataframe.DataFrame(**data)
# k = frame.aggregate(Mean, "mean", "petallength")
#
# print(k)