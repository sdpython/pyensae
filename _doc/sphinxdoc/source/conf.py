# -*- coding: utf-8 -*-
import sys
import os
import alabaster
from pyquickhelper.helpgen.default_conf import set_sphinx_variables

sys.path.insert(0, os.path.abspath(os.path.join(os.path.split(__file__)[0])))

set_sphinx_variables(__file__, "pyensae", "Xavier Dupré", 2023,
                     "alabaster", alabaster.get_path(),
                     locals(), add_extensions=None,
                     extlinks=dict(issue=(
                         'https://github.com/sdpython/pyensae/issues/%s',
                         'issue %s')))

blog_root = "http://www.xavierdupre.fr/app/pyensae/helpsphinx/"
blog_background = False

html_css_files = ['my-styles.css']

nblinks = {"code-r2python": blog_root + "pyensae/languages/rconverter.html"}

epkg_dictionary = ({
    "antlr4": 'https://github.com/antlr/antlr4',
    "antlr4-python3-runtime": "https://pypi.org/project/antlr4-python3-runtime/",
    "blockdiag": 'http://blockdiag.com/',
    'cartopy': 'https://scitools.org.uk/cartopy/docs/latest/',
    'GeoDataFrame': 'https://geopandas.org/reference/geopandas.GeoDataFrame.html',
    'geopandas': 'https://geopandas.org/',
    "json": 'https://en.wikipedia.org/wiki/JSON',
    "manydataapi": 'http://www.xavierdupre.fr/app/manydataapi/helpsphinx/index.html',
    "networkx": 'https://networkx.github.io/',
    "pyenbc": 'http://www.xavierdupre.fr/app/pyenbc/helpsphinx/index.html',
    "SQLite3": 'https://www.sqlite.org/index.html',
})
