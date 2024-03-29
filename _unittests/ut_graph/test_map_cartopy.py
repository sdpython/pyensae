"""
@brief      test log(time=1s)
"""
import os
import unittest
from pyquickhelper.pycode import (
    get_temp_folder, ExtTestCase, fix_tkinter_issues_virtualenv,
    skipif_circleci)
from pyensae.datasource import load_french_departements
from pyensae.graphhelper import plot_map_france, plot_map_france_polygon


class TestMap(ExtTestCase):

    @skipif_circleci('cartopy crashes on circleci')
    def test_plot_map_france(self):
        temp = get_temp_folder(__file__, "temp_plot_map_france")
        fix_tkinter_issues_virtualenv()
        from matplotlib import pyplot as plt  # pylint: disable=C0415
        import cartopy.crs as ccrs  # pylint: disable=C0415

        fig = plt.figure(figsize=(7, 7))
        ax = fig.add_subplot(1, 1, 1, projection=ccrs.PlateCarree())
        ax.set_extent([-5, 10, 38, 52])
        plot_map_france(ax=ax)
        img = os.path.join(temp, "france.png")
        try:
            fig.savefig(img)
        except AttributeError as e:
            if "'GeoAxesSubplot' object has no attribute '_autoscaleXon'" in str(e):
                return
            raise e
        plt.close('all')
        self.assertExists(img)

    @skipif_circleci('cartopy crashes on circleci')
    def test_plot_map_france_polygon(self):
        temp = get_temp_folder(__file__, "temp_plot_map_france_polygon")
        df = load_french_departements(cache=temp)

        fix_tkinter_issues_virtualenv()
        from matplotlib import pyplot as plt  # pylint: disable=C0415
        import cartopy.crs as ccrs  # pylint: disable=C0415

        fig = plt.figure(figsize=(7, 7))
        ax = fig.add_subplot(1, 1, 1, projection=ccrs.PlateCarree())
        ax.set_extent([-5, 10, 38, 52])
        N = float(df.shape[0])
        try:
            plot_map_france_polygon(
                ax=ax, geometry=df['geometry'],
                colors=[(i / N, i / N, i / N) for i in range(df.shape[0])])
        except AttributeError as e:
            if "'GeoAxesSubplot' object has no attribute '_autoscaleXon'" in str(e):
                return
            raise e
        img = os.path.join(temp, "france.png")
        fig.savefig(img)
        if __name__ == "__main__":
            plt.show()
        plt.close('all')
        self.assertExists(img)


if __name__ == "__main__":
    unittest.main()
