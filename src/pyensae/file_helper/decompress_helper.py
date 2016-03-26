"""
@file
@brief Various functions to decompress files
"""
import zipfile
import tarfile
import os
import gzip
import bz2
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


def decompress_targz(filename, whereTo=".", fLOG=noLOG):
    """
    decompress a tar.gz file

    @param      filename        file to process
    @param      folder          location of the result
    @param      fLOG            logging function
    @return                     return the list of decompressed files
    """
    tfile = tarfile.open(filename, 'r:gz')
    files = tfile.getmembers()
    tfile.extractall(whereTo)
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
