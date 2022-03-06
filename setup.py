# -*- coding: utf-8 -*-
import sys
import os
from setuptools import find_packages, setup
from pyquicksetup import read_version, read_readme, default_cmdclass
from distutils.core import Command

#########
# settings
#########

project_var_name = "pyensae"
versionPython = "%s.%s" % (sys.version_info.major, sys.version_info.minor)
path = "Lib/site-packages/" + project_var_name
readme = 'README.rst'
history = "HISTORY.rst"
requirements = None

KEYWORDS = [project_var_name, 'ENSAE', 'sqllite', 'database', 'teachings']
DESCRIPTION = """Helpers for teaching purposes (includes sqllite helpers)."""
CLASSIFIERS = [
    'Programming Language :: Python :: %d' % sys.version_info[0],
    'Intended Audience :: Developers',
    'Topic :: Scientific/Engineering',
    'Topic :: Education',
    'License :: OSI Approved :: MIT License',
    'Development Status :: 5 - Production/Stable'
]

#######
# data
#######


class SetupCommandBuildScript(Command):
    description = "Updates grammars."

    user_options = [
        ('g=', None, 'grammar file to recompile, R.g4 for example)')
    ]

    def initialize_options(self):
        self.g = None

    def finalize_options(self):
        pass

    def run(self):
        if self.g is None:
            raise RuntimeError(
                "Expecting a grammar file: python setup.py update_grammars R.g4")
        grammar = self.g
        from pyensae.languages import build_grammar
        if not os.path.exists(grammar):
            cdir = os.path.abspath(os.path.dirname(__file__))
            g2 = os.path.join(cdir, "src", "pyensae", "languages", grammar)
            if not os.path.exists(g2):
                raise FileNotFoundError("{0}\n{1}".format(grammar, g2))
            grammar = g2
        build_grammar(grammar, fLOG=logging_function)
        r = True


packages = find_packages('src', exclude='src')
package_dir = {k: "src/" + k.replace(".", "/") for k in packages}
package_data = {project_var_name + ".subproject": ["*.tohelp"],
                project_var_name + ".languages": ["*.g4", "*.tokens"], }
command = default_cmdclass().copy()
command['update_grammars'] = SetupCommandBuildScript


setup(
    name=project_var_name,
    version=read_version(__file__, project_var_name, subfolder='src'),
    author='Xavier Dupré',
    author_email='xavier.dupre@gmail.com',
    license="MIT",
    url="http://www.xavierdupre.fr/app/pyensae/helpsphinx/index.html",
    download_url="https://github.com/sdpython/pyensae/",
    description=DESCRIPTION,
    long_description=read_readme(__file__),
    cmdclass=command,
    keywords=KEYWORDS,
    classifiers=CLASSIFIERS,
    packages=packages,
    package_dir=package_dir,
    package_data=package_data,
    setup_requires=["pyquicksetup"],
    install_requires=[
        "pyquickhelper>=1.8",
        "numpy>=1.18", "pandas>=1.0", "matplotlib>=3.0"
    ],
    extras_require={
        'graphhelper': ['blockdiag', 'cartopy'],
        'datasource': ['dbread', 'geopandas', 'shapely', 'pyshp', 'pylzma'],
        'finance': ['pandas-datareader', 'yahoo_historical>=0.4'],
        'graphhelper': ['matplotlib>=3.0'],
        'languages': ['antlr4-python3-runtime>=4.8'],
        'notebookhelper': ['folium', 'qgrid'],
        'all': [
            "pyquickhelper>=1.8", "numpy>=1.18", "pandas>=1.0", "matplotlib>=3.0",
            'blockdiag', 'cartopy',
            'dbread', 'geopandas', 'shapely', 'pyshp', 'pylzma',
            'pandas-datareader', 'yahoo_historical>=0.4',
            'antlr4-python3-runtime>=4.8',
            'folium', 'qgrid', 'easydev',
        ],
    },
    entry_points={
        'console_scripts': [
            'file_head = pyensae.cli.head_cli:file_head_cli',
            'file_tail = pyensae.cli.tail_cli:file_tail_cli',
        ]}
)
