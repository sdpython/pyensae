"""
@file
@brief Hadoop uses a java implementation of Python: Jython.
This provides provides helper around that.
"""

import os
import sys
import urllib
import urllib.request
from pyquickhelper.loghelper import run_cmd, noLOG

JYTHON_VERSION = "2.7.1-rc2"


def download_java_standalone(version=JYTHON_VERSION):
    """
    download the standalone jython
    if it does not exists, we should version ``JYTHON_VERSION``
    by default in order to fit the cluster's version

    @param      version     ``JYTHON_VERSION`` or ...
    @return                 path to it
    """
    dest = "jython-standalone-%s.jar" % version
    url = "https://search.maven.org/remotecontent?filepath=org/python/jython-standalone/{1}/{0}".format(
          dest, version)
    this = os.path.abspath(os.path.dirname(__file__))
    final = os.path.join(this, dest)
    if os.path.exists(final):
        return final

    try:
        u = urllib.request.urlopen(url)
    except urllib.error.HTTPError as e:
        raise Exception(
            "Unable to download file from '{0}'.".format(url)) from e
    alls = u.read()
    u.close()

    with open(final, "wb") as f:
        f.write(alls)

    return final


def get_java_path():
    """
    returns the java path

    :raises FileNotFoundError: if java is not found
    """
    if "JAVA_HOME" in os.environ:
        java = os.environ["JAVA_HOME"]
    else:
        if sys.platform.startswith("win"):
            location = r'C:\Program Files\Java'
            if not os.path.exists(location):
                raise FileNotFoundError(
                    "path {0} does not exists, you need to install java.\nGo to " +
                    "http://www.oracle.com/technetwork/java/javase/downloads/jre8-downloads-2133155.html")
            pa = os.listdir(location)
            if len(pa) == 0:
                raise FileNotFoundError(
                    "path {0} does not exists, you need to install java.\nGo to " +
                    "http://www.oracle.com/technetwork/java/javase/downloads/jre8-downloads-2133155.html")
            pa = [os.path.join(location, _) for _ in pa]
            for p in pa:
                if os.path.isdir(p) and os.path.exists(p):
                    return p
            raise FileNotFoundError(
                "path {0} does not exists, you need to install java.\nGo to http://www.oracle.com/technetwork/java/javase/downloads/jre8-downloads-2133155.html")
        else:
            java = ""
    return java


def get_java_cmd():
    """
    return the java path

    @return     java cmd
    """
    if sys.platform.startswith("win"):
        java = get_java_path()
        cmd = os.path.join(java, 'bin', 'java.exe')
        if not os.path.exists(cmd):
            raise FileNotFoundError(cmd)
        return '"{0}"'.format(cmd)
    else:
        return "java"


def is_java_installed(fLOG=noLOG):
    """
    this function checks if java is installed

    @return     boolean
    """
    cmd = get_java_cmd() + " -showversion"
    out, err = run_cmd(cmd, wait=True, log_error=False)
    fLOG("OUT:\n", out)
    fLOG("ERR:\n", err)
    return "Java(TM)" in err


def get_jython_jar():
    """
    this function assumes a file ``jython-standalone-x.x.x.jar``
    is present in this directory, the function returns the file

    @return     absolute path
    """
    this = os.path.abspath(os.path.dirname(__file__))
    files = [os.path.join(this, _) for _ in os.listdir(this)]
    files = [_ for _ in files if "jython-standalone" in _]
    if len(files) == 0:
        raise FileNotFoundError("no jython-standalone*.jar found in " + this)
    if len(files) != 1:
        raise FileNotFoundError(
            "more than one jython-standalone*.jar found in " +
            this +
            "\n:" +
            "\n".join(files))
    return files[0]


def run_jython(pyfile,
               argv=None,
               jython_path=None,
               sin=None,
               timeout=None,
               fLOG=noLOG):
    """
    runs a jython script and returns the standard output and error

    @param      pyfile          jython file
    @param      argv            arguments to sned to the command line
    @param      jython_path     path to jython standalone
    @param      sin             data to send to the standard input
    @param      timeout         timeout
    @param      fLOG            logging function
    @return                     out, err

    If *jython_path* is None, the function looks into this directory.
    """
    if jython_path is None:
        jython_path = get_jython_jar()

    def clean(i, p):
        if i == 0:
            return p
        if '"' in p:
            p = p.replace('"', '\\"')
        if " " in p:
            p = '"{0}"'.format(p)
        return p

    cmd = [get_java_cmd(), "-jar", jython_path, pyfile]
    if argv is not None:
        cmd.extend(argv)
    cmd = " ".join(clean(i, _) for i, _ in enumerate(cmd))
    out, err = run_cmd(
        cmd, wait=True, sin=sin, communicate=True, timeout=timeout, shell=False)
    return out, err
