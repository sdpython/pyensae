#-*- coding: utf-8 -*-
"""
@file
@brief Magic command to run PIG script with Azure.
"""
import sys, os
import pandas

from IPython.core.magic import Magics, magics_class, line_magic, cell_magic
from IPython.core.magic import line_cell_magic
from IPython.core.display import HTML
from .azure_connection import AzureClient, AzureException

@magics_class
class MagicAzure(Magics):
    """
    Defines magic commands to access `blob storage <http://azure.microsoft.com/fr-fr/documentation/articles/storage-dotnet-how-to-use-blobs/>`_
    and `HDInsight <http://azure.microsoft.com/fr-fr/services/hdinsight/>`_.

    When the container is not specified, it will take the default one.
    """

    def _replace_params(self, cell):
        """
        replaces parameter such ``__PASSWORD__`` by variable in the notebook environment

        @param  cell    string
        @return         modified string
        """
        if "__PASSWORD__" in cell and self.shell is not None and "password" in self.shell.user_ns:
            cell = cell.replace("__PASSWORD__", self.shell.user_ns["password"])
        return cell

    def get_blob_connection(self):
        """
        returns the connection stored in the workspace
        """
        if self.shell is None:
            raise Exception("No detected workspace.")

        if "remote_azure_client" not in self.shell.user_ns:
            raise KeyError("No opened Azure connection.")

        if "remote_azure_blob" not in self.shell.user_ns:
            raise KeyError("No opened Blob Storage connection.")

        cl = self.shell.user_ns["remote_azure_client"]
        bs = self.shell.user_ns["remote_azure_blob"]
        return cl, bs

    @line_magic
    def open_blob(self, line):
        """
        @see me open_blob
        """
        return self.blob_open(line)

    @line_magic
    def azureclient(self,line):
        """
        returns the AzureClient object
        """
        cl, bs = self.get_blob_connection()
        return cl

    @line_magic
    def blobservice(self,line):
        """
        returns the BlobService object
        """
        cl, bs = self.get_blob_connection()
        return bs

    @line_magic
    def blob_open (self, line):
        """
        open a connection to blob service
        """
        spl = line.strip().split()
        if len(spl) != 3 and len(spl) != 0:
            print("Usage:")
            print("   blob_open <blobstorage> <blobpassword>")
            print("   blob_open")
            print("")
            print("No parameter means blobstorage, blobpassword will be found in the workspace")
        else:
            if len(spl)==2:
                server,password = spl
            elif self.shell is not None:
                server   = self.shell.user_ns.get("blobstorage",None)
                password = self.shell.user_ns.get("blobpassword",None)
                if server is None : raise KeyError("unable to find blobstorage")
                if password is None : raise KeyError("unable to find blobpassword")
            else:
                raise Exception("No detected workspace.")

            if self.shell is None:
                raise Exception("No detected workspace.")

            if "remote_azure_blob" in self.shell.user_ns:
                raise Exception("a connection is still open, close it first")

            cl = self.create_client(server, password)
            bs = cl.open_blob_service()
            self.shell.user_ns["remote_azure_blob"] = bs
            return bs

    @line_magic
    def hd_open (self, line):
        """
        open a connection to blob service
        """
        spl = line.strip().split()
        if len(spl) != 3 and len(spl) != 0:
            print("Usage:")
            print("   hd_open <blobstorage> <blobpassword> <hadoop_server> <hadoop_password>")
            print("   hd_open")
            print("")
            print("No parameter means blobstorage, blobpassword, hadoop_server, hadoop_password will be found in the workspace.")
            print("HDInsight is able to work with multiple blob storage.")
            print("Only one is allowed here.")
        else:
            if len(spl)==4:
                server,password,hadoop_server,hadoop_password = spl
            elif self.shell is not None:
                server          = self.shell.user_ns.get("blobstorage",None)
                password        = self.shell.user_ns.get("blobpassword",None)
                hadoop_server   = self.shell.user_ns.get("hadoop_server",None)
                hadoop_password = self.shell.user_ns.get("hadoop_password",None)
                if server           is None : raise KeyError("unable to find blobstorage")
                if password         is None : raise KeyError("unable to find blobpassword")
                if hadoop_server    is None : raise KeyError("unable to find hadoop_server")
                if hadoop_password  is None : raise KeyError("unable to find hadoop_password")
            else:
                raise Exception("No detected workspace.")

            if self.shell is None:
                raise Exception("No detected workspace.")

            if "remote_azure_blob" in self.shell.user_ns:
                raise Exception("a connection is still open, close it first")

            cl = self.create_client(server, password, hadoop_server, hadoop_password)
            bs = cl.open_blob_service()
            self.shell.user_ns["remote_azure_blob"] = bs
            return bs

    def create_client(self, account_name, account_key, hadoop_server = None, hadoop_password = None):
        """
        Create a @see cl AzureClient and stores in the workspace.

        @param      account_name        login
        @param      account_key         password
        @param      hadoop_server       hadoop server
        @param      hadoop_password     hadoop password
        """
        cl = AzureClient(account_name, account_key, hadoop_server, hadoop_password)
        self.shell.user_ns["remote_azure_client"] = cl
        return cl

    @line_magic
    def close_blob(self, line):
        """
        @see me close_blob
        """
        return self.blob_close(line)

    @line_magic
    def blob_close (self, line):
        """
        close a SSH connection and store the connection
        into the notebook workspace
        """
        cl, bs = self.get_blob_connection()
        #bs.close()
        del self.shell.user_ns["remote_azure_blob"]
        return True

    @line_magic
    def blob_containers(self, line):
        """
        returns the list of containers
        """
        cl, bs = self.get_blob_connection()
        res = bs.list_containers()
        return [ r.name for r in res ]

    @line_magic
    def ls_blob(self, line):
        """
        @see me blob_ls
        """
        return self.blob_ls(line)

    def _interpret_path(self, line, cl, bs, empty_is_value = False):
        """
        Interpret a path

        @param      line                line
        @param      cl                  @see cl AzureClient
        @param      bs                  blob service
        @param      empty_is_value      if True, do not raise an exception
        @return                         container, remotepath
        """
        line = line.strip()
        if line.startswith("/"):
            container = cl.account_name
            line = line.lstrip("/")
            remotepath = line
        else:
            spl = line.split("/")
            container = spl[0]
            remotepath = None if len(spl)==1 else "/".join(spl[1:])

        if not empty_is_value and len(remotepath)==0:
            raise FileNotFoundError("path should not be empty: " + line)

        return container, remotepath

    @line_magic
    def blob_ls(self, line):
        """
        defines command %blob_ls
        """
        if line is None or len(line.strip()) == 0:
            print("Usage:")
            print("    blob_ls <container/path>")
            print("or")
            print("    blob_ls </path>")
        else :
            cl, bs = self.get_blob_connection()
            container, remotepath = self._interpret_path(line, cl, bs, True)
            l = cl.ls(bs, container, remotepath)
            return pandas.DataFrame(l)

    @line_magic
    def up_blob(self, line):
        """
        @see me blob_up
        """
        return self.blob_up(line)

    @line_magic
    def blob_up(self, line):
        """
        upload a file to the blob storage,
        we assume the container is the first element of the path

        Example::

            %blob_up localfile remotepath

        the command does not allow spaces in files
        """
        spl = line.strip().split()
        if len(spl) != 2 :
            print("Usage:")
            print("   blob_up <localfile> <container/remotepath>")
            print("or")
            print("   blob_up <localfile> </remotepath>")
        else :
            localfile,remotepath = spl
            if not os.path.exists(localfile) :
                raise FileNotFoundError(localfile)

            cl, bs = self.get_blob_connection()
            container,remotepath = self._interpret_path(remotepath, cl, bs)
            cl.upload(bs, container, remotepath, localfile)
            return remotepath

    @line_magic
    def down_blob(self, line):
        """
        @see me blob_down
        """
        return self.blob_down(line)

    @line_magic
    def blob_down(self, line):
        """
        download a file from the blob storage

        Example::

            %blob_down remotepath localfile

        the command does not allow spaces in files
        """
        spl = line.strip().split()
        if len(spl) != 2 :
            print("Usage:")
            print("   blob_down <container/remotepath> <localfile>")
            print("or")
            print("   blob_down </remotepath> <localfile>")
        else :
            remotepath,localfile = spl
            if os.path.exists(localfile) :
                raise Exception("file {0} cannot be overwritten".format(localfile))

            cl, bs = self.get_blob_connection()
            container,remotepath = self._interpret_path(remotepath, cl, bs)
            cl.download(bs, container, remotepath, localfile)
            return localfile

    @line_magic
    def blob_delete(self, line):
        """
        deletes a blob
        """
        if line is None or len(line.strip()) == 0:
            print("Usage:")
            print("   blob_delete <container/remotepath>")
            print("or")
            print("   blob_delete </remotepath>")
        else :
            cl, bs = self.get_blob_connection()
            container, remotepath = self._interpret_path(line, cl, bs)
            cl.delete_blob(bs, container, remotepath)
            return True

    @line_magic
    def blob_copy(self, line):
        """
        deletes a blob
        """
        spl = line.strip().split()
        if len(spl) != 2 :
            print("Usage:")
            print("   blob_copy <container/source> <container/dest>")
            print("or")
            print("   blob_copy </source> </dest>")
        else :
            src,dest = spl
            cl, bs = self.get_blob_connection()
            container,src  = self._interpret_path(src, cl, bs)
            container_,dest = self._interpret_path(dest, cl, bs)
            if container != container_:
                raise AzureException("containers should be the same: {0} != {1}".format(container, container_), None)
            cl.copy_blob(bs, container, dest, src)
            return True

    @line_magic
    def hd_queue(self, line):
        """
        defines ``%hq_queue``
        """
        showall = line in ["showall", "1", 1, "True", True, "true"]
        cl, bs = self.get_blob_connection()
        return cl.job_queue(showall = showall)

    @line_magic
    def hd_job_status(self, line):
        """
        defines ``%hd_job_status``
        """
        line = line.strip()
        if len(line) == 0 :
            print("Usage:")
            print("    hd_job_status <jobid>")
        else:
            jobid = line
            cl, bs = self.get_blob_connection()
            return cl.job_status(jobid)

    @line_magic
    def hd_job_kill(self, line):
        """
        defines ``%hd_job_kill``
        """
        line = line.strip()
        if len(line) == 0 :
            print("Usage:")
            print("    hd_job_kill <jobid>")
        else:
            jobid = line
            cl, bs = self.get_blob_connection()
            return cl.job_kill(jobid)

    @line_magic
    def hd_wasb_prefix(self, line):
        """
        defines ``%hd_wasb_prefix``
        """
        cl, bs = self.get_blob_connection()
        return cl.wasb_to_file(cl.account_name)

    @cell_magic
    def PIG_azure(self, line, cell = None):
        """
        defines command ``%%PIG_azure``
        """
        if line in [None, ""] :
            print("Usage:")
            print("     %%PIG_azure <filename>")
            print("")
            print("The command store the content of the cell as a local file.")
            print("It also replaces __CONTAINER__ as a right prefix for streams.")
        else:
            filename = line.strip()
            script = cell.replace("\r","")
            cl, bs = self.get_blob_connection()
            prefix = cl.wasb_prefix(cl.account_name)
            script = script.replace("__CONTAINER__", prefix + "/")
            with open(filename, "w", encoding="utf8") as f :
                f.write(script)

    @line_magic
    def hd_pig_submit(self, line):
        """
        defines command ``%hd_pig_submit``
        """
        if line in [None, ""]:
            print("Usage:")
            print("  %hd_pig_submit <jobname.pig>")
            print("")
            print("The file <jobname.pig> is local.")
        else:
            line = line.strip()
            if not os.path.exists(line):
                raise FileNotFoundError(line)

            username = self.shell.user_ns["username"] if "username" in self.shell.user_ns else os.environ.get("USERNAME","nouser")
            remote   = "scripts/pig/{0}/{1}".format(username, os.path.split(line)[-1])
            sd       = "scripts/run/{0}".format(username)

            cl, bs = self.get_blob_connection()
            cl.upload(bs, cl.account_name, remote, line)
            r = cl.pig_submit(cl.account_name,remote,status_dir=sd)
            return r

    @line_magic
    def tail_stderr(self, line):
        """
        defines ``%tail_stderr``
        """
        line = line.strip()
        if len(line) == 0 :
            nbline = 30
            cont = True
        else:
            try:
                nbline = int(line)
                cont = True
            except ValueError:
                print("Usage:")
                print("     %tail_stderr [nblines]")
                cont = False
                nbline = 0

        if cont:
            username = self.shell.user_ns["username"] if "username" in self.shell.user_ns else os.environ.get("USERNAME","nouser")
            #remote   = "scripts/pig/{0}/{1}".format(username, os.path.split(line)[-1])
            sd       = "scripts/run/{0}".format(username)
            loc      = "stderr"
            sd      += "/" + loc
            loc     += ".txt"

            if os.path.exists(loc):
                os.remove(loc)

            cl, bs = self.get_blob_connection()
            fi = cl.download(bs, cl.account_name, sd, loc)
            with open(fi, "r") as f : lines = f.readlines()
            nb = min(nbline, len(lines))
            show = "\n".join( _.strip("\n\r") for _ in lines[-nb:])
            return HTML("<pre>\n%s\n</pre>" % show)



def register_azure_magics():
    """
    register magics function, can be called from a notebook
    """
    from IPython import get_ipython
    ip = get_ipython()
    ip.register_magics(MagicAzure)