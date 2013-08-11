
rem uncomment the next three lines if you want to generate the setup for the 64 bit version
rem set pythonexe="c:\python33_x64\python"
rem %pythonexe% setup.py build bdist_wininst --plat-name=win-amd64

set pythonexe="c:\python33\python"
%pythonexe% setup.py sdist --formats=gztar,zip --verbose
%pythonexe% setup.py bdist_wininst

%pythonexe% make_help.py
xcopy /E /C /I /Y _doc\sphinxdoc\build\html dist\html

rem we open a browser with on the generated help
dist\html\index.html


