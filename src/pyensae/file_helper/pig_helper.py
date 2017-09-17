"""
@file
@brief Hadoop uses a java implementation of Python: Jython.
This provides provides helper around that.

.. versionadded:: 1.1
"""

import os
import glob
from pyquickhelper.loghelper import run_cmd, noLOG
from pyquickhelper.filehelper import change_file_status
from .jython_helper import get_java_cmd, get_java_path
from ..datasource.http_retrieve import download_data

PIG_VERSION = "0.17.0"
HADOOP_VERSION = "2.8.1"


def download_pig_standalone(pig_version=PIG_VERSION,
                            hadoop_version=HADOOP_VERSION, fLOG=noLOG):
    """
    download the standalone jython
    if it does not exists, we should version ``HADOOP_VERSION``
    by default in order to fit the cluster's version

    @param      pig_version         pig_version
    @param      hadoop_version      hadoop_version
    @param      fLOG                logging function
    @return                         location

    This function might need to be run twice if the first try
    fails, it might to due to very long path when unzipping the
    downloaded file.

    Hadoop is downloaded from one of the websites referenced at
    ` <http://www.apache.org/dyn/closer.cgi/hadoop/common/hadoop-2.8.0/hadoop-2.8.0.tar.gz>`_.
    Check the source to see which one was chosen.
    """
    fbs = []

    # download winutils.exe
    d = os.path.join(os.path.abspath(os.path.dirname(__file__)), "winutils")
    if not os.path.exists(d):
        os.mkdir(d)
    exe = download_data(name="winutils.zip",
                        whereTo=d,
                        website="xd",
                        fLOG=fLOG)
    fbs.append(exe)
    change_file_status(d)

    # download hadoop
    fLOG("download hadoop", hadoop_version)
    d = os.path.join(os.path.abspath(os.path.dirname(__file__)), "hadoopjar")
    if not os.path.exists(d):
        os.mkdir(d)
    fn = download_data(name="hadoop-%s.tar.gz" % hadoop_version,
                       whereTo=d,
                       website="http://apache.crihan.fr/dist/hadoop/common/hadoop-%s/" % hadoop_version,
                       fLOG=fLOG)
    fbs.append(fn)
    change_file_status(d)

    # download pig
    fLOG("download pig", pig_version)
    d = os.path.join(os.path.abspath(os.path.dirname(__file__)), "pigjar")
    if not os.path.exists(d):
        os.mkdir(d)
    fn = download_data(name="pig-%s.tar.gz" % pig_version,
                       whereTo=d, silent=True,
                       website="http://apache.crihan.fr/dist/pig/pig-%s/" % pig_version,
                       fLOG=fLOG)
    fbs.append(fn)
    change_file_status(d)
    return fbs


def get_pig_path():
    """
    this function assumes a folder pig ``pigjar``
    is present in this directory, the function returns the folder

    @return     absolute path
    """
    this = os.path.abspath(os.path.dirname(__file__))
    files = [os.path.join(this, _) for _ in os.listdir(this)]
    files = [_ for _ in files if "pig" in _ and os.path.isdir(_)]
    if len(files) == 0:
        raise FileNotFoundError("no pig folder found in " + this)
    if len(files) != 1:
        raise FileNotFoundError(
            "more than one folder found in " +
            this +
            "\n:" +
            "\n".join(files))
    return files[0]


def get_hadoop_path():
    """
    this function assumes a folder pig ``hadoopjar``
    is present in this directory, the function returns the folder

    @return     absolute path
    """
    this = os.path.abspath(os.path.dirname(__file__))
    files = [os.path.join(this, _) for _ in os.listdir(this)]
    files = [_ for _ in files if "hadoop" in _ and os.path.isdir(_)]
    if len(files) == 0:
        raise FileNotFoundError("no hadoop folder found in " + this)
    if len(files) != 1:
        raise FileNotFoundError(
            "more than one folder found in " +
            this +
            "\n:" +
            "\n".join(files))
    return files[0]


def get_pig_jars():
    """
    returns the list of jars to include into the command line in order to run PIG

    @return     list of jars
    """
    path = get_pig_path()
    res = []
    for root, dirs, files in os.walk(path):
        for name in files:
            if os.path.splitext(name)[-1] == ".jar" and "lib" in root:
                if "h1" not in root and "h1" not in name and "h1" not in root \
                   and "hadoop1-runtime" not in name \
                        and "hadoop1-runtime" not in root \
                        and "test" not in root \
                        and "h2" not in name \
                        and ("pig-" + PIG_VERSION + "-withouthadoop-h2") not in name:
                    res.append(os.path.join(root, name))
    return res


def get_hadoop_jars():
    """
    returns the list of jars to include into the command line in order to run HADOOP

    @return     list of jars
    """
    path = get_hadoop_path()
    res = []
    for root, dirs, files in os.walk(path):
        for name in files:
            if os.path.splitext(name)[-1] == ".jar":
                if "sources.jar" not in name and "-test-sources" not in name \
                        and "tests.jar" not in name:
                    res.append(os.path.join(root, name))
    return res


def run_pig(pigfile, argv=None, pig_path=None, hadoop_path=None,
            jython_path=None, timeout=None, logpath="logs",
            pig_version=PIG_VERSION, hadoop_version=HADOOP_VERSION,
            fLOG=noLOG):
    """
    runs a pig script and returns the standard output and error

    @param      pigfile         pig file
    @param      argv            arguments to sned to the command line
    @param      pig_path        path to pig 0.XX.0
    @param      hadoop_path     path to hadoop
    @param      timeout         timeout
    @param      logpath         path to the logs
    @param      pig_version     PIG version (if *pig_path* is not defined)
    @param      hadoop_version  Hadoop version (if *hadoop_path* is not defined)
    @param      fLOG            logging function
    @return                     out, err

    If *pig_path* is None, the function looks into this directory.
    """
    if pig_path is None:
        pig_path = os.path.join(get_pig_path(), "pig-%s" % pig_version)

    if hadoop_path is None:
        hadoop_path = get_hadoop_path()

    java = get_java_path()
    if "JAVA_HOME" not in os.environ:
        os.environ["JAVA_HOME"] = java

    if "PIG_CONF_DIR" not in os.environ:
        os.environ["PIG_CONF_DIR"] = os.path.normpath(
            os.path.join(
                pig_path,
                "conf"))
        if not os.path.exists(os.environ["PIG_CONF_DIR"]):
            raise FileNotFoundError(os.environ["PIG_CONF_DIR"])

    if "HADOOP_HOME" not in os.environ:
        os.environ["HADOOP_HOME"] = hadoop_path
        if not os.path.exists(os.environ["HADOOP_HOME"]):
            raise FileNotFoundError(os.environ["HADOOP_HOME"])

    if "HADOOP_CLIENT_OPTS" not in os.environ:
        os.environ["HADOOP_CLIENT_OPTS"] = "-Xmx1024m"

    fLOG("PIG_CONF_DIR=", os.environ["PIG_CONF_DIR"])

    def clean(i, p):
        if i == 0:
            return p
        if '"' in p:
            p = p.replace('"', '\\"')
        if " " in p:
            p = '"{0}"'.format(p)
        return p

    full = False
    jars = []
    if full:
        jars.extend(get_pig_jars())  # + get_hadoop_jars()
        folds = set(os.path.split(j)[0] for j in jars)
        jars = [os.path.join(f, "*.jar") for f in folds]

        jars.append(
            os.path.join(
                hadoop_path,
                "hadoop-%s" % hadoop_version,
                "share",
                "hadoop",
                "common",
                "lib",
                "*.jar"))
        jars.append(
            os.path.join(
                hadoop_path,
                "hadoop-%s" % hadoop_version,
                "share",
                "hadoop",
                "hdfs",
                "lib",
                "*.jar"))
        jars.append(
            os.path.join(
                hadoop_path,
                "hadoop-%s" % hadoop_version,
                "share",
                "hadoop",
                "mapreduce",
                "lib",
                "*.jar"))
        jars.append(
            os.path.join(
                hadoop_path,
                "hadoop-%s" % hadoop_version,
                "share",
                "hadoop",
                "httpfs",
                "tomcat",
                "lib",
                "*.jar"))
        jars.append(
            os.path.join(
                hadoop_path,
                "hadoop-%s" % hadoop_version,
                "share",
                "hadoop",
                "tools",
                "lib",
                "*.jar"))
        jars.append(
            os.path.join(
                hadoop_path,
                "hadoop-%s" % hadoop_version,
                "share",
                "hadoop",
                "yarn",
                "lib",
                "*.jar"))

        jars.append(
            os.path.join(
                hadoop_path,
                "hadoop-%s" % hadoop_version,
                "share",
                "hadoop",
                "common",
                "hadoop-common-%s.jar" % hadoop_version))
        jars.append(
            os.path.join(
                hadoop_path,
                "hadoop-%s" % hadoop_version,
                "share",
                "hadoop",
                "common",
                "hadoop-nfs-%s" % hadoop_version))
        jars.append(
            os.path.join(
                hadoop_path,
                "hadoop-%s" % hadoop_version,
                "share",
                "hadoop",
                "hdfs",
                "hadoop-hdfs-%s.jar" % hadoop_version))
        jars.append(
            os.path.join(
                hadoop_path,
                "hadoop-2.5.2",
                "share",
                "hadoop",
                "hdfs",
                "hadoop-hdfs-nfs-%s.jar" % hadoop_version))
        jars.append(
            os.path.join(
                hadoop_path,
                "hadoop-%s" % hadoop_version,
                "share",
                "hadoop",
                "mapreduce",
                "*.jar"))
        jars.append(
            os.path.join(
                hadoop_path,
                "hadoop-%s" % hadoop_version,
                "share",
                "hadoop",
                "yarn",
                "*.jar"))

        jars.append(os.path.join(pig_path, "pig-%s-core-h1.jar" % pig_version))
    else:
        jars.append(
            os.path.join(
                pig_path,
                "pig-%s" % pig_version,
                "legacy",
                "pig-%s-withouthadoop-h2.jar" % pig_version))

    jarsall = []
    for j in jars:
        r = glob.glob(j)
        jarsall.extend(r)
    jarsall.sort()
    for j in jarsall:
        fLOG(j)

    jars = ";".join(jars)
    fLOG("jars", jars)

    cmd = [get_java_cmd(), "-Xmx1024m",
           "-classpath", jars,
           "-Dpig.log.dir=" + logpath,
           "-Dhadoop.log.dir=" + logpath,
           "-Dhadoop.tmp.dir=" + logpath,
           "-Dpig.log.file=pid.log",
           "-Djava.io.tmpdir=" + logpath,
           "-Dpig.home.dir=" + pig_path,
           #"-Dpig.schematuple=true",
           #"-Dpig.schematuple.local.dir=" + logpath,
           "org.apache.pig.Main",
           "-x", "local", pigfile,
           "-stop_on_failure"
           ]

    cmd = " ".join(clean(i, _) for i, _ in enumerate(cmd))
    out, err = run_cmd(
        cmd, wait=True, sin=None, communicate=True, timeout=timeout, shell=False)
    return out, err
