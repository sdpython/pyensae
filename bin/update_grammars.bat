
@echo off
@echo SCRIPT: windows_prefix
if "%1"=="" goto default_value_python:
if "%1"=="default" goto default_value_python:
set pythonexe=%1
goto start_script:

:default_value_python:
set pythonexe=python

@echo ~SET pythonexe=%pythonexe%

:start_script:
set current=%~dp0
@echo ~SET current=%current%

%pythonexe% -u %current%..\setup.py update_grammars --g Python3.g4
if %errorlevel% neq 0 exit /b %errorlevel%
%pythonexe% -u %current%..\setup.py update_grammars --g CSharpLexer.g4
if %errorlevel% neq 0 exit /b %errorlevel%
%pythonexe% -u %current%..\setup.py update_grammars --g CSharpParser.g4
if %errorlevel% neq 0 exit /b %errorlevel%
%pythonexe% -u %current%..\setup.py update_grammars --g DOT.g4
if %errorlevel% neq 0 exit /b %errorlevel%
%pythonexe% -u %current%..\setup.py update_grammars --g SimpleWorkflow.g4
if %errorlevel% neq 0 exit /b %errorlevel%
%pythonexe% -u %current%..\setup.py update_grammars --g SQLiteLexer.g4
if %errorlevel% neq 0 exit /b %errorlevel%
%pythonexe% -u %current%..\setup.py update_grammars --g SQLiteParser.g4
if %errorlevel% neq 0 exit /b %errorlevel%
%pythonexe% -u %current%..\setup.py update_grammars --g R.g4 RFilter.g4
if %errorlevel% neq 0 exit /b %errorlevel%