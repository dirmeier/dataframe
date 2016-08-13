from ._dataframe_abstract import ADataFrame
from ._dataframe_column_set import DataFrameColumnSet, DataFrameColumn
from .dataframe_grouped_dataframe import GroupedDataFrame

from ._check import is_none, is_callable, has_elements

class DataFrame(ADataFrame):
    """
    The base DataFrame class.
    """

    def __init__(self, **kwargs):
        """
        Constructor for DataFrame.

        :param kwargs: standard named vargs argument, i.e. list of named lists
        :type kwargs: list of named lists
        :return: returns a new DataFrame object
        :rtype: DataFrame
        """
        self.__data_columns = DataFrameColumnSet(**kwargs)

    def __iter__(self):
        """
        Iterator implementation for DataFrame. Every iteration yields one row of the DataFrame.

        :return: returns a row from the DataFrame
        :rtype: DataFrameRow
        """
        for i in range(self.nrow()):
            yield self.__row(i)

    def __getitem__(self, item):
        """
        Getter method for DataFrame. Returns the column with name item.

        :param item: the name of a column
        :type item: str
        :return: returns a column from the DataFrame
        :rtype: DataFrameColumn
        """

        if isinstance(item, str) and item in self.colnames():
            return self.__data_columns[self.colnames().index(item)]
        elif isinstance(item, int):
            return self.__row(item)
        elif isinstance(item, slice):
            return self.__rows(list(range(*item.indices(self.nrow()))))
        elif isinstance(item, tuple):
            return self.__rows(list(item))
        elif isinstance(item, list):
            return self.__rows(item)
        return None

    def __repr__(self):
        """
        String representation of DataFrame when print is called.

        :return: returns the string representation
        :rtype: str
        """
        return self.__str__()

    def __str__(self):
        """
        ToString method for DataFrame

        :return: returns the string representation
        :rtype: str
        """
        return self.__data_columns.__str__()

    def aggregate(self, clazz, new_col, *args):
        """
        Aggregate the rows of the dataframe into a single value.

        :param clazz: name of a class that extends class Callable
        :type clazz: class
        :param new_col: name of the new column
        :type new_col: str
        :param args: list of column names of the object that function should be applied to
        :type args: varargs
        :return: returns a new dataframe object with the aggregated value
        :rtype: DataFrame
        """
        if is_callable(clazz) and not is_none(new_col) and has_elements(*args):
            return self.__do_aggregate(clazz, new_col, *args)

    def __do_aggregate(self, clazz, new_col, *col_names):
        # get columns
        colvals = [self[x] for x in col_names]
        if colvals is None:
            return None
        # instantiate class and call
        res = [clazz()(*colvals)]
        if len(res) != 1:
            raise ValueError("The function you provided yields an array of false length!")
        return DataFrame(**{new_col: res})

    def subset(self, *args):
        """
        Subset only some of the columns of the dataframe

        :param args: list of column names of the object that should be subsetted
        :type args: varargs
        :return: returns dataframe with only the columns you selected
        :rtype: DataFrame
        """
        cols = {}
        for k in self.colnames():
            if k in args:
                cols[str(k)] = self.__data_columns[self.colnames().index(k)].values()
        return DataFrame(**cols)

    def group(self, *args):
        """
        Group the dataframe into row-subsets.

        :param args: list of column names taht should be used for grouping
        :type args: varargs
        :return: returns a dataframe that has grouping information
        :rtype: GroupedDataFrame
        """
        return GroupedDataFrame(self, *args)

    def modify(self, clazz, new_col, *args):
        """
        Modify some columns (i.e. apply a function) and add the result to the table

        :param clazz: name of a class that extends class Callable
        :type clazz: class
        :param new_col: name of the new column
        :type new_col: str
        :param args: list of column names of the object that function should be applied to
        :type args: varargs
        :return: returns a new dataframe object with the aggregated value
        :rtype: DataFrame
        """
        if is_callable(clazz) and not is_none(new_col) and has_elements(*args):
            return self.__do_modify(clazz, new_col, *args)

    def __do_modify(self, clazz, new_col, *col_names):
        colvals = [self[x] for x in col_names]
        if colvals is None:
            return None
        # instantiate class and call
        res = clazz()(*colvals)
        res = [res] if not isinstance(res, list) else res
        if len(res) != len(colvals[0].values()):
            raise ValueError("The function you provided yields an array of false length!")
        cols = {column.colname(): column.values() for column in self.__data_columns}
        cols[new_col] = res
        return DataFrame(**cols)

    def nrow(self):
        """
        Getter for the number of rows in the dataframe.

        :return: returns the number of rows
        :rtype: int
        """
        return self.__data_columns.nrow()

    def ncol(self):
        """
        Getter for the number of columns in the dataframe.

        :return: returns the number of columns
        :rtype: int
        """
        return self.__data_columns.ncol()

    def colnames(self):
        """
        Getter for the columns names of the dataframe

        :return: returns a list of column names
        :rtype: list(str)
        """
        return self.__data_columns.colnames()

    def which_colnames(self, *args):
        """
        Computes the indexes of the columns in the dataframe

        :param args: list of column names
        :type args: varargs
        :return: returns a list of indexes
        :rtype: list(int)
        """
        return self.__data_columns.which_colnames(*args)

    def __rows(self, idxs):
        return self.__data_columns.rows(idxs)

    def __row(self, idx):
        return self.__data_columns.row(idx)
