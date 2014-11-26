"""
@file
@brief provides some functionalities to upload file to a website
"""
from ftplib import FTP
import os


from pyquickhelper import noLOG

class TransferFTP (FTP) :
    """
    this class uploads files to a website,
    if the remote does not exists, it creates it first

    .. versionadded:: 1.1

    @example(Transfer files to webste through FTP)

    Simple sketch to transfer a list of ``files`` to
    a website through FTP

    @code
    ftp = TransferFTP('ftp.<website>', alias, password, fLOG=print)

    issues = [ ]
    done = [ ]
    notdone = [ ]
    for file in files :

        try :
            r = ftp.transfer (file, path)
            if r : done.append( (file, path) )
            else : notdone.append ( (file, path) )
        except Exception as e :
            issues.append( (file, e) )

    try :
        ftp.close()
    except Exception as e :
        print ("unable to close FTP connection using ftp.close")

    @endcode
    @endexample
    """

    errorNoDirectory = "Can't change directory"

    def __init__ (self, site, login, password, fLOG = noLOG) :
        """
        constructor

        @param      site        website
        @param      login       login
        @param      password    password
        @param      fLOG        logging function
        """
        FTP.__init__(self, site, login, password)
        self.LOG = fLOG
        self._atts = dict(site=site)

    @property
    def Site(self):
        """
        return the website
        """
        return self._atts["site"]

    def _private_login (self) :
        """
        logs in
        """
        self.LOG ("connecting to ", self.Site)
        FTP.login(self)

    def run_command (self, command, *args) :
        """
        run a FTP command

        @param      command     command
        @param      args        list of argument
        @return                 output of the command or True for success, False for failure
        """
        try :
            t = command (self, *args)
            if command == FTP.pwd or command == FTP.dir:
                return t
            elif command != FTP.cwd :
                self.LOG("    ** run ", str(command), str(args))
            return True
        except Exception as e:
            if TransferFTP.errorNoDirectory in str(e) :
                raise e
            self.LOG (e)
            self.LOG ("    ** run exc ", str(command), str(args))
            self._private_login()
            t = command (self, *args)
            self.LOG ("    ** run ", str(command), str(args))
            return t

    def print_list (self) :
        """
        return the list of files in the current directory
        the function sends eveything to the logging function

        @return         @see me run_command
        """
        return self.run_command(FTP.retrlines,'LIST')

    def close(self) :
        """
        closes the connection
        """
        self.LOG ("disconnecting from", self.Site)
        FTP.disconnect(self)

    def mkd (self, path) :
        """
        creates a directory

        @param        path      path to the directory
        @return                 True or False
        """
        self.LOG("[mkd]", path)
        return self.run_command(FTP.mkd, path)

    def cwd (self, path, create = False) :
        """
        go to a directory, if it does not exist, create it
        (if create is True)

        @param      path        path to the directory
        @param      create      True to create it
        @return                 True or False
        """
        try :
            self.run_command(FTP.cwd, path)
        except Exception as e :
            if create and TransferFTP.errorNoDirectory in str(e) :
                self.mkd (path)
                self.cwd (path, create)
            else :
                raise e

    def pwd (self) :
        """
        Return the pathname of the current directory on the server.

        @return         pathname
        """
        return self.run_command(FTP.pwd)

    def dir(self, path = '.'):
        """
        list the content of a path

        @param      path        path
        @return                 list of path
        """
        return self.run_command(FTP.dir, path)

    def ls(self, path = '.'):
        """
        list the content of a path

        @param      path        path
        @return                 list of path
        """
        return self.run_command(FTP.dir, path)

    def transfer (self, file, to, debug = False) :
        """
        transfers a file

        @param      file        file
        @param      to          destination
        @param      debug       if True, displays more information
        @return                 status
        """
        if not os.path.exists(file):
            raise FileNotFoundError(file)

        path = to.split("/")
        path = [ _ for _ in path if len(_) > 0 ]
        temp = os.path.split(file)[-1]
        self.LOG ("[upload] ", temp, "to", to)

        if debug :
            self.LOG ("    -- path", path)
            self.LOG ("    -- pwd", self.pwd())

        for p in path :
            if debug :  self.LOG ("    -- cwd", p)
            self.cwd(p, True)

        if debug :
            self.LOG ("    -- transferring", file)

        with open(file, "rb") as f :
            r = self.run_command(FTP.storbinary, 'STOR ' + temp, f)

        for p in path :
            if debug :
                self.LOG ("    -- cwd", "..")
            self.cwd("..")

        return r