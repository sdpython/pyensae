"""
@file
@brief Various functions to decompress files
"""
import zipfile
import tarfile
import os
import gzip
import bz2
import warnings
import copy
from tarfile import ExtractError
from pyquickhelper.loghelper import noLOG


def decompress_zip(filename, whereTo=".", fLOG=noLOG):
    """
    unzip a zip file

    @param      filename        file to process
    @param      whereTo         location of the result
    @param      fLOG            logging function
    @return                     return the list of decompressed files
    """
    file = zipfile.ZipFile(filename, "r")
    files = []
    for info in file.infolist():
        if not os.path.exists(info.filename):
            data = file.read(info.filename)
            tos = os.path.join(whereTo, info.filename)
            if not os.path.exists(tos):
                finalfolder = os.path.split(tos)[0]
                if not os.path.exists(finalfolder):
                    fLOG("    creating folder ", finalfolder)
                    os.makedirs(finalfolder)
                if not info.filename.endswith("/"):
                    u = open(tos, "wb")
                    u.write(data)
                    u.close()
                    files.append(tos)
                    fLOG("    unzipped ", info.filename, " to ", tos)
            elif not tos.endswith("/"):
                files.append(tos)
        elif not info.filename.endswith("/"):
            files.append(info.filename)
    return files


def extractall_silent(self, path=".", members=None, *, numeric_owner=False, silent=False):
    """Extract all members from the archive to the current working
       directory and set owner, modification time and permissions on
       directories afterwards. `path' specifies a different directory
       to extract to. `members' is optional and must be a subset of the
       list returned by getmembers(). If `numeric_owner` is True, only
       the numbers for user/group names are used and not the names.

    Same function as `TarFile.extractall <https://github.com/python/cpython/blob/master/Lib/tarfile.py>`_
    but raises a warning if something wrong happens if silent is True.
    """
    directories = []

    if members is None:
        members = self

    for tarinfo in members:
        if tarinfo.isdir():
            # Extract directories with a safe mode.
            directories.append(tarinfo)
            tarinfo = copy.copy(tarinfo)
            tarinfo.mode = 0o700
        # Do not set_attrs directories, as we will do that further down
        if silent:
            try:
                self.extract(tarinfo, path, set_attrs=not tarinfo.isdir(),
                             numeric_owner=numeric_owner)
            except FileNotFoundError as e:
                warnings.warn(
                    "[TarFile.extractall_silent] issue with '{0}' - {1}".format(path, e))
        else:
            self.extract(tarinfo, path, set_attrs=not tarinfo.isdir(),
                         numeric_owner=numeric_owner)

    # Reverse sort directories.
    directories.sort(key=lambda a: a.name)
    directories.reverse()

    # Set correct owner, mtime and filemode on directories.
    for tarinfo in directories:
        dirpath = os.path.join(path, tarinfo.name)
        try:
            self.chown(tarinfo, dirpath, numeric_owner=numeric_owner)
            self.utime(tarinfo, dirpath)
            self.chmod(tarinfo, dirpath)
        except ExtractError as e:
            if self.errorlevel > 1:
                raise
            else:
                self._dbg(1, "tarfile: %s" % e)


def decompress_targz(filename, whereTo=".", silent=True, fLOG=noLOG):
    """
    Decompress a tar.gz file.

    @param      filename        file to process
    @param      folder          location of the result
    @param      silent          raise a warning instead of an error
    @param      fLOG            logging function
    @return                     return the list of decompressed files

    .. versionchanged::
        Parameter *silent* was added.
    """
    tfile = tarfile.open(filename, 'r:gz')
    files = tfile.getmembers()
    extractall_silent(tfile, whereTo, silent=silent)
    t = [os.path.join(whereTo, f.name) for f in files]
    return [f for f in t if os.path.isfile(f)]


def decompress_gz(filename, whereTo=".", fLOG=noLOG):
    """
    decompress a tar.gz file

    @param      filename        file to process
    @param      folder          location of the result
    @param      fLOG            logging function
    @return                     return the list of decompressed files (only one)
    """
    if not filename.endswith(".gz"):
        raise NameError("the file should end with .gz: " + filename)
    dest = os.path.join(whereTo, filename[:-3])
    with gzip.open(filename, 'rb') as f:
        with open(dest, "wb") as g:
            g.write(f.read())
    return [dest]


def decompress_bz2(filename, whereTo=".", fLOG=noLOG):
    """
    decompress a bz2 file

    @param      filename        file to process
    @param      folder          location of the result
    @param      fLOG            logging function
    @return                     return the list of decompressed files (only one)
    """
    if not filename.endswith(".bz2"):
        raise NameError("the file should end with .bz2: " + filename)
    dest = os.path.join(whereTo, filename[:-3])
    with bz2.open(filename, 'rb') as f:
        with open(dest, "wb") as g:
            g.write(f.read())
    return [dest]
