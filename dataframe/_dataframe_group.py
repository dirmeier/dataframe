# @author = 'Simon Dirmeier'
# @email = 'rafstraumur@simon-dirmeier.net'

from ._dataframe_column_set import DataFrameColumnSet


class DataFrameGroup:
    def __init__(self, grp_idx, grouping_values, grouping_colnames, **kwargs):
        self.__grp_idx = grp_idx
        self.__grouping_values = grouping_values
        self.__grouping_colnames = grouping_colnames
        self.__data_columns = DataFrameColumnSet(**kwargs)

    def __getitem__(self, item):
        """
        Getter method for DataFrame. Returns the column with name item.

        :param item: the name of a column
        :type item: str
        :return: returns a column from the DataFrame
        :rtype: DataFrameColumn
        """

        if isinstance(item, str) and item in self.__data_columns.colnames():
            return self.__data_columns[self.__data_columns.colnames().index(item)]
        raise TypeError("Wrong idx (either no string or item is not in DataFrame!")

    def __iter__(self):
        for i in range(self.__data_columns.nrow()):
            yield self.__data_columns.row(i)

    def grp_idx(self):
        return self.__grp_idx

    def grouping_values(self):
        return self.__grouping_values

    def grouping_colnames(self):
        return self.__grouping_colnames
