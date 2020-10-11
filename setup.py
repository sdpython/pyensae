# -*- coding: utf-8 -*-
import sys
import os
from distutils.core import setup
from setuptools import find_packages

#########
# settings
#########

project_var_name = "pyensae"
versionPython = "%s.%s" % (sys.version_info.major, sys.version_info.minor)
path = "Lib/site-packages/" + project_var_name
readme = 'README.rst'
history = "HISTORY.rst"
requirements = None

KEYWORDS = project_var_name + ', ENSAE, sqllite, database, teachings'
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

packages = find_packages('src', exclude='src')
package_dir = {k: "src/" + k.replace(".", "/") for k in packages}
package_data = {project_var_name + ".subproject": ["*.tohelp"],
                project_var_name + ".languages": ["*.g4", "*.tokens"], }

############
# functions
############


def ask_help():
    return "--help" in sys.argv or "--help-commands" in sys.argv


def is_local():
    file = os.path.abspath(__file__).replace("\\", "/").lower()
    if "/temp/" in file and "pip-" in file:
        return False
    try:
        from pyquickhelper.pycode.setup_helper import available_commands_list
    except ImportError:
        return False
    if "update_grammars" in sys.argv:
        return True
    return available_commands_list(sys.argv)


def verbose():
    print("---------------------------------")
    print("package_dir =", package_dir)
    print("packages    =", packages)
    print("package_data=", package_data)
    print("current     =", os.path.abspath(os.getcwd()))
    print("---------------------------------")

##########
# version
##########


if is_local() and not ask_help():
    def write_version():
        from pyquickhelper.pycode import write_version_for_setup
        return write_version_for_setup(__file__)

    write_version()

    versiontxt = os.path.join(os.path.dirname(__file__), "version.txt")
    if os.path.exists(versiontxt):
        with open(versiontxt, "r") as f:
            lines = f.readlines()
        subversion = "." + lines[0].strip("\r\n ")
        if subversion == ".0":
            raise Exception("Git version is wrong: '{0}'.".format(subversion))
    else:
        raise FileNotFoundError(versiontxt)
else:
    # when the module is installed, no commit number is displayed
    subversion = ""

if "upload" in sys.argv and not subversion and not ask_help():
    # avoid uploading with a wrong subversion number
    raise Exception(
        "Git version is empty, cannot upload, is_local()={0}, pyquickhelper={1}".format(is_local()))

##############
# common part
##############

if os.path.exists(readme):
    with open(readme, "r", encoding='utf-8-sig') as f:
        long_description = f.read()
else:
    long_description = ""
if os.path.exists(history):
    with open(history, "r", encoding='utf-8-sig') as f:
        long_description += f.read()

if "--verbose" in sys.argv:
    verbose()

if is_local():
    import pyquickhelper
    logging_function = pyquickhelper.get_fLOG()
    logging_function(OutputPrint=True)
    from pyquickhelper.pycode import process_standard_options_for_setup
    r = process_standard_options_for_setup(
        sys.argv, __file__, project_var_name,
        layout=["html"],
        unittest_modules=["pyquickhelper", "jyquickhelper", "pymyinstall"],
        requirements=["pyquickhelper", "jyquickhelper", "pymyinstall"],
        additional_notebook_path=["pyquickhelper", "jyquickhelper"],
        coverage_options=dict(
            omit=["*Parser.py", "*Listener.py", "*Lexer.py"]),
        github_owner='sdpython', fLOG=logging_function,
        covtoken=("f929c9b3-bf00-4928-906a-b1dc54d5a5d9", "'_UT_37_std' in outfile"))
    if not r and "update_grammars" in sys.argv:
        # expecting python setup.py update_grammars file
        ind = sys.argv.index("update_grammars")
        if len(sys.argv) <= ind:
            raise Exception(
                "expecting a grammar file: python setup.py update_grammars R.g4")
        grammar = sys.argv[ind + 1]
        try:
            from pyensae.languages import build_grammar
        except ImportError:
            from src.pyensae.languages import build_grammar
        if not os.path.exists(grammar):
            cdir = os.path.abspath(os.path.dirname(__file__))
            g2 = os.path.join(cdir, "src", "pyensae", "languages", grammar)
            if not os.path.exists(g2):
                raise FileNotFoundError("{0}\n{1}".format(grammar, g2))
            grammar = g2
        build_grammar(grammar, fLOG=logging_function)
        r = True
    if not r and not ({"bdist_msi", "sdist",
                       "bdist_wheel", "publish", "publish_doc", "register",
                       "upload_docs", "bdist_wininst", "build_ext"} & set(sys.argv)):
        raise Exception("unable to interpret command line: " + str(sys.argv))
else:
    r = False

if ask_help():
    from pyquickhelper.pycode import process_standard_options_for_setup_help
    process_standard_options_for_setup_help(sys.argv)

if not r:

    def import_pyensae():
        try:
            import pyensae
        except ImportError:
            p = os.path.normpath(
                os.path.abspath(
                    os.path.join(
                        os.path.dirname(__file__),
                        "src")))
            sys.path.append(p)
            import pyensae

    if len(sys.argv) in (1, 2) and sys.argv[-1] in ("--help-commands",):
        from pyquickhelper.pycode import process_standard_options_for_setup_help
        process_standard_options_for_setup_help(sys.argv)

    import_pyensae()
    from pyquickhelper.pycode import clean_readme
    from pyensae import __version__ as sversion
    long_description = clean_readme(long_description)

    setup(
        name=project_var_name,
        version=sversion,
        author='Xavier Dupré',
        author_email='xavier.dupre@gmail.com',
        license="MIT",
        url="http://www.xavierdupre.fr/app/pyensae/helpsphinx/index.html",
        download_url="https://github.com/sdpython/pyensae/",
        description=DESCRIPTION,
        long_description=long_description,
        keywords=KEYWORDS,
        classifiers=CLASSIFIERS,
        packages=packages,
        package_dir=package_dir,
        package_data=package_data,
        setup_requires=["pyquickhelper"],
        install_requires=[
            "pyquickhelper>=1.8",
            "numpy>=1.18", "pandas>=1.0", "matplotlib>=3.0"
        ],
        extras_require={
            'graphhelper': ['blockdiag', 'cartopy'],
            'datasource': ['dbread', 'geopandas', 'shapely', 'pyshp', 'pylzma'],
            'finance': ['pandas-datareader', 'yahoo_historical'],
            'graphhelper': ['matplotlib>=3.0'],
            'languages': ['antlr4-python3-runtime>=4.8'],
            'notebookhelper': ['folium', 'qgrid'],
            'all': [
                "pyquickhelper>=1.8", "numpy>=1.18", "pandas>=1.0", "matplotlib>=3.0",
                'blockdiag', 'cartopy',
                'dbread', 'geopandas', 'shapely', 'pyshp', 'pylzma',
                'pandas-datareader', 'yahoo_historical',
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
