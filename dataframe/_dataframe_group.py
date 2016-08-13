# @author = 'Simon Dirmeier'
# @email = 'rafstraumur@simon-dirmeier.net'

from ._dataframe_column import DataFrameColumnSet


class DataFrameGroup:
    def __init__(self, grp_idx, rows):
        #TODO
        self.__grp_idx = grp_idx
        self.__nrow = len(rows)
        self.__rows = rows
        self.__data_columns = DataFrameColumnSet()

    def __str__(self):
        buf = "Group " + str(self.__grp_idx) + ":"
        for i in self.__rows:
            buf += " " + i.__str__()
        return buf

    def __repr__(self):
        return self.__str__()

    def __getitem__(self, idx):
        return self.__rows[idx]

    def __iter__(self):
        for i in self.__rows:
            yield i

    def append(self, el):
        for i in range(el):
            self.__rows.append(el)

    def __grp_index(self):
        return self.__grp_idx

    def values(self):
        return self.__rows
