set pythonexe="c:\python33\python"
%pythonexe% clean_pyd.py
%pythonexe% setup.py sdist --formats=gztar,zip --verbose

set pythonexe="c:\python33_x64\python"
%pythonexe% clean_pyd.py
%pythonexe% setup.py build bdist_wininst --plat-name=win-amd64

set pythonexe="c:\python33\python"
%pythonexe% clean_pyd.py
%pythonexe% setup.py bdist_wininst

%pythonexe% make_help.py
if not exist dist\html mkdir dist\html
xcopy /E /C /I /Y _doc\sphinxdoc\build\html dist\html

rem we open a browser with on the generated help
rem dist\html\index.html


