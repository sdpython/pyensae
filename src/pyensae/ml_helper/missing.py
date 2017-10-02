#-*- coding: utf-8 -*-
"""
@file
@brief Missing values and pandas.
"""
import pandas
import numpy
from .joins import df_crossjoin


def add_missing_indices(df, column, all_values, values=None, fillvalue=numpy.nan):
    """
    After aggregation, it usually happens that the series is sparse.
    This function add rows for missing time.

    @param      df          dataframe to extend
    @param      column      column with time
    @param      all_values  all the values we want
    @param      values      columns which contain the values, the others are considered as the keys
    @return                 new dataframe

    .. exref::
        :title: Add missing values in one column.

        .. runpython::
            :showcode:

            import pandas
            from pyensae.ml_helper import add_missing_indices
            df = pandas.DataFrame([{"x":3, "y": 4, "z":1}, {"x":5, "y": 6, "z":2}])
            df2 = add_missing_indices(df, "x", ["y", "z"], [3,4,5,6])
            print(df2)

        .. runpython::
            :showcode:

            import pandas
            from pyensae.ml_helper import add_missing_indices
            df = pandas.DataFrame([{"x":3, "y": 4, "z":1}, {"x":5, "y": 6, "z":2}])
            df2 = add_missing_indices(df, "x", ["y"], [3,4,5,6])
            print(df2)

    """
    if isinstance(values, str):
        values = [values]
    if values is None or len(values) == 0:
        keys = [_ for _ in df.columns if _ != column]
    else:
        keys = [_ for _ in df.columns if _ not in values and _ != column]
    if isinstance(all_values, list):
        dfti = pandas.DataFrame({column: all_values})
    elif isinstance(all_values, (pandas.Series, numpy.ndarray)):
        dfti = pandas.DataFrame({column: all_values})
    elif isinstance(all_values, pandas.DataFrame):
        dfti = all_values
        if dfti.shape[1] != 1:
            raise ValueError("all_values should have only one column")
        if dfti.columns[0] != column:
            raise ValueError(
                "all_values should have only one column with name '{0}'".format(column))
    else:
        raise TypeError(
            "Unexpected type for all_values '{0}'".format(type(all_values)))

    if len(keys) == 0:
        dfj = df.merge(dfti, on=column, how="right")
    else:
        nkeys = keys + [column]
        only = df[nkeys].groupby(
            keys, as_index=False).count().drop(column, axis=1)
        dfti = df_crossjoin(only, dfti)
        dfj = df.merge(dfti, on=nkeys, how="right")
    return dfj.sort_values(column)
