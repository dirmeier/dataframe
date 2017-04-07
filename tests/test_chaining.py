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


from dataframe import DataFrame
from sklearn import datasets
import re
from dataframe import chainable

iris_data = datasets.load_iris()
features = [re.sub("\s|cm|\(|\)", "", x) for x in iris_data.feature_names]

data = {features[i]: iris_data.data[:,i] for i in range(len(iris_data.data[1,:]))}
data["target"] = iris_data.target
frame = DataFrame(**data)

print(frame)

fg = frame.group("target")

class Bla:
    def __init__(self, x):
        self.x = x

    def __ror__(self, other):
        return other.x < self.x


a = Bla(1)
b = Bla(2)

print(a | b