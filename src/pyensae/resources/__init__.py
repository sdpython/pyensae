"""
@file
@brief This module gathers various functions about configurations, resources, need modules...
"""


def check_dependency( name ):
    """
    Checks if a library is present.
    It raises an exception if not.
    
    @param      name    name of the library to check
    """
    if name == "pyhome3" :
        try :
            import pyhome3
        except ImportError:
            import sys, os
            ab = os.path.abspath(os.path.split(__file__)[0])
            ab = os.path.join(ab, "..", "..", "..", "..", "..", "pyhome")
            sys.path.append(ab)
            import pyhome3
    else :
        raise Exception("unexpected library name" + name)
    
    