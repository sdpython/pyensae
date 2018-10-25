
@echo off
@echo SCRIPT: windows_prefix
if "%1"=="" goto default_value_python:
if "%1"=="default" goto default_value_python:
set pythonexe=%1
goto start_script:

:default_value_python:
set pythonexe=c:\Python370_x64\python

@echo ~SET pythonexe=%pythonexe%

:start_script:
set current=%~dp0
@echo ~SET current=%current%

%pythonexe% -u %current%..\setup.py update_grammars Python3.g4
if %errorlevel% neq 0 exit /b %errorlevel%
%pythonexe% -u %current%..\setup.py update_grammars Pig.g4
if %errorlevel% neq 0 exit /b %errorlevel%
%pythonexe% -u %current%..\setup.py update_grammars CSharpLexer.g4
if %errorlevel% neq 0 exit /b %errorlevel%
%pythonexe% -u %current%..\setup.py update_grammars CSharpParser.g4
if %errorlevel% neq 0 exit /b %errorlevel%
%pythonexe% -u %current%..\setup.py update_grammars R.g4 RFilter.g4
if %errorlevel% neq 0 exit /b %errorlevel%
%pythonexe% -u %current%..\setup.py update_grammars DOT.g4
if %errorlevel% neq 0 exit /b %errorlevel%
%pythonexe% -u %current%..\setup.py update_grammars SimpleWorkflow.g4
if %errorlevel% neq 0 exit /b %errorlevel%
%pythonexe% -u %current%..\setup.py update_grammars SQLite.g4
if %errorlevel% neq 0 exit /b %errorlevel%