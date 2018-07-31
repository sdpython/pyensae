"""
@file
@brief dendogram, heatmap functionalities.

It comes from `linkage.py <https://raw.githubusercontent.com/biokit/biokit/master/biokit/viz/linkage.py>`_
which I copied here because the module does not properly work on Python 3 (import issues).
See also `biokit license <https://github.com/biokit/biokit/blob/master/LICENSE>`_.

:author: Thomas Cokelaer

"""


class Linkage:
    """
    Linkage used in other tools such as Heatmap,
    the class requires `scipy <http://www.scipy.org/>`_.
    """

    def __init__(self):
        """
        unused
        """
        pass

    def linkage(self, df, method, metric):
        """
        Mostly calls `linkage
        <https://docs.scipy.org/doc/scipy/reference/generated/scipy.cluster.hierarchy.linkage.html>`_.

        @param      df          dataframe
        @param      method      see `linkage
                                <https://docs.scipy.org/doc/scipy/reference/generated/scipy.cluster.hierarchy.linkage.html>`_
        @param      metric      see `linkage
                                <https://docs.scipy.org/doc/scipy/reference/generated/scipy.cluster.hierarchy.linkage.html>`_
        @return                 output of `linkage
                                <https://docs.scipy.org/doc/scipy/reference/generated/scipy.cluster.hierarchy.linkage.html>`_
        """
        from scipy.cluster.hierarchy import linkage
        from scipy.spatial.distance import pdist, squareform
        d = pdist(df)
        D = squareform(d)
        Y = linkage(D, method=method, metric=metric)
        return Y
