"""
@file
@brief Various functions to get data from a website, a reference website.
"""
import os
import sys
import importlib
import re
import urllib.request
from pyquickhelper.loghelper import noLOG


class DownloadDataException(Exception):
    """
    raised when data cannot be downloaded
    """
    pass


def remove_empty_line(file):
    """
    remove empty line in an imported file

    @param      file        local file name
    """
    try:
        f = open(file, "r")
        lines = f.readlines()
        f.close()
        encoding = None
    except UnicodeDecodeError:
        try:
            f = open(file, "r", encoding="latin-1")
            lines = f.readlines()
            f.close()
            encoding = "latin-1"
        except UnicodeDecodeError:
            f = open(file, "r", encoding="utf8")
            lines = f.readlines()
            f.close()
            encoding = "utf8"

    nbrn = len([_ for _ in lines if _.endswith("\n")])
    lines = [_.rstrip(" \n") for _ in lines]
    nbempty = len([_ for _ in lines if len(_) == 0])
    skip = 0
    if nbempty + nbrn > len(lines) / 3:
        res = lines
        lines = []
        last = -1
        for i, line in enumerate(res):
            if len(line) == 0:
                if last >= i - 2:
                    last = i
                    lines.append(line)
                else:
                    skip += 1
            else:
                lines.append(line)
    if skip > 0:
        with open(file, "w", encoding=encoding) as f:
            f.write("\n".join(lines))


def download_data(name, moduleName=None, url=None, glo=None,
                  loc=None, whereTo=".", website="xd", timeout=None,
                  retry=2, fLOG=noLOG):
    """
    retrieve a module given its name, a text file or a zip file,
    look for it on http://www.xavierdupre.fr/... (website),
    the file is copied at this file location and uncompressed if it is a zip file (or a tar.gz file)

    @param      name        (str) name of the module
    @param      moduleName  (str|None) like import name as moduleName, None for name
    @param      url         (str|None) link to the website to use
    @param      glo         (dict|None) if None, it will be replaced ``globals()``
    @param      loc         (dict|None) if None, it will be replaced ``locals()``
    @param      whereTo     specify a folder where downloaded files will be placed
    @param      website     website to look for
    @param      timeout     timeout (seconds) when establishing the connection (see `urlopen <https://docs.python.org/3/library/urllib.request.html#urllib.request.urlopen>`_)
    @param      retry       number of retries in case of failure when downloading the data
    @param      fLOG        logging function
    @return                 modules or list of files

    By extension, this function also download various zip files and decompresses it.
    If the file was already downloaded, the function will not do it again.

    .. exref::
        :title: Download data for a practical lesson

        ::

            from pyensae import download_data
            download_data('voeux.zip', website = 'xd')

    .. exref::
        :title: Download data from a website

        ::

            download_data("facebook.tar.gz",website="http://snap.stanford.edu/data/")

    If it does not work, I suggest to use standard python:
    `Download a file from Dropbox with Python <http://www.xavierdupre.fr/blog/2015-01-20_nojs.html>`_.

    .. versionchanged:: 1.1
        Parameter *retry* was added.
    """
    from ..file_helper.decompress_helper import decompress_zip, decompress_targz, decompress_gz, decompress_bz2

    if glo is None:
        glo = globals()
    if loc is None:
        loc = locals()

    if website == "xd":
        website = "http://www.xavierdupre.fr/enseignement/complements/"
    elif website == "xdtd":
        website = "http://www.xavierdupre.fr/site2013/enseignements/tddata/"

    if not os.path.exists(whereTo):
        raise FileExistsError("this folder should exists " + whereTo)

    origname = name
    if name in sys.modules:
        return sys.modules[name]
    elif "." not in name:
        fLOG("    unable to find module ", name)

    file = name if "." in name else "%s.py" % name
    outfile = file if whereTo == "." else os.path.join(whereTo, file)

    if not os.path.exists(outfile):
        path = "../../../../complements_site_web"
        f2 = os.path.join(path, file)
        if os.path.exists(f2):
            fLOG("adding file", f2)
            u = open(f2, "r")
            alls = u.read()
            u.close()
        else:
            if url is None:
                url = website
            url += file
            fLOG("    downloading of ", url, " to ", outfile)
            while retry > 0:
                try:
                    u = urllib.request.urlopen(
                        url) if timeout is None else urllib.request.urlopen(url, timeout=timeout)
                    alls = u.read()
                    u.close()
                    break
                except Exception as e:
                    if retry <= 0:
                        raise DownloadDataException(
                            "unable to retrieve data from {0}".format(url)) from e
                    else:
                        fLOG("    fail and retry to download of ",
                             url, " to ", outfile)
                except ConnectionResetError as ee:
                    if retry <= 0:
                        raise DownloadDataException(
                            "unable to retrieve data from {0}".format(url)) from ee
                    else:
                        fLOG("    fail and retry to download of ",
                             url, " to ", outfile)
                retry -= 1
            u = open(outfile, "wb")
            u.write(alls)
            u.close()
    else:
        if name.endswith(".tar.gz") and os.stat(outfile).st_size > 2 ** 20:
            return [outfile]

    if name.endswith(".zip"):
        return decompress_zip(outfile, whereTo, fLOG)

    elif name.endswith(".tar.gz"):
        return decompress_targz(outfile, whereTo, fLOG)

    elif name.endswith(".gz"):
        return decompress_gz(outfile, whereTo, fLOG)

    elif name.endswith(".bz2"):
        return decompress_bz2(outfile, whereTo, fLOG)

    elif "." not in name:
        path, filename = os.path.split(outfile)
        if filename != outfile:
            if path not in sys.path:
                sys.path.append(path)

        remove_empty_line(outfile)

        try:
            temp = importlib.import_module(name)
        except SystemError as e:
            if "Parent module '' not loaded" in str(e):
                reg1 = re.compile("^(from +[.])[a-zA-Z]")
                reg2 = re.compile("^from +[.]{2}")
                fLOG("removing relative import for ", name)
                with open(outfile, "r") as f:
                    lines = f.readlines()
                fil = []
                fir = True
                for l in lines:
                    r1 = reg1.search(l)
                    r2 = reg2.search(l)
                    if r2:
                        l = ""
                        if fir:
                            l = "fLOG = print"
                            fir = False
                    elif r1:
                        st = r1.groups()[0]
                        l = l.replace(st, "from ")
                        if fir:
                            l += "\nfLOG = print"
                            fir = False
                    fil.append(l.strip("\n\r"))
                if not fir:
                    fLOG("end removing relative import for ", name)
                    with open(outfile, "w") as f:
                        f.write("\n".join(fil))

            try:
                temp = importlib.import_module(name)
            except Exception as e:
                fLOG("issue (3) while importing ", name, " -- ", origname)
                fLOG("sys.path ", sys.path)
                for _ in sys.path:
                    fLOG("    path ", _)
                fLOG("sys.modules.keys()", list(sys.modules.keys()))
                for _ in sorted(sys.modules):
                    fLOG("    modules ", _)
                raise e

        except Exception as e:
            fLOG("issue (2) while importing ", name, " -- ", origname)
            fLOG("sys.path ", sys.path)
            for _ in sys.path:
                fLOG("    path ", _)
            fLOG("sys.modules.keys()", list(sys.modules.keys()))
            for _ in sorted(sys.modules):
                fLOG("    modules ", _)
            raise e

        if name not in temp.__name__:
            raise NameError(
                "name should be present in __name__ " +
                name +
                " ? " +
                temp.__name__)
        glo[moduleName] = temp
        sys.modules[moduleName] = temp
        sys.modules[origname] = temp
        return temp

    elif file.split(".")[-1] in ["txt", "csv", "tsv", "xml", "html"]:
        remove_empty_line(outfile)
        return outfile
    else:
        return outfile
