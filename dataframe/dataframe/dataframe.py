from dataframe._check import _is_none, _is_callable, _has_elements
from dataframe.dataframe_abstract import ADataFrame
from dataframe.dataframe_column import DataFrameColumn
from dataframe.dataframe_grouped import GroupedDataFrame
from dataframe.dataframe_row import DataFrameRow


class DataFrame(ADataFrame):
    def __init__(self, **kwargs):
        self.__data_columns = []
        self.__colnames = []
        self.__ncol = len(kwargs)
        self.__append(**kwargs)

    def __iter__(self):
        for i in range(self.__nrow):
            yield DataFrameRow(i, [x[i] for x in self.__data_columns], self.__colnames)

    def __getitem__(self, item):
        if item in self.__colnames:
            return self.__data_columns[item]
        return None

    def aggregate(self, f, new_col, *args):
        if _is_callable(f) and not _is_none(new_col) and _has_elements(*args):
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
        if _is_callable(f) and not _is_none(new_col) and _has_elements(*args):
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
