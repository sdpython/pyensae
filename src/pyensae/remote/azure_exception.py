# -*- coding: utf-8 -*-
"""
@file
@brief An specific exception for Azure
"""


class AzureException(Exception):

    """
    exception raised by @see cl AzureClient
    """

    def __init__(self, message, ret):
        """
        store more information than a regular exception

        @param      message             error message
        @param      ret                 results of the requests
        """
        Exception.__init__(self, message)

        if ret is not None:
            code = ret.status_code
            try:
                js = ret.json()
            except Exception as e:
                js = str(e) + "\n" + str(ret)

            self.ret = (code, js, ret)
        else:
            self.ret = (None, None)

    def __str__(self):
        """
        usual
        """
        s = Exception.__str__(self)
        f = "STATUS: {0}, JSON: {1}\n{2}\nREQUEST:\n{3}".format(
            self.ret[0], self.ret[1], s, self.ret[2])
        return f
