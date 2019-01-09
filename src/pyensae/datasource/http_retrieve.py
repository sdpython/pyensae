"""
@file
@brief Various functions to get data from a website, a reference website.
"""
import os
import sys
import importlib
import re
import time
import urllib.request
from pyquickhelper.loghelper import noLOG


class DownloadDataException(Exception):
    """
    raised when data cannot be downloaded
    """
    pass


class RetrieveDataException(Exception):
    """
    raised when data cannot be downloaded
    """
    pass


def remove_empty_line(file):
    """
    Removes empty line in an imported file.

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
                  retry=2, silent=False, fLOG=noLOG):
    """
    Retrieves a module given its name, a text file or a :epkg:`zip` file,
    looks for it on ``http://www.xavierdupre.fr/...`` (website),
    the file is copied at this file location and uncompressed
    if it is a :epkg:`zip` file (or a :epkg:`tar.gz` file).
    This function can be replaced in most cases by function
    `urlretrieve <https://docs.python.org/3/library/urllib.request.html#urllib.request.urlretrieve>`_.

    ::

        import urllib.request
        url = 'https://...'
        dest = "downloaded_file.bin"
        urllib.request.urlretrieve(url, dest)

    @param      name        (str) name of the file to download
    @param      moduleName  (str|None) like import name as moduleName if *name* is a module
    @param      url         (str|list|None) link to the website to use (or the websites if list)
    @param      glo         (dict|None) if None, it will be replaced ``globals()``
    @param      loc         (dict|None) if None, it will be replaced ``locals()``
    @param      whereTo     specify a folder where downloaded files will be placed
    @param      website     website to look for
    @param      timeout     timeout (seconds) when establishing the connection
                            (see `urlopen <https://docs.python.org/3/library/urllib.request.html#urllib.request.urlopen>`_)
    @param      retry       number of retries in case of failure when downloading the data
    @param      silent      if True, convert some exception into warnings when unzipping a tar file
    @param      fLOG        logging function
    @return                 modules or list of files

    By extension, this function also download various zip files and decompresses it.
    If the file was already downloaded, the function will not do it again.

    .. exref::
        :title: Download data for a practical lesson

        ::

            from pyensae.datasource import download_data
            download_data('voeux.zip', website='xd')

    .. exref::
        :title: Download data from a website

        ::

            download_data("facebook.tar.gz", website="http://snap.stanford.edu/data/")

    If it does not work, I suggest to use standard python:
    `Download a file from Dropbox with Python <http://www.xavierdupre.fr/blog/2015-01-20_nojs.html>`_.

    .. versionchanged:: 1.1
        Parameters *retry*, *silent* were added.

    .. versionchanged:: 1.2
        Parameter *url* can be a list. The function
        tries the first one which contains the file.
    """
    from ..filehelper.decompress_helper import decompress_zip, decompress_targz, decompress_gz, decompress_bz2

    if glo is None:
        glo = globals()
    if loc is None:
        loc = locals()

    def transform_url(w):
        "local function"
        if isinstance(w, list):
            return [transform_url(_) for _ in w]
        if w == "xd":
            w = "http://www.xavierdupre.fr/enseignement/complements/"
        elif w == "xdtd":
            w = "http://www.xavierdupre.fr/site2013/enseignements/tddata/"
        return w

    website = transform_url(website)
    url = transform_url(url)
    if url is None:
        url = website

    if not os.path.exists(whereTo):
        raise FileExistsError("this folder should exists " + whereTo)

    # Multiple downloads.
    if isinstance(url, list):
        single = isinstance(name, str)
        if single:
            name = [name] * len(url)
        if not isinstance(name, list):
            raise TypeError("If url is a list, name be a list too.")
        if len(name) != len(url):
            raise ValueError("url and name must be list of the same size.")
        outfiles = []
        for i, u in enumerate(url):
            res = download_data(name[i], moduleName=moduleName, url=u, glo=glo,
                                loc=loc, whereTo=whereTo, website=website, timeout=timeout,
                                retry=retry, silent=silent, fLOG=fLOG)
            if isinstance(res, list):
                outfiles.extend(res)
            else:
                outfiles.append(res)
                if single and res is not None and os.path.exists(res):
                    break
        return outfiles
    elif isinstance(name, list):
        outfiles = []
        for i, n in enumerate(name):
            res = download_data(n, moduleName=moduleName, url=url, glo=glo,
                                loc=loc, whereTo=whereTo, website=website, timeout=timeout,
                                retry=retry, silent=silent, fLOG=fLOG)
            if isinstance(res, list):
                outfiles.extend(res)
            else:
                outfiles.append(res)
        return outfiles

    # Single download.
    origname = name
    if name in sys.modules:
        return sys.modules[name]
    elif "." not in name:
        fLOG("[download_data] unable to find module '{0}'".format(name))

    file = name if "." in name else "%s.py" % name
    outfile = file if whereTo == "." else os.path.join(whereTo, file)

    if url is not None and not os.path.exists(outfile):
        excs = []
        success = False
        alls = None
        url += file
        fLOG("[download_data]    download '{0}' to '{1}'".format(
            url, outfile))
        while retry > 0:
            try:
                u = urllib.request.urlopen(
                    url) if timeout is None else urllib.request.urlopen(url, timeout=timeout)
                alls = u.read()
                u.close()
                success = True
                break
            except ConnectionResetError as ee:
                if retry <= 0:
                    exc = DownloadDataException(
                        "Unable (1) to retrieve data from '{0}'. Error: {1}".format(url, ee))
                    excs.append(exc)
                    excs.append(ee)
                    break
                else:
                    fLOG("[download_data] (1)  fail and retry to download '{0}' to '{1}'".format(
                        url, outfile))
                    # We wait for 2 seconds.
                    time.sleep(2)
            except Exception as e:
                if retry <= 1:
                    exc = DownloadDataException(
                        "Unable (2) to retrieve data from '{0}'. Error: {1}".format(url, e))
                    excs.append(exc)
                    excs.append(e)
                    break
                else:
                    fLOG("[download_data] (2)  fail and retry to download '{0}' to '{1}'".format(
                        url, outfile))
                    # We wait for 2 seconds.
                    time.sleep(2)
            retry -= 1

        if success and alls is not None:
            u = open(outfile, "wb")
            u.write(alls)
            u.close()
        elif len(excs) > 0:
            raise excs[0]
        else:
            raise DownloadDataException(
                "Unable to retrieve data from '{0}'".format(url))

    if name.endswith(".zip"):
        return decompress_zip(outfile, whereTo, fLOG)

    elif name.endswith(".tar.gz"):
        return decompress_targz(outfile, whereTo, silent=silent, fLOG=fLOG)

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
                fLOG("[download_data] removing relative import for ", name)
                with open(outfile, "r") as f:
                    lines = f.readlines()
                fil = []
                fir = True
                for l in lines:
                    r1 = reg1.search(l)
                    r2 = reg2.search(l)
                    if r2:
                        ls = ""
                        if fir:
                            ls = "fLOG = print"
                            fir = False
                    elif r1:
                        st = r1.groups()[0]
                        ls = ls.replace(st, "from ")
                        if fir:
                            ls += "\nfLOG = print"
                            fir = False
                    fil.append(ls.strip("\n\r"))
                if not fir:
                    fLOG("[download_data] end removing relative import for ", name)
                    with open(outfile, "w") as f:
                        f.write("\n".join(fil))

            try:
                temp = importlib.import_module(name)
            except Exception as e:
                fLOG("[download_data] issue (3) while importing ",
                     name, " -- ", origname)
                fLOG("[download_data] sys.path ", sys.path)
                for _ in sys.path:
                    fLOG("[download_data]     path ", _)
                fLOG("[download_data] sys.modules.keys()",
                     list(sys.modules.keys()))
                for _ in sorted(sys.modules):
                    fLOG("[download_data]     modules ", _)
                raise e

        except Exception as e:
            fLOG("[download_data] issue (2) while importing ",
                 name, " -- ", origname)
            fLOG("[download_data] sys.path ", sys.path)
            for _ in sys.path:
                fLOG("[download_data]     path ", _)
            fLOG("[download_data] sys.modules.keys()", list(sys.modules.keys()))
            for _ in sorted(sys.modules):
                fLOG("[download_data]     modules ", _)
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
