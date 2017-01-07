"""
@file
@brief Shortcuts to file_helper
"""

from .content_helper import replace_comma_by_point
from .decompress_helper import decompress_zip, decompress_targz, decompress_gz
from .jython_helper import run_jython, get_jython_jar, is_java_installed, download_java_standalone
from .content_helper import file_head, file_tail, enumerate_grep, file_encoding
