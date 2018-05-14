# -*- coding: utf-8 -*-
"""
@file
@brief Helpers for pandas `pandas <http://pandas.pydata.org/>`_.
"""
import warnings
import numpy
from pandas import Index, DataFrame


def numpy_types():
    """
    Returns the list of :epkg:`numpy` available types.

    @return     list of types
    """

    return [numpy.bool_,
            numpy.int_,
            numpy.intc,
            numpy.intp,
            numpy.int8,
            numpy.int16,
            numpy.int32,
            numpy.int64,
            numpy.uint8,
            numpy.uint16,
            numpy.uint32,
            numpy.uint64,
            numpy.float_,
            numpy.float16,
            numpy.float32,
            numpy.float64,
            numpy.complex_,
            numpy.complex64,
            numpy.complex128]


def pandas_fillna(df, by, hasna=None, suffix=None):
    """
    Replaces the :epkg:`nan` values for something not :epkg:`nan`.

    @param      df      dataframe
    @param      by      list of columns for which we need to replace nan
    @param      hasna   None or list of columns for which we need to replace NaN
    @param      suffix  use a prefix for the NaN value
    @return             list of values chosen for each column, new dataframe (new copy)
    """
    suffix = suffix if suffix else "²"
    df = df.copy()
    rep = {}
    for c in by:
        if hasna is not None and c not in hasna:
            continue
        if df[c].dtype in (str, bytes, object):
            se = set(df[c].dropna())
            val = se.pop()
            if isinstance(val, str):
                cst = suffix
                val = ""
            elif isinstance(val, bytes):
                cst = b"_"
            else:
                raise TypeError(
                    "Unable to determine a constant for type='{0}' dtype='{1}'".format(val, df[c].dtype))
            val += cst
            while val in se:
                val += suffix
            df[c].fillna(val, inplace=True)
            rep[c] = val
        else:
            dr = df[c].dropna()
            mi = abs(dr.min())
            ma = abs(dr.max())
            val = ma + mi
            if val <= ma:
                raise ValueError(
                    "Unable to find a different value for column '{0}': min={1} max={2}".format(val, mi, ma))
            df[c].fillna(val, inplace=True)
            rep[c] = val
    return rep, df


def pandas_groupby_nan(df, by, axis=0, as_index=False, suffix=None, nanback=True, **kwargs):
    """
    Does a *groupby* including keeping missing values (:epkg:`nan`).

    @param      df          dataframe
    @param      by          column or list of columns
    @param      axis        only 0 is allowed
    @param      as_index    should be False
    @param      suffix      None or a string
    @param      nanback     put :epkg:`nan` back in the index,
                            otherwise it leaves a replacement for :epkg:`nan`.
                            (does not work when grouping by multiple columns)
    @param      kwargs      other parameters sent to
                            `groupby <http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.groupby.html>`_
    @return                 groupby results

    See `groupby and missing values <http://pandas-docs.github.io/pandas-docs-travis/groupby.html#na-and-nat-group-handling>`_.
    If no :epkg:`nan` is detected, the function falls back in regular
    :epkg:`pandas:DataFrame:groupby` which has the following
    behavior.

    .. runpython::
        :showcode:

        from pandas import DataFrame

        data = [dict(a="a", b="b", c="c", n=1), dict(b="b", n=2),
                dict(a="a", n=3), dict(c="c", n=4)]
        df = DataFrame(data)
        print(df)
        gr = df.groupby(["a", "b", "c"]).sum()
        print(gr)

    Function @see fn pandas_groupby_nan modifies the behavior
    with:

    .. runpython::
        :showcode:

        from pandas import DataFrame
        from pyensae.ml_helper import pandas_groupby_nan

        data = [dict(a="a", b="b", c="c", n=1), dict(b="b", n=2),
                dict(a="a", n=3), dict(c="c", n=4)]
        df = DataFrame(data)
        gr2 = pandas_groupby_nan(df, ["a", "b", "c"])
        print(gr2)
    """
    if axis != 0:
        raise NotImplementedError("axis should be 0")
    if as_index:
        raise NotImplementedError("as_index must be False")
    if isinstance(by, tuple):
        raise TypeError("by should be of list not tuple")
    if not isinstance(by, list):
        by = [by]
    hasna = {}
    for b in by:
        h = df[b].isnull().values.any()
        if h:
            hasna[b] = True
    if len(hasna) > 0:
        rep, df_copy = pandas_fillna(df, by, hasna, suffix=suffix)
        res = df_copy.groupby(by, axis=axis, as_index=as_index, **kwargs)
        if len(by) == 1:
            if not nanback:
                dummy = DataFrame([{"a": "a"}])
                do = dummy.dtypes[0]
                typ = {c: t for c, t in zip(df.columns, df.dtypes)}
                if typ[by[0]] != do:
                    warnings.warn("NaN value: {0}".format(rep))
                return res
            for b in by:
                fnan = rep[b]
                if fnan in res.grouper.groups:
                    res.grouper.groups[numpy.nan] = res.grouper.groups[fnan]
                    del res.grouper.groups[fnan]
                new_val = list((numpy.nan if b == fnan else b)
                               for b in res.grouper.result_index)
                res.grouper.groupings[0]._group_index = Index(new_val)
                res.grouper.groupings[0].obj[b].replace(
                    fnan, numpy.nan, inplace=True)
                if isinstance(res.grouper.groupings[0].grouper, numpy.ndarray):
                    arr = numpy.array(new_val)
                    res.grouper.groupings[0].grouper = arr
                    if hasattr(res.grouper.groupings[0], '_cache') and 'result_index' in res.grouper.groupings[0]._cache:
                        del res.grouper.groupings[0]._cache['result_index']
                else:
                    raise NotImplementedError("Not implemented for type: {0}".format(
                        type(res.grouper.groupings[0].grouper)))
                res.grouper._cache['result_index'] = res.grouper.groupings[0]._group_index
        else:
            if not nanback:
                dummy = DataFrame([{"a": "a"}])
                do = dummy.dtypes[0]
                typ = {c: t for c, t in zip(df.columns, df.dtypes)}
                for b in by:
                    if typ[b] != do:
                        warnings.warn("NaN values: {0}".format(rep))
                        break
                return res
            raise NotImplementedError(
                "Not yet implemented. Replacing pseudo nan values by real nan values is not as easy as it looks. Use nanback=False")

            # keys = list(res.grouper.groups.keys())
            # didit = False
            # mapping = {}
            # for key in keys:
            #     new_key = list(key)
            #     mod = False
            #     for k, b in enumerate(by):
            #         if b not in rep:
            #             continue
            #         fnan = rep[b]
            #         if key[k] == fnan:
            #             new_key[k] = numpy.nan
            #             mod = True
            #             didit = True
            #             mapping[fnan] = numpy.nan
            #     if mod:
            #         new_key = tuple(new_key)
            #         mapping[key] = new_key
            #         res.grouper.groups[new_key] = res.grouper.groups[key]
            #         del res.grouper.groups[key]
            # if didit:
            #     # this code deos not work
            #     vnan = numpy.nan
            #     new_index = list(mapping.get(v, v)
            #                      for v in res.grouper.result_index)
            #     names = res.grouper.result_index.names
            #     # index = MultiIndex.from_tuples(tuples=new_index, names=names)
            #     # res.grouper.result_index = index  # does not work cannot set
            #     # values for [result_index]
            #     for k in range(len(res.grouper.groupings)):
            #         grou = res.grouper.groupings[k]
            #         new_val = list(mapping.get(v, v) for v in grou)
            #         grou._group_index = Index(new_val)
            #         b = names[k]
            #         if b in rep:
            #             vv = rep[b]
            #             grou.obj[b].replace(vv, vnan, inplace=True)
            #         if isinstance(grou.grouper, numpy.ndarray):
            #             grou.grouper = numpy.array(new_val)
            #         else:
            #             raise NotImplementedError(
            #                 "Not implemented for type: {0}".format(type(grou.grouper)))
            #     del res.grouper._cache
        return res
    else:
        return df.groupby(by, axis=axis, **kwargs)
