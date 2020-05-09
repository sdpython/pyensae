"""
@file
@brief Geographic datasets.
"""
import math
import os
import pandas
from pyquickhelper.filehelper import un7zip_files
from .http_retrieve import download_data


def lambert932WGPS(lambertE, lambertN):
    """
    Converts Lambert coordinates into longitude, latitude.
    Does not use :epkg:`pyproj`.

    @param      lambertE        lambertE
    @param      lambertN        lambertN
    @return                     longitude, latitude
    """

    class constantes:
        GRS80E = 0.081819191042816
        LONG_0 = 3
        XS = 700000
        YS = 12655612.0499
        n = 0.7256077650532670
        C = 11754255.4261

    delX = lambertE - constantes.XS
    delY = lambertN - constantes.YS
    gamma = math.atan(-delX / delY)
    R = math.sqrt(delX * delX + delY * delY)
    latiso = math.log(constantes.C / R) / constantes.n
    sinPhiit0 = math.tanh(latiso + constantes.GRS80E *
                          math.atanh(constantes.GRS80E * math.sin(1)))
    sinPhiit1 = math.tanh(latiso + constantes.GRS80E *
                          math.atanh(constantes.GRS80E * sinPhiit0))
    sinPhiit2 = math.tanh(latiso + constantes.GRS80E *
                          math.atanh(constantes.GRS80E * sinPhiit1))
    sinPhiit3 = math.tanh(latiso + constantes.GRS80E *
                          math.atanh(constantes.GRS80E * sinPhiit2))
    sinPhiit4 = math.tanh(latiso + constantes.GRS80E *
                          math.atanh(constantes.GRS80E * sinPhiit3))
    sinPhiit5 = math.tanh(latiso + constantes.GRS80E *
                          math.atanh(constantes.GRS80E * sinPhiit4))
    sinPhiit6 = math.tanh(latiso + constantes.GRS80E *
                          math.atanh(constantes.GRS80E * sinPhiit5))

    longRad = math.asin(sinPhiit6)
    latRad = gamma / constantes.n + constantes.LONG_0 / 180 * math.pi

    longitude = latRad / math.pi * 180
    latitude = longRad / math.pi * 180

    return longitude, latitude


def load_french_departements(cache=None):
    """
    Returns the definition of French departments.

    @param      cache       cache folder
    @return                 French departments as a :epkg:`GeoDataFrame`

    .. exref::
        :title: Loads French departments polygons

        Simple example to retrieve French departements.

        .. runpython::
            :showcode:

            from pyensae.datasource import load_french_departements
            df = load_french_departements(cache=temp)
            print(df.head(2).T)
    """
    if cache is None:
        cache = '.'
    # delayed import
    import shapefile
    import geopandas
    from shapely.geometry import Polygon
    from shapely.ops import unary_union

    name = "GEOFLA_2-1_DEPARTEMENT_SHP_LAMB93_FXX_2015-12-01.7z"
    try:
        download_data(name, whereTo=cache,
                      website="https://wxs-telechargement.ign.fr/oikr5jryiph0iwhw36053ptm/telechargement/inspire/"
                      "GEOFLA_THEME-DEPARTEMENTS_2015_2$GEOFLA_2-1_DEPARTEMENT_SHP_LAMB93_FXX_2015-12-01/file/")
    except Exception as e:
        # au cas le site n'est pas accessible
        download_data(name, website="xd", whereTo=cache)

    full_name = os.path.join(cache, name)
    un7zip_files(full_name, where_to=os.path.join(cache, "shapefiles"))
    departements = os.path.join(cache, 'shapefiles/GEOFLA_2-1_DEPARTEMENT_SHP_LAMB93_FXX_2015-12-01/GEOFLA/1_DONNEES_LIVRAISON_2015/'
                                'GEOFLA_2-1_SHP_LAMB93_FR-ED152/DEPARTEMENT/DEPARTEMENT.shp')

    r = shapefile.Reader(departements)
    shapes = r.shapes()
    records = r.records()

    polys = []
    datas = []
    for i, (record, shape) in enumerate(zip(records, shapes)):
        # coordinates in Lambert 93
        geo_points = [lambert932WGPS(x, y) for x, y in shape.points]
        rec = {}
        for k in ['CODE_DEPT', 'CODE_REG', 'CODE_CHF', 'ID_GEOFLA', 'NOM_CHF',
                  'NOM_DEPT', 'NOM_REG', 'X_CENTROID', 'X_CHF_LIEU',
                  'Y_CENTROID', 'Y_CHF_LIEU']:
            rec[k] = getattr(record, k, None)
        if len(shape.parts) == 1:
            # only one polygon
            poly = Polygon(geo_points)
        else:
            # merge them
            ind = list(shape.parts) + [len(shape.points)]
            pols = [Polygon(geo_points[ind[i]:ind[i + 1]])
                    for i in range(0, len(shape.parts))]
            try:
                poly = unary_union(pols)
            except Exception as e:
                poly = Polygon(geo_points)
        polys.append(poly)
        datas.append(rec)

    geom = geopandas.GeoDataFrame(geometry=polys)
    data = pandas.DataFrame(datas)
    return pandas.concat([geom, data], axis=1)
