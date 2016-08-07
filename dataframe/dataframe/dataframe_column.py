# @author = 'Simon Dirmeier'
# @email = 'rafstraumur@simon-dirmeier.net'

class DataFrameColumn:
    def __init__(self, colname, vals):
        self.__colname = colname
        self.__vals = vals

    def values(self):
        return self.__vals

    def colname(self):
        return self.__colname

    def __getitem__(self, index):
        return self.__vals[index]
