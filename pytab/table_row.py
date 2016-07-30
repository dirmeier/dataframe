# @author = 'Simon Dirmeier'
# @email = 'rafstraumur@simon-dirmeier.net'

class TableRow:
    def __init__(self, idx, vals):
        self.__idx = idx
        self.__vals = vals

    def idx(self):
        return self.__idx
