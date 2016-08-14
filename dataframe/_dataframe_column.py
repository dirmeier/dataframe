# @author = 'Simon Dirmeier'
# @email = 'rafstraumur@simon-dirmeier.net'

class DataFrameColumn:
    def __init__(self, colname, vals):
        self.__colname = colname
        self.__vals = vals

    def size(self):
        return len(self.__vals)

    def values(self):
        return self.__vals

    def colname(self):
        return self.__colname

    def __getitem__(self, index):
        if isinstance(index, slice) or isinstance(index, int):
            return self.__vals[index]
        elif isinstance(index, tuple):
            return [self.__vals[x] for x in list(index)]
        elif isinstance(index, list):
            return [self.__vals[x] for x in index]
        return self.__vals[index]
