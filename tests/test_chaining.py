# __author__ = 'Simon Dirmeier'
# __email__  = 'simon.dirmeier@bsse.ethz.ch'
# __date__   = 06.04.17

from dataframe import DataFrame
from sklearn import datasets
import re
from dataframe import Chainable

iris_data = datasets.load_iris()
features = [re.sub("\s|cm|\(|\)", "", x) for x in iris_data.feature_names]

data = {features[i]: iris_data.data[:,i] for i in range(len(iris_data.data[1,:]))}
data["target"] = iris_data.target
frame = DataFrame(**data)

print(frame)

fg = frame.group("target")


chain(DataFrame)