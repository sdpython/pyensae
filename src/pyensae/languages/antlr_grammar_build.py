"""
@file
@brief Helpers to build grammars
This module requires `antlr4 <http://www.antlr.org/>`_.
and `antlr4-python3-runtime <https://pypi.python.org/pypi/antlr4-python3-runtime/>`_.
"""
import os
import sys
from pyquickhelper.loghelper import noLOG


def _is_syntax_is_missing(language):
    """
    Downloads the grammar for a specific language if
    the files is missing.

    @param      language        language: python, sqlite, ...
    @return                     grammar file
    """
    locations = {
        "R": "https://github.com/antlr/grammars-v4/tree/master/r/R.g4",
        "SQLite": "https://github.com/antlr/grammars-v4/blob/master/sqlite/SQLite.g4",
        "Pig": "http://wiki.apache.org/pig/PigLexer",
        "CSharp": "https://github.com/antlr/grammars-v4/tree/master/csharp",
    }

    folder = os.path.dirname(__file__)
    filename = os.path.join(folder, language + ".g4")
    if os.path.exists(filename):
        return filename
    if language in locations:
        raise FileNotFoundError(
            "The grammar {0} is not available, you should get it from {1}".format(
                language,
                locations[language]))
    raise KeyError(
        "unexpected language: {0}, not in {1}".format(
            language,
            ",".join(
                locations.keys())))


def build_grammar(g4, version="4.7.1", fLOG=noLOG):
    """
    Compiles the grammar for a specific file.

    @param      g4          grammar format antlr4
    @param      version     version of *antlr4* to use, 4.7
    @param      fLOG        logging function
    @return                 list of files

    The compilation must be done with `antlr4 <http://www.antlr.org/>`_.
    It generates a lexer and a parser which can be imported in Python.
    The options for the command line are described at:
    `antlr4 options <https://theantlrguy.atlassian.net/wiki/display/ANTLR4/Options>`_.

    .. exref::
        :title: Builds a Antlr4 grammar

        See `grammars-v4 <https://github.com/antlr/grammars-v4>`_

        ::

            build_grammar("R.g4")
    """
    if not g4.endswith(".g4"):
        fold = os.path.abspath(os.path.dirname(__file__))
        g4 = os.path.join(fold, g4 + ".g4")

    url = "http://www.antlr.org/download/antlr-{0}-complete.jar".format(
        version)
    spl = url.split("/")
    domain, name = "/".join(spl[:-1]) + "/", spl[-1]
    folder = os.path.abspath(os.path.dirname(__file__))
    final = os.path.join(folder, name)

    if not os.path.exists(final):
        from ..datasource.http_retrieve import download_data
        name = download_data(name, website=domain, whereTo=folder)
        if not os.path.exists(name):
            raise FileNotFoundError("unable to download: " + url)

    path = os.environ.get("CLASSPATH", "")
    if name not in path:
        path = ".;{0}\\antlr-{1}-complete.jar".format(folder, version)
    else:
        path = ".;{0}\\antlr-{1}-complete.jar;{2}".format(
            folder,
            version,
            os.environ["CLASSPATH"])

    os.environ["CLASSPATH"] = path
    fLOG("CLASSPATH", os.environ["CLASSPATH"])

    # we remove -rc...
    version = version.split("-")[0]

    cmd = "org.antlr.v4.Tool "
    if "Lexer" not in g4:
        cmd += "-Dlanguage=Python3 "
    cmd += g4
    from pyquickhelper.loghelper import run_cmd
    out, err = run_cmd("java " + cmd, wait=True, fLOG=fLOG)

    def compiled():
        if "Lexer" in g4:
            lexer = g4.replace(".g4", ".tokens")
        else:
            lexer = g4.replace(".g4", ".py")
        return os.path.exists(lexer)

    if not compiled() or (len(err) > 0 and "error" in err):

        javapath = r'C:\Program Files\Java\jre7\bin\java.exe'
        os.environ["PATH"] = os.environ["PATH"] + ";" + javapath
        if sys.platform.startswith("win") and os.path.exists(javapath):
            out, err = run_cmd(
                '"' + javapath + '" ' + cmd, wait=True, fLOG=fLOG)
            if not compiled() or (len(err) > 0 and "error" in err):
                raise Exception(
                    "unable to compile: " +
                    final +
                    "\nCLASSPATH:\n" +
                    os.environ["CLASSPATH"] +
                    "\nERR:\n" +
                    err +
                    "\nCMD:\njava " +
                    cmd +
                    "\nYou should do it manually.")
        elif err:
            err_lines = err.split(err)
            err_lines = [_ for _ in err_lines if not _.startswith("warning(")]
            err2 = "\n".join(err_lines).strip("\n ")
            if len(err2) > 0:
                raise Exception(
                    "unable to compile: " +
                    final +
                    "\nCLASSPATH:\n" +
                    os.environ["CLASSPATH"] +
                    "\nERR:\n" +
                    err +
                    "\nCMD:\njava " +
                    cmd)

    if os.environ.get("USERNAME", os.environ.get("USER", "")) in g4:
        dest = os.path.dirname(g4)
        for name in os.listdir(dest):
            if "Parser" not in name and "Lexer" not in name and \
                    "Token" not in name and "Listener" not in name:
                continue
            full = os.path.join(dest, name)
            with open(full, "r", encoding="utf-8") as f:
                content = f.read()
            content1 = content.replace(dest, "")
            if content1 != content:
                fLOG("[build_grammar] modified", name)
                with open(full, "w", encoding="utf-8") as f:
                    f.write(content1)

    return out + "\n---ERR---\n" + err
