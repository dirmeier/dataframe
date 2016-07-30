# @author = 'Simon Dirmeier'
# @email = 'rafstraumur@simon-dirmeier.net'

class TableColumn:
    def __init__(self, colname, vals):
        self.__colname = colname
        self.__vals = vals

    def values(self):
        return self.__vals
