#-*- coding: utf-8 -*-
"""
@file
@brief Adds functionalities to a dataframe.
"""
import pandas
import datetime


class TableFormula(pandas.DataFrame):
    """
    Extends class :epkg:`pandas:DataFrame` or proposes extensions
    to existing functions using lambda functions.
    """

    def __init__(self, *args, **kwargs):
        """
        Constructor.
        """
        pandas.DataFrame.__init__(self, *args, **kwargs)

    def sort(self, function_sort, reverse=False):
        """
        Sorts rows based on the values returned by *function_sort*.

        @param      function_sort   lambda function
        @param      reverse         reverse order

        The function creates a column ``__key__`` and removes it later.
        The changes happen inplace.
        """
        if "__key__" in self.columns:
            raise ValueError(
                "__key__ cannot be used in the original dataframe.")
        self["__key__"] = self.apply(lambda row: function_sort(row), axis=1)
        self.sort_values("__key__", inplace=True, ascending=not reverse)
        self.drop("__key__", inplace=True, axis=1)

    def fgroupby(self, function_key, function_values, columns=None,
                 function_agg=None, function_weight=None):
        """
        Groups information based on columns defined by lambda functions.

        @param      function_key        defines the key
        @param      function_values     defines the values
        @param      columns             name of the columns, if None, new ones will be created
        @param      function_agg        how to aggregate the data, if None, the default is
                                        :epkg:`pandas:DataFrame:sum`.
        @param      function_weight     defines weights, can be None

        The function uses columns ``__key__``, ``__weight__``.
        You should not use these names.
        Others columns are created ``__value_{0}__`` and
        ``__weight_{0}__``. All of them are created and removed
        before returning the result.

        Example:

        ::

            group = table.groupby(lambda v: v["name"],
                      [lambda v: v["d_a"]],
                      ["sum_d_a"],
                      [lambda vec, w: sum(vec) / w],
                      lambda v: v["d_b"])
        """
        if "__key__" in self.columns:
            raise ValueError(
                "__key__ cannot be used in the original dataframe.")
        if "__weight__" in self.columns:
            raise ValueError(
                "__weight__ cannot be used in the original dataframe.")

        cp = self.copy()
        cp["__key__"] = cp.apply(lambda row: function_key(row), axis=1)
        if function_weight is not None:
            cp["__weight__"] = cp.apply(
                lambda row: function_weight(row), axis=1)

        if columns is None:
            columns = ["fv{0}" for i in range(len(function_values))]
        if len(columns) != len(function_values):
            raise ValueError(
                "Parameters function_values and columns must have the same size.")
        if function_agg is None:
            function_agg = [pandas.DataFrame.sum for c in columns]
        if len(function_agg) != len(function_values):
            raise ValueError(
                "Parameters function_values and function_agg must have the same size.")

        values = []
        rep = dict()
        for v, cnew in zip(function_values, columns):
            n = "__value_{0}__".format(cnew)
            values.append(n)
            rep[n] = cnew
            if function_weight is None:
                cp[n] = cp.apply(lambda row: v(row), axis=1)
            else:
                cp[n] = cp.apply(lambda row: v(row), axis=1) * cp["__weight__"]

        if function_weight is None:
            aggs = {k: v for k, v in zip(values, function_agg)}
            gr = cp.groupby("__key__", as_index=False).agg(aggs)
        else:
            sum_weight = cp["__weight__"].sum()
            aggs = {k: (lambda c: v(c, sum_weight))
                    for k, v in zip(values, function_agg)}
            gr = cp.groupby("__key__", as_index=False).agg(aggs)
        gr.columns = [rep.get(_, _) for _ in gr.columns]
        gr = gr.drop("__key__", axis=1)
        return TableFormula(gr)

    def add_column_index(self, index, name=None):
        """
        Changes the index.

        @param      index       new_index
        @param      name        name of the index

        The changes happen inplace.
        """
        self["__key__"] = index
        self.set_index("__key__", inplace=True)
        self.index.rename(name, inplace=True)

    def add_column_vector(self, name, values):
        """
        Adds a column knowing its name and a vector of values.

        @param      name                name of the column
        @param      values              values

        The changes happen inplace.
        """
        self[name] = values

    def addc(self, name, function_value):
        """
        Adds a column knowing its name and a lambda function.

        @param      name                name of the column
        @param      function_value      function

        The changes happen inplace.
        """
        self[name] = self.apply(lambda row: function_value(row), axis=1)

    def graph_XY(self, curves, xlabel=None, ylabel=None, marker=True,
                 link_point=False, title=None, format_date="%Y-%m-%d",
                 legend_loc=0, figsize=None, ax=None):
        """
        @param      curves      list of 3-uples (generator for X, generator for Y, label)
                                for some layout, it can also be:
                                (generator for X, generator for Y, generator for labels, label)
        @param      xlabel      label for X axis
        @param      ylabel      label for Y axis
        @param      marker      add a marker for each point
        @param      link_point  link points between them
        @param      title       graph title
        @param      format_date if X axis is a datetime object, the function will use this format
                                to print dates
        @param      legend_loc  location of the legend
        @param      figsize     size of the figure
        @param      ax          :epkg:`matplotlib:Axis` or None to create a new one
        @return                 :epkg:`matplotlib:Axis`

        For the legend position, see `matplotlib <http://matplotlib.org/api/legend_api.html>`_.

        Example:

        ::

            table.graph_XY ( [ [ lambda v: v["sum_a"], lambda v: v["sum_b"], "xy label 1"],
                              [ lambda v: v["sum_b"], lambda v: v["sum_c"], "xy label 2"],
                                ])
        """
        if ax is None:
            import matplotlib.pyplot as plt
            fig, ax = plt.subplots(1, 1, figsize=figsize)

        smarker = {(True, True): 'o-', (True, False): 'o', (False, True): '-',
                   #(False, False) :''
                   }[marker, link_point]
        allvalues = []

        for xf, yf, label in curves:
            x = self.apply(xf, axis=1)
            y = self.apply(yf, axis=1)
            ax.plot(x, y, smarker, label=label)
            allvalues.extend(x)

        if isinstance(allvalues[0], datetime.datetime):
            import matplotlib.dates
            hfmt = matplotlib.dates.DateFormatter(format_date)
            if "%H" in format_date or "%M" in format_date:
                ax.xaxis.set_major_locator(matplotlib.dates.MinuteLocator())
            ax.xaxis.set_major_formatter(hfmt)
            fig = ax.get_figure()
            fig.autofmt_xdate()

        ax.legend(loc=legend_loc)
        return ax
