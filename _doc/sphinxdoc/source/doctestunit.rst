.. _l-doctestunit:

Documentation, unit tests, setup
================================

.. contents::
   :depth: 3


    
Unit tests
----------
    
The project includes an easy to write and run unit tests:
    * the file ``_unittests/run_unittests.py`` runs all of them.
    * you can add a new one in a folder: ``_unittests/<subfolder>/test_<filename>.py``.
    
This test file must begin by ``test_`` and must look like the following::

    """
    @brief      test log(time=1s)

    You should indicate a time in seconds. The program ``run_unittests.py``
    will sort all test files by increasing time and run them.
    """

    import sys, os, unittest
    from pyhome3 import fLOG  # it requires pyhome3.

    # to import files from the module
    try :
        import src
    except ImportError :
        path = os.path.normpath(os.path.abspath( os.path.join( os.path.split(__file__)[0], "..", "..")))
        if path not in sys.path : sys.path.append (path)
        import src

    # import the file you want to test 
    from src.project_name.subproject.myexample import myclass

    class TestExample (unittest.TestCase):
        
        def test_split_cmp_command(self) :

            # to log information
            fLOG (__file__, self._testMethodName, OutputPrint = __name__ == "__main__")
            
            # you test content
            # it must raises an exception if a test fails.

    if __name__ == "__main__"  :
        unittest.main ()        

Generation of the documentation
-------------------------------

The program ``make_help.py`` without any required change except mention in the introduction. Just run it. It will go through the following steps:
    * it will copy all files found in ``src`` in folder ``_doc/sphinxdoc/source/project_name``
    * it will generates a file .rst for each python file in ``_doc/sphinxdoc/source/project_name``
    * it will run the generation of the documentation using Sphinx.
    
The results are stored in folder ``_doc/sphinxdoc/build``.

.. warning::
    
    The folder containing the project (here: project_template) must be different from the project name 
    (here: project_name). Otherwise, the generation of the documentation might face some issues while 
    importing modules. The documentation creates another folder, copies every source file
    there, change the doxygen help format into rst format, adds custom summaries.

Generation of the setup
-----------------------

Unless you add an extension or some data to your module (images, text files),
no modification are required. To generate a zip or gz setup::

    %pythonexe% setup.py sdist --formats=gztar,zip
    
To generate an executable setup on Windows::

    %pythonexe% setup.py bdist_wininst

On Windows, the file ``build_setup_help_on_windows.bat`` does everything for you.
