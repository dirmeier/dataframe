# @author = 'Simon Dirmeier'
# @email = 'rafstraumur@simon-dirmeier.net'


class DataFrameColumn:
    """
    Class that represents one column in a dataframe.

    """
    def __init__(self, colname, vals):
        self.__colname = colname
        self.__vals = vals

    def size(self):
        """
        Getter for number if items in the column.

        :return: returns the number of items
        """
        return len(self.__vals)

    @property
    def values(self):
        """
        Getter for the column values.

        :return: returns the values of the column
        """
        return self.__vals

    @property
    def colname(self):
        """
        Getter for the column name.

        :return: returns the column name
        """
        return self.__colname

    def __getitem__(self, index):
        if isinstance(index, slice) or isinstance(index, int):
            return self.__vals[index]
        elif isinstance(index, tuple):
            return [self.__vals[x] for x in list(index)]
        elif isinstance(index, list):
            return [self.__vals[x] for x in index]
        return self.__vals[index]
