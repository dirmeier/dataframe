# @author = 'Simon Dirmeier'
# @email = 'rafstraumur@simon-dirmeier.net'


class DataFrameRow:
    def __init__(self, idx, vals, colnames):
        self.__idx = idx
        self.__colnames = colnames
        self.__vals = vals

    def __hash__(self):
        return hash(self.__idx)

    def __eq__(self, other):
        if isinstance(other, DataFrameRow):
            return self.__idx == other.__idx
        return False

    def __getitem__(self, index):
        return self.__vals[index]

    def __str__(self):
        return str(self.idx()) + ":\t" + "\t".join(str(x) for x in self.__vals)

    def __repr__(self):
        return self.__str__()

    def idx(self):
        return self.__idx

    def values(self):
        return self.__vals

    def colnames(self):
        return self.__colnames
