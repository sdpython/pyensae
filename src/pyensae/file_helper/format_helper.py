"""
@file
@brief Various functions to display information about files
"""

import datetime


def format_file_size(size):
    """
    format the file size as string

    @param      size        numeric value
    @return                 string (something + unit)
    """
    if size >= 2 ** 30:
        size = size / 2 ** 30
        return "%1.2f Gb" % size
    elif size >= 2 ** 20:
        size = size / 2 ** 20
        return "%1.2f Mb" % size
    elif size >= 2 ** 10:
        size = size / 2 ** 10
        return "%1.2f Kb" % size
    else:
        return "%d" % size


def format_file_mtime(timestamp):
    """
    return a datetime for a file

    @param      timestamp       modified date for example
    @return                     datetime
    """
    return datetime.datetime.fromtimestamp(timestamp)
