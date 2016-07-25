# @author = 'Simon Dirmeier'
# @email = 'rafstraumur@simon-dirmeier.net'

class TableGrouping:
    def __init__(self):
        self.__groups = []
        self.__grouping = {}


def group_by_(obj=None, *args):
    grp = TableGrouping()
    for row in obj:
        __add_grp(grp, row, *args)

def __add_grp(grp, row, *args):
    pass
