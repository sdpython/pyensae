# -*- coding: utf-8 -*-
#  Copyright (C) 2013 ---------------
#  All rights reserved.
#
#  Redistribution and use in source and binary forms, with or without
#  modification, are permitted provided that the following conditions
#  are met:
#
#  1. Redistributions of source code must retain the above copyright
#     notice, this list of conditions and the following disclaimer.
#
#  2. Redistributions in binary form must reproduce the above copyright
#     notice, this list of conditions and the following disclaimer in
#     the documentation and/or other materials provided with the
#     distribution.
#
#  3. All advertising materials mentioning features or use of this
#     software must display the following acknowledgment:
#     "This product includes software developed by
#      Xavier Dupré <xavier.dupre AT gmail.com>"
#
#  4. Redistributions of any form whatsoever must retain the following
#     acknowledgment:
#     "This product includes software developed by
#      Xavier Dupré <xavier.dupre AT gmail.com>."
#
#  THIS SOFTWARE IS PROVIDED BY Xavier Dupré ``AS IS'' AND ANY
#  EXPRESSED OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
#  IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR
#  PURPOSE ARE DISCLAIMED.  IN NO EVENT SHALL Roman V. Kiseliov OR
#  ITS CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
#  SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT
#  NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
#  LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION)
#  HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT,
#  STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
#  ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED
#  OF THE POSSIBILITY OF SUCH DAMAGE.

import sys,os
from distutils.core import setup
from setuptools import find_packages

if os.path.exists("version.txt") :
    with open("version.txt", "r") as f : lines = f.readlines()
    subversion = lines[0].strip("\r\n ")
else :
    subversion = 1

project_var_name    = "pyensae"
sversion            = "1.1"
versionPython       = "%s.%s" % (sys.version_info.major, sys.version_info.minor)
path                = "Lib/site-packages/" + project_var_name
readme              = 'README.rst'


KEYWORDS = \
project_var_name + ', ENSAE, sqllite, database, teachings'

DESCRIPTION = \
"""Helpers for teaching purposes (includes sqllite helpers)"""

CLASSIFIERS = \
[
'Programming Language :: Python :: 3',
'Intended Audience :: Developers',
'Topic :: Scientific/Engineering',
'Topic :: Education',
'License :: OSI Approved :: BSD License',
'Development Status :: 5 - Production/Stable'
]


if "bdist_wininst" not in sys.argv :
    EXT_MODULES = [
                    #Extension(project_var_name + '.subproject.sample_module',
                    #    ['src/' + project_var_name + '/subproject/sample_module.cpp'],
                    #    include_dirs = ['src/' + project_var_name + '/subproject']),
                ]
else :
    EXT_MODULES = [ ]

packages     = find_packages('src', exclude='src')
package_dir  = { k: "src/" + k.replace(".","/") for k in packages }
package_data = { project_var_name + ".subproject": ["*.tohelp"],
                 project_var_name + ".languages": ["*.g4", "*.tokens"], }

if os.path.exists(readme):
    try:
        with open(readme, "r", encoding='utf-8') as f : long_description = f.read()
        long_description = long_description.replace("\ufeff","")
    except :
        try:
            with open(readme, "r") as f : long_description = f.read()
        except:
            long_description = ""
else:
    long_description = ""

def import_pyquickhelper():
    try:
        import pyquickhelper
    except ImportError:
        sys.path.append ( os.path.normpath (os.path.abspath(os.path.join("..", "pyquickhelper", "src" ))))
        try:
            import pyquickhelper
        except ImportError as e :
            raise ImportError("module pyquickhelper is needed to build the documentation ({0})".format(sys.executable)) from e
    return pyquickhelper

if "--verbose" in sys.argv :
    print ("---------------------------------")
    print ("package_dir =",package_dir)
    print ("packages    =",packages)
    print ("package_data=",package_data)
    print ("current     =", os.path.abspath(os.getcwd()))
    print ("---------------------------------")

if "clean_space" in sys.argv:
    pyquickhelper = import_pyquickhelper()

    fold = os.path.dirname(__file__)
    fold = os.path.abspath(fold)
    rem  = pyquickhelper.remove_extra_spaces_folder(fold, extensions=[".py","rst",".bat",".sh"])
    print("number of impacted files", len(rem))

elif "clean_pyd" in sys.argv:
    pyquickhelper = import_pyquickhelper()
    pyquickhelper.clean_exts()

elif "build_sphinx" in sys.argv:
    pyquickhelper = import_pyquickhelper()

    if "--help" in sys.argv:
        print(pyquickhelper.get_help_usage())
    else :

        if not os.path.exists("_doc/sphinxdoc/source"):
            raise FileNotFoundError("you must get the source from GitHub to build the documentation")

        from pyquickhelper import fLOG, generate_help_sphinx

        fLOG (OutputPrint = True)
        project_name = os.path.split(os.path.split(os.path.abspath(__file__))[0])[-1]
        generate_help_sphinx(project_name)

elif "unittests" in sys.argv:

    if not os.path.exists("_unittests"):
        raise FileNotFoundError("you must get the source from GitHub to run the unittests")

    run_unit = os.path.join("_unittests", "run_unittests.py")
    if not os.path.exists(run_unit):
        raise FileNotFoundError("the folder should contain run_unittests.py")

    pyquickhelper = import_pyquickhelper()
    pyquickhelper.main_wrapper_tests(run_unit, add_coverage=True)

else :

    setup(
        name                    = project_var_name,
        version                 = '%s.%s' %(sversion, subversion) if "register" in sys.argv or "sdist" in sys.argv or "bdist_wheel" in sys.argv or "bdist_msi" in sys.argv or "install" in sys.argv  else 'py%s-%s.%s' % (versionPython, sversion, subversion),
        author                  = 'Xavier Dupré',
        author_email            = 'xavier.dupre AT gmail.com',
        url                     = "http://www.xavierdupre.fr/app/pyensae/helpsphinx/index.html",
        download_url            = "https://github.com/sdpython/pyensae/",
        description             = DESCRIPTION,
        long_description        = long_description,
        keywords                = KEYWORDS,
        classifiers             = CLASSIFIERS,
        packages                = packages,
        package_dir             = package_dir,
        package_data            = package_data,
        #data_files              = data_files,
        install_requires        = [  "pyquickhelper" ],
        ext_modules             = EXT_MODULES,
        #include_package_data    = True,
        )