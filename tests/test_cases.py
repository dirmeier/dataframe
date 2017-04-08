# __author__ = 'Simon Dirmeier'
# __email__  = 'simon.dirmeier@bsse.ethz.ch'
# __date__   = 08.04.17


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
frame = dataframe.DataFrame(**data)

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

k = frame >> \
     group("target") >> \
     modify(Zscore, "z", "petalwidth") >> \
     subset("z") >> \
     aggregate(Mean, "m", "z")

print(k)