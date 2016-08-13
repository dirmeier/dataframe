# @author = 'Simon Dirmeier'
# @email = 'rafstraumur@simon-dirmeier.net'
from dataframe import DataFrame
from itertools import chain
import numpy
# x = DataFrame(a=list(range(10)),b=[1, 28880000] * 5).group("b")
# print(x)
# a = ['a', 'b', 'c', 3, 4, 'd', 6, 7, 8]
# new_list = list(chain(a[0:2], [a[4]], a[6:]))
# print(new_list)
#
#
# import scipy.stats as ss
#
# print(ss.zscore([1,2,3]))

# a = [1,2,1,2,1,2,1,2,1,2,3]
# print(a)
# s = numpy.unique(a)
# print(s)
# ii = numpy.where(a == s[0])[0]
# print(ii)

# class C(object):
#     def l(self, *a):
#         print(a)
#     def __getitem__(self, val):
#         if isinstance(val, tuple):
#             print(list(val))
#         if isinstance(val, slice):
#             print(list(range(*val.indices(10))))
#             print(*val.indices(10))
#             print()
# c = C()
#
# s = ["a", "b", "c"]
# print(s)
# d = [x for x in s if x not in["a", "b"] ]
# print(d)

class B:
    def __init__(self, *args,  **kwargs):
        if kwargs:
            print("dict")
        elif args:
            print("list")

B(**{"a":1})
print("ssssssssssssssssssss")
B(*list(range(4)))