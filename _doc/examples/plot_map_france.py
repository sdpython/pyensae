"""

.. _l-map-france:

Plot a map of France
====================

This example show how to leverage a function to
draw a map of France.

plot_map_france
+++++++++++++++

Just a map of France.
"""

from matplotlib import pyplot as plt
from matplotlib import pyplot as plt
import cartopy.crs as ccrs
from pyensae.datasource import load_french_departements
from pyensae.graphhelper import plot_map_france, plot_map_france_polygon

ax = plot_map_france()
ax.set_extent([-5., 10., 38., 52.])
ax.set_title('France')


#########################################
# plot_map_france_polygon
# +++++++++++++++++++++++
#
# Other function to draw departments in France.


# loads the French departments
df = load_french_departements()

fig = plt.figure(figsize=(7, 7))
ax = fig.add_subplot(1, 1, 1, projection=ccrs.PlateCarree())
N = float(df.shape[0])
plot_map_france_polygon(
    ax=ax, geometry=df['geometry'],
    colors=[(i / N, 1. - i / N, 1. - i / N) for i in range(df.shape[0])])
ax.set_title('France departments')
plt.show()
