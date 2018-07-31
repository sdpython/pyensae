# -*- coding: utf-8 -*-
"""
@file
@brief Complex joins with pandas.
"""
import pandas


def df_crossjoin(df1, df2, **kwargs):
    """
    Make a cross join (cartesian product) between two dataframes by using a constant temporary key.
    Also sets a MultiIndex which is the cartesian product of the indices of the input dataframes.
    Source: `Cross join / cartesian product between pandas DataFrames
    https://mkonrad.net/2016/04/16/cross-join--cartesian-product-between-pandas-dataframes.html>`_.

    @param      df1     dataframe 1
    @param      df2     dataframe 2
    @param      kwargs  keyword arguments that will be passed to pd.merge()
    @return             cross join of df1 and df2

    .. exref::
        :title: Cross join with a pandas dataframe

        .. runpython::
            :showcode:

            import pandas
            from pyensae.mlhelper import df_crossjoin
            df = pandas.DataFrame([{"x":3, "y": 4}, {"x":5, "y": 6}])
            jj = df_crossjoin(df, df.copy())

        A dataframe cannot be joined on itself, the second one musrt be copied.
    """
    df1['_tmpkey'] = 1
    df2['_tmpkey'] = 1
    res = pandas.merge(df1, df2, on='_tmpkey', **
                       kwargs).drop('_tmpkey', axis=1)
    res.index = pandas.MultiIndex.from_product((df1.index, df2.index))
    df1.drop('_tmpkey', axis=1, inplace=True)
    df2.drop('_tmpkey', axis=1, inplace=True)
    return res
