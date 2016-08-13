# @author = 'Simon Dirmeier'
# @email = 'rafstraumur@simon-dirmeier.net'

class DataFrameColumnSet:
    def __init__(self):
        self.__data_columns = []
        self.__nrow = -1

    def __getitem__(self, item):
        if isinstance(item, int):
            return self.__data_columns[item]
        raise ValueError("Item should be integer!")

    def __iter__(self):
        for c in self.__data_columns:
            yield c

    def nrow(self):
        return self.__nrow

    def ncol(self):
        return len(self.colnames())

    def colnames(self):
        return [x.colname() for x in self.__data_columns]

    def append(self, column):
        if column.colname in self.colnames():
            ValueError("Appending duplicate col-name!")
        self.__data_columns.append(column)
        self.__nrow = self.__data_columns[-1].size()
        for col in self.__data_columns:
            if col.size() != self.__nrow:
                raise ValueError("Columns do not have equal lengths!")


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
