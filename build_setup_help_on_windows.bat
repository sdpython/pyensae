
rem uncomment the next three lines if you want to generate the setup for the 64 bit version
set pythonexe64="c:\python33_x64\python"
set pythonexe="c:\python33\python"

%pythonexe% setup.py sdist --formats=gztar,zip --verbose
%pythonexe64% setup.py build bdist_wininst --plat-name=win-amd64
%pythonexe% setup.py bdist_wininst

%pythonexe% make_help.py
xcopy /E /C /I /Y _doc\sphinxdoc\build\html dist\html

rem we open a browser with on the generated help
dist\html\index.html


