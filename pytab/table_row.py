# @author = 'Simon Dirmeier'
# @email = 'rafstraumur@simon-dirmeier.net'

class TableRow:
    def __init__(self, rowname=None, vals=None):
        if rowname is not None:
            self.__rowname = rowname
        if vals is not None:
            self.__vals = vals
