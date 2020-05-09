"""
@file
@brief Shortcuts to datasource
"""
from .convert import dBase2df, dBase2sqllite
from .geodata import load_french_departements
from .http_retrieve import download_data, DownloadDataException
