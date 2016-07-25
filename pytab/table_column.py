# @author = 'Simon Dirmeier'
# @email = 'rafstraumur@simon-dirmeier.net'

class TableColumn:
    def __init__(self, colname=None, vals=None):
        if colname is not None:
            self.__colname = colname
        if vals is not None:
            self.__vals = vals
