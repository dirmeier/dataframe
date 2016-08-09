from ._check import is_none, is_callable, has_elements
from ._dataframe_abstract import ADataFrame
from ._dataframe_column import DataFrameColumn
from .dataframe_grouped import GroupedDataFrame
from ._dataframe_row import DataFrameRow


class DataFrame(ADataFrame):
    """
    The base DataFrame class
    """

    def __init__(self, **kwargs):
        """
        Constructor for DataFrame.

        :param kwargs: standard named vargs argument, i.e. list of named lists
        :type kwargs: list of named lists
        :return: returns a new DataFrame object
        :rtype: DataFrame
        """
        self.__data_columns = []
        self.__colnames = []
        self.__ncol = len(kwargs)
        self.__append(**kwargs)

    def __iter__(self):
        """
        Iterator implementation for DataFrame. Every iteration yields one row of the DataFrame.

        :return: returns a row from the DataFrame
        :rtype: DataFrameRow
        """
        for i in range(self.__nrow):
            yield DataFrameRow(i, [x[i] for x in self.__data_columns], self.__colnames)

    def __getitem__(self, item):
        """
        Getter method for DataFrame. Returns the column with name item.

        :param item: the name of a column
        :type item: str
        :return: returns a column from the DataFrame
        :rtype: DataFrameColumn
        """
        if item in self.__colnames:
            return self.__data_columns[self.__colnames.index(item)]
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
        s = "\t" + "\t".join(self.__colnames) + "\n"
        sit = self.__iter__()
        for i in range(10):
            st = sit.__next__().__str__()
            if st is not None:
                s += st + "\n"
        return s

    def aggregate(self, f, new_col, *args):
        """

        :param f:
        :param new_col:
        :param args:
        :return:
        """
        if is_callable(f) and not is_none(new_col) and has_elements(*args):
            self.__do_aggregate(f, new_col, *args)
        return self

    def __do_aggregate(self, f, new_col, *col_names):
        colvals = [self[x] for x in col_names]
        if colvals is None:
            return
        res = f()(colvals)
        if res.size != 1:
           raise ValueError("The function you provided yields an array of false length!")
        self._cbind(**{new_col: res})

    def subset(self, *args):
        cols = {}
        for k in self.__colnames:
            if k in args:
                cols[str(k)] = self.__data_columns[self.__colnames.index(k)].values()
        return DataFrame(**cols)

    def group(self, *args):
        return GroupedDataFrame(self, *args)

    def modify(self, f, new_col, *args):
        if is_callable(f) and not is_none(new_col) and has_elements(*args):
            self.__do_modify(f, new_col, *args)
        return self

    def __do_modify(self, f, new_col, *col_names):
        colvals = [self[x] for x in col_names]
        if colvals is None:
            return
        res = f()(colvals)
        if res.size != len(colvals):
            raise ValueError("The function you provided yields an array of false length!")
        self._cbind(**{new_col: res})

    def _nrow(self):
        return self.__nrow

    def _ncol(self):
        return self.__ncol

    def _cbind(self, **kwargs):
        self.__append(**kwargs)

    def _colnames(self):
        return self.__colnames

    def _columns(self):
        return self.__data_columns

    def _which_colnames(self, *args):
        idx = []
        for i in range(len(self.__colnames)):
            if self.__colnames[i] in args:
                idx.append(i)
        return idx

    def __append(self, **kwargs):
        keys = [x for x in kwargs.keys()]
        keys.sort()
        lens = set()
        for k in keys:
            k = str(k)
            v = kwargs.get(k)
            if k in self.__colnames:
                print("Appending duplicate colname!")
            self.__colnames.append(k)
            self.__data_columns.append(DataFrameColumn(k, v))
            lens.add(len(v))
        if len(lens) != 1:
            raise ValueError("Columns don't have equal sizes!")
        self.__nrow = list(lens).pop()
