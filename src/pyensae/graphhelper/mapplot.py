"""
@file
@brief Plotting maps.
"""


def plot_map_france(ax=None, scale='50m'):
    """
    Creates a map for France using :epkg:`cartopy`.

    @param      ax          existing axes or None to create ones
    @param      scale       scale in (`10m`, `50m`, `110m`)
    @return                 ax

    .. plot::

        from matplotlib import pyplot as plt
        from pyensae.graphhelper import plot_map_france

        plot_map_france()
        plt.show()
    """

    if ax is None:
        import matplotlib.pyplot as plt  # pylint: disable=C0415
        import cartopy.crs as ccrs  # pylint: disable=C0415
        fig = plt.figure(figsize=(8, 8))
        ax = fig.add_subplot(1, 1, 1, projection=ccrs.PlateCarree())
        ax.set_extent([-5, 10, 38, 52])

    import cartopy.feature as cfeature  # pylint: disable=C0415
    ax.add_feature(cfeature.OCEAN.with_scale(scale))
    ax.add_feature(cfeature.RIVERS.with_scale(scale))
    ax.add_feature(cfeature.BORDERS.with_scale(scale), linestyle=':')
    return ax


def plot_map_france_polygon(geometry, colors, ax=None, scale='50m'):
    """
    Plots polygons into a map for France.

    @param      geometry        series of polygons
    @param      colors          colors
    @param      scale           scale, see @see fn map_france
    @param      ax              existing axes, None to create one
    @return                     ax

    .. plot::

        from matplotlib import pyplot as plt
        import cartopy.crs as ccrs
        from pyensae.datasource import load_french_departements
        from pyensae.graphhelper import plot_map_france, plot_map_france_polygon

        # loads the French departments
        df = load_french_departements()

        fig = plt.figure(figsize=(7,7))
        ax = fig.add_subplot(1, 1, 1, projection=ccrs.PlateCarree())
        ax.set_extent([-5, 10, 38, 52])
        N = float(df.shape[0])
        plot_map_france_polygon(
            ax=ax, geometry=df['geometry'],
            colors=[(i/N, i/N, i/N) for i in range(df.shape[0])])

        plt.show()
    """
    from geopandas.plotting import plot_polygon_collection  # pylint: disable=C0415
    ax = plot_map_france(scale=scale, ax=ax)
    plot_polygon_collection(
        ax, geometry, facecolor=colors, values=None, edgecolor='black')
    return ax
