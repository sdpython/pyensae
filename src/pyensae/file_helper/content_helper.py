"""
@file
@brief Various functions to process text
"""

import os
import re
import chardet


def replace_comma_by_point(file):
    """
    replaces all commas by point in a file (do that inplace)

    @param      file        file to process
    """
    with open(file, "r") as f:
        text = f.read()
    text = text.replace(",", ".")
    with open(file, "w") as f:
        f.write(text)


def file_head(filename: str, nbline=10, encoding="utf8", errors: str=None):
    """
    Extracts the first nbline of a file (assuming it is text file).

    @param      filename        filename
    @param      nbline          number of lines
    @param      encoding        encoding
    @param      errors          see `open <https://docs.python.org/3/library/functions.html#open>`_
    @return                     list of lines
    """
    if isinstance(filename, str):
        if not os.path.exists(filename):
            raise FileNotFoundError(filename)
        if not os.path.isfile(filename):
            raise FileNotFoundError("'{0}' is not a file".format(filename))
        with open(filename, "r", encoding=encoding, errors=errors) as f:
            return file_head(f, nbline=nbline, encoding=encoding)
    else:
        rows = []
        for line in filename:
            rows.append(line)
            if len(rows) >= nbline:
                break
        return rows


def file_tail(filename: str, nbline=10, encoding="utf8", threshold=2 ** 14, errors: str=None):
    """
    Extracts the first nbline of a file (assuming it is text file).

    @param      filename        filename
    @param      nbline          number of lines
    @param      encoding        encoding
    @param      threshold       if the file size is above, it will not read the beginning
    @param      errors          see `open <https://docs.python.org/3/library/functions.html#open>`_
    @return                     list of lines

    The line marked as *A* has an issue because the cursor
    could fall on a character (= byte) in the middle of a character
    if the file is encoded in utf-8 character.
    The next line fails. That's why we try again
    by moving the cursor by one character (see line B).

    The first returned line may be incomplete.
    """
    if not os.path.exists(filename):
        raise FileNotFoundError(filename)
    if not os.path.isfile(filename):
        raise FileNotFoundError("'{0}' is not a file".format(filename))

    size = os.stat(filename).st_size
    if size < threshold:
        with open(filename, "r", encoding=encoding, errors=errors) as f:
            rows = f.readlines()
        return rows[-nbline:] if len(rows) > nbline else rows
    else:
        with open(filename, "r", encoding=encoding, errors=errors) as f:
            f.seek(size - threshold)  # line A
            try:
                content = f.read()
            except UnicodeDecodeError:
                f.seek(size - threshold - 1)  # line B
                content = f.read()

        rows = content.split("\n")
        res = rows[-nbline:] if len(rows) > nbline else rows
        return [_ + "\n" for _ in res]


def enumerate_grep(filename, regex, encoding="utf8", errors=None):
    """
    extract lines matching a regular expression

    @param      filename        filename
    @param      regex           regular expression
    @param      encoding        encoding
    @param      errors          see `open <https://docs.python.org/3/library/functions.html#open>`_
    @return                     iterator in lines

    .. versionadded:: 1.1
    """
    if isinstance(filename, str):
        if not os.path.exists(filename):
            raise FileNotFoundError(filename)
        if not os.path.isfile(filename):
            raise FileNotFoundError("'{0}' is not a file".format(filename))
        with open(filename, "r", encoding=encoding, errors=errors) as f:
            for _ in enumerate_grep(f, regex, encoding):
                yield _
    else:
        reg = re.compile(regex)
        for line in filename:
            if reg.search(line):
                yield line


def file_encoding(filename_or_bytes, limit=2**20):
    """
    Returns the encoding of a file.
    The function relies on `chardet <http://chardet.readthedocs.io/en/latest/usage.html>`_.

    @param      filename_or_bytes       filename or bytes
    @param      limit                   if *filename_or_bytes* is a file, the function only
                                        loads the first *limit* bytes (or all if *limit* is -1)
    @return                             dictionary

    Example of results:

    ::

        {'encoding': 'EUC-JP', 'confidence': 0.99}
    """
    if isinstance(filename_or_bytes, str):
        if not os.path.exists(filename_or_bytes):
            raise FileNotFoundError(filename_or_bytes)
        if not os.path.isfile(filename_or_bytes):
            raise FileNotFoundError(
                "'{0}' is not a file".format(filename_or_bytes))
        size = os.stat(filename_or_bytes).st_size
        with open(filename_or_bytes, "rb") as f:
            content = f.read() if limit == -1 or size < limit else f.read(limit)
        return file_encoding(content)
    elif isinstance(filename_or_bytes, bytes):
        return chardet.detect(filename_or_bytes)
    else:
        raise TypeError("Unexpecting type for filename_or_bytes, got: {0}.".format(
            type(filename_or_bytes)))
