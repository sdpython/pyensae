"""
@file
@brief Helpers around building language grammar.
This module requires `antlr4 <https://pypi.python.org/pypi/antlr4-python3-runtime/>`_.
"""
import os, sys

def _is_syntax_is_missing(language):
    """
    download the grammar for a specific language if 
    the files is missing
    
    @param      language        language: python, sqlite, ...
    @return                     grammar file    
    """
    locations = {
        "R":        "https://github.com/antlr/grammars-v4/tree/master/r/R.g4",
        "SQLite":   "https://github.com/antlr/grammars-v4/blob/master/sqlite/SQLite.g4",
        "Pig":      "http://wiki.apache.org/pig/PigLexer",
        }
    
    folder = os.path.dirname(__file__)
    filename = os.path.join(folder, language + ".g4")
    if os.path.exists(filename):
        return filename
    if language in locations:
        raise FileNotFoundError("The grammar {0} is not available, you should get it from {1}".format(language, locations[language]))
    else:
        raise KeyError("unexpected language: {0}, not in {1}".format(language, ",".join( locations.keys() ) ) )
        
def build_grammar(g4):
    """
    compile the grammar for a specific file
    
    @param      g4      grammar format antlr4
    @return             list of files
    
    The compilation must be done with `antlr4 <http://www.antlr.org/>`_.
    It generates a lexer and a parser which can be imported in Python.
    The options for the command line are described at: `antlr4 options <https://theantlrguy.atlassian.net/wiki/display/ANTLR4/Options>`_.
    """
    if not g4.endswith(".g4"):
        g4 = g4 + ".g4"
        
    version = "4.4"
    
    url = "http://www.antlr.org/download/antlr-{0}-complete.jar".format(version)
    spl = url.split("/")
    domain,name = "/".join(spl[:-1])+"/", spl[-1]
    folder = os.path.abspath(os.path.dirname(__file__))
    final = os.path.join(folder, name)
    if not os.path.exists(final):
        from ..resources.http_retrieve import download_data
        name = download_data(name, website=domain,whereTo=folder)
        print(name)
        if not os.path.exists(name):
            raise FileNotFoundError("unable to download: " + url)
    path = os.environ.get("CLASSPATH","")
    if name not in path:
        path = ".;{0}\antlr-{1}-complete.jar;%CLASSPATH%".format(folder,version)
        os.environ["CLASSPATH"] = path
    else:
        path = ".;{0}\antlr-{1}-complete.jar;%CLASSPATH%".format(folder,version)
        os.environ["CLASSPATH"] = os.environ["CLASSPATH"] + ";" + path
    
    cmd = "org.antlr.v4.Tool -Dlanguage=Python3 " + g4
    from pyquickhelper import run_cmd
    out,err= run_cmd("java " + cmd, wait=True)
    
    if len(err)>0:
        
        javapath = r"C:\Program Files\Java\jre7\bin"
        os.environ["PATH"] = os.environ["PATH"] + ";" + javapath
        if sys.platform.startswith("win") and os.path.exists(javapath):
            cp = os.path.abspath(folder)
            out,err= run_cmd("java " + cmd, wait=True)
            if len(err)>0:
                raise Exception("unable to compile: " + final + "\nERR:\n" + err + "\nCMD:\njava " + cmd + "\nYou should do it manually.")
        else:
            raise Exception("unable to compile: " + final + "\nERR:\n" + err + "\nCMD:\njava " + cmd)
    
    return out

    