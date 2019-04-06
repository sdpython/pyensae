# -*- coding: utf-8 -*-
import sys
import os
import sphinxjp.themes.basicstrap
from pyquickhelper.helpgen.default_conf import set_sphinx_variables

sys.path.insert(0, os.path.abspath(os.path.join(os.path.split(__file__)[0])))

set_sphinx_variables(__file__, "pyensae", "Xavier Dupré", 2019,
                     "basicstrap", None, locals(), add_extensions=None,
                     extlinks=dict(issue=('https://github.com/sdpython/pyensae/issues/%s', 'issue')))

blog_root = "http://www.xavierdupre.fr/app/pyensae/helpsphinx/"
blog_background = False

nblinks = {"code-r2python": blog_root + "pyensae/languages/rconverter.html"}

extensions.append("sphinxjp.themes.basicstrap")

epkg_dictionary = ({
    "antlr4": 'https://github.com/antlr/antlr4',
    "blockdiag": 'http://blockdiag.com/',
    "json": 'https://en.wikipedia.org/wiki/JSON',
    "manydataapi": 'http://www.xavierdupre.fr/app/manydataapi/helpsphinx/index.html',
    "networkx": 'https://networkx.github.io/',
    "pyenbc": 'http://www.xavierdupre.fr/app/pyenbc/helpsphinx/index.html',
    "SQLite3": 'https://www.sqlite.org/index.html',
})
