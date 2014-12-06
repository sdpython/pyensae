rem we remove everything from dist
echo off
del /Q dist\*.*

rem unittests with python 3.4

IF EXIST c:\Python34vir GOTO next:
mkdir c:\Python34vir

:next:
IF EXIST c:\Python34vir\install GOTO fullsetup:
c:\Python34\Scripts\virtualenv c:\Python34vir\install --system-site-packages
if %errorlevel% neq 0 exit /b %errorlevel%

:fullsetup:

echo #######################################################
c:\Python34vir\install\Scripts\python -u setup.py install
if %errorlevel% neq 0 exit /b %errorlevel%
echo #######################################################

set pythonexe="c:\Python34\python"
%pythonexe% -u setup.py clean_space
%pythonexe% -u setup.py unittests
if %errorlevel% neq 0 exit /b %errorlevel%
echo #######################################################

rem python 3.3

set pythonexe="c:\python33_x64\python"
%pythonexe% clean_pyd.py
%pythonexe% setup.py build bdist_wininst --plat-name=win-amd64
if %errorlevel% neq 0 exit /b %errorlevel%
echo #######################################################

set pythonexe="c:\python33\python"
%pythonexe% clean_pyd.py
%pythonexe% setup.py sdist --formats=gztar,zip --verbose
if %errorlevel% neq 0 exit /b %errorlevel%
%pythonexe% setup.py bdist_wininst
if %errorlevel% neq 0 exit /b %errorlevel%
echo #######################################################

rem python 3.4

set pythonexe="c:\python34_x64\python"
%pythonexe% clean_pyd.py
%pythonexe% setup.py build bdist_wininst --plat-name=win-amd64
if %errorlevel% neq 0 exit /b %errorlevel%
%pythonexe% setup.py build bdist_msi --plat-name=win-amd64
if %errorlevel% neq 0 exit /b %errorlevel%
echo #######################################################

set pythonexe="c:\python34\python"
%pythonexe% clean_pyd.py
%pythonexe% setup.py sdist --formats=gztar,zip --verbose
if %errorlevel% neq 0 exit /b %errorlevel%
%pythonexe% setup.py bdist_wininst
if %errorlevel% neq 0 exit /b %errorlevel%
%pythonexe% setup.py bdist_msi
if %errorlevel% neq 0 exit /b %errorlevel%
echo #######################################################

rem help

%pythonexe% -u setup.py build_sphinx
if %errorlevel% neq 0 exit /b %errorlevel%
echo #######################################################

if not exist dist\html mkdir dist\html
xcopy /E /C /I /Y _doc\sphinxdoc\build\html dist\html
if %errorlevel% neq 0 exit /b %errorlevel%