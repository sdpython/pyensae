#-*- coding: utf-8 -*-
import sys
import os
import datetime
import re
import sphinxjp.themes.basicstrap

sys.path.insert(0, os.path.abspath(os.path.join(os.path.split(__file__)[0])))
sys.path.insert(
    0,
    os.path.abspath(
        os.path.join(
            os.path.split(__file__)[0],
            "..",
            "..",
            "..",
            "..",
            "pyquickhelper",
            "src")))

from pyquickhelper.helpgen.default_conf import set_sphinx_variables

set_sphinx_variables(__file__, "pyensae", "Xavier Dupré", 2017,
                     "basicstrap", None, locals(), add_extensions=None,
                     extlinks=dict(issue=('https://github.com/sdpython/pyensae/issues/%s', 'issue')))

blog_root = "http://www.xavierdupre.fr/app/pyensae/helpsphinx/"
blog_background = False
exclude_patterns += ["pyensae/file_helper/pigjar/*",
                     "pyensae/file_helper/hadoopjar/*"]
