# @author = 'Simon Dirmeier'
# @email = 'rafstraumur@simon-dirmeier.net'
from dataframe import DataFrame
from itertools import chain

x = DataFrame(a=list(range(10)),b=[1, 28880000] * 5).group("b")
print(x)
a = ['a', 'b', 'c', 3, 4, 'd', 6, 7, 8]
new_list = list(chain(a[0:2], [a[4]], a[6:]))
print(new_list)


import scipy.stats as ss

print(ss.zscore([1,2,3]))