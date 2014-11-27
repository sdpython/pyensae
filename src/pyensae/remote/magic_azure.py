#-*- coding: utf-8 -*-
"""
@file
@brief Magic command to run PIG script with Azure.
"""
import sys, os
import pandas

from pyquickhelper import run_cmd

from IPython.core.magic import Magics, magics_class, line_magic, cell_magic
from IPython.core.magic import line_cell_magic
from IPython.core.display import HTML
from .azure_connection import AzureClient, AzureException
from ..file_helper.jython_helper import run_jython, get_jython_jar, is_java_installed, download_java_standalone

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
        Open a connection to blob service.
        It returns objects @see cl AzureClient and `BlobService <http://www.xavierdupre.fr/app/azure-sdk-for-python/helpsphinx/storage/blobservice.html?highlight=blobservice#azure.storage.blobservice.BlobService>`_.

        .. versionchanged:: 1.1
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
            return cl, bs

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
                username        = self.shell.user_ns.get("username",None)
                if server           is None : raise KeyError("unable to find blobstorage")
                if password         is None : raise KeyError("unable to find blobpassword")
                if hadoop_server    is None : raise KeyError("unable to find hadoop_server")
                if hadoop_password  is None : raise KeyError("unable to find hadoop_password")
                if username         is None : raise KeyError("unable to find username")
            else:
                raise Exception("No detected workspace.")

            if self.shell is None:
                raise Exception("No detected workspace.")

            if "remote_azure_blob" in self.shell.user_ns:
                raise Exception("a connection is still open, close it first")

            cl = self.create_client(server, password, hadoop_server, hadoop_password, username = username)
            bs = cl.open_blob_service()
            self.shell.user_ns["remote_azure_blob"] = bs
            return cl, bs

    def create_client(self, account_name, account_key, hadoop_server = None, hadoop_password = None, username = None):
        """
        Create a @see cl AzureClient and stores in the workspace.

        @param      account_name        login
        @param      account_key         password
        @param      hadoop_server       hadoop server
        @param      hadoop_password     hadoop password
        @param      username            username
        """
        if username is None : username = "any"
        cl = AzureClient(account_name, account_key, hadoop_server, hadoop_password, pseudo = username)
        self.shell.user_ns["remote_azure_client"] = cl
        return cl

    @line_magic
    def blob_close (self, line):
        """
        close the connection and store the connection
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
            df = cl.ls(bs, container, remotepath)
            if len(df) > 0 :
                return df [["name","last_modified","content_type","content_length","blob_type"]]
            else:
                return df

    @line_magic
    def blob_lsl(self, line):
        """
        defines command %blob_lse (extended version of blob_ls)
        """
        if line is None or len(line.strip()) == 0:
            print("Usage:")
            print("    blob_ls <container/path>")
            print("or")
            print("    blob_ls </path>")
        else :
            cl, bs = self.get_blob_connection()
            container, remotepath = self._interpret_path(line, cl, bs, True)
            return cl.ls(bs, container, remotepath, add_metadata=True)

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
    def blob_down(self, line):
        """
        download a file from the blob storage

        Example::

            %blob_down remotepath localfile

        the command does not allow spaces in file names
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
    def blob_downmerge(self, line):
        """
        download all files from a folder

        Example::

            %blob_downmerge remotepath localfile

        the command does not allow spaces in file names

        ..versionadded:: 1.1
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
            cl.download_merge(bs, container, remotepath, localfile)
            return localfile

    @line_magic
    def blob_rm(self, line):
        """
        calls blob_delete

        .. versionadded:: 1.1
        """
        return self.blob_delete(line)

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
    def blob_rmr(self, line):
        """
        deletes a folder
        """
        if line is None or len(line.strip()) == 0:
            print("Usage:")
            print("   blob_rmr <container/remotepath>")
            print("or")
            print("   blob_rmr </remotepath>")
        else :
            cl, bs = self.get_blob_connection()
            container, remotepath = self._interpret_path(line, cl, bs)
            cl.delete_folder(bs, container, remotepath)
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
        else:
            filename = line.strip()
            script   = cell.replace("\r","")
            with open(filename, "w", encoding="utf8") as f :
                f.write(script)

    @line_magic
    def hd_pig_submit(self, line):
        """
        defines command ``%hd_pig_submit``
        """
        if line in [None, ""]:
            print("Usage:")
            print("  %hd_pig_submit <jobname.pig> [dependencies.py] [-stop_on_failure]")
            print("")
            print("The file <jobname.pig> is local.")
        else:
            line = line.strip()
            spl  = line.split()
            opt  = [ _ for _ in spl if _.startswith("-") ]
            pys  = [ _ for _ in spl if _.endswith(".py") ]
            pig  = [ _ for _ in spl if _ not in pys and _ not in opt ]
            if len(pig) != 1:
                raise ValueError("unable to interpret line: {0}".format(line))
            pig      = pig [0]
            if not os.path.exists(pig):
                raise FileNotFoundError(pig)

            options = { "stop_on_failure":False }
            options.update( { k.strip("-"):True for k in opt } )

            cl, bs = self.get_blob_connection()
            r = cl.pig_submit(bs, cl.account_name, pig, pys, **options)

            self.shell.user_ns["last_job"] = r
            return r

    @line_magic
    def tail_stderr(self, line):
        """
        defines ``%tail_stderr``
        """
        line = line.strip()
        spl = line.strip().split()
        job = [ _ for _ in spl if _.startswith("job") ]
        nbline = [ _ for _ in spl if not _.startswith("job") ]
        if len(job) == 0 :
            if  self.shell is None or "last_job" not in self.shell.user_ns:
                raise Exception("no submitted jobs found in the workspace")
            else:
                job = self.shell.user_ns["last_job"]["jid"]
        elif len(job) == 1:
            job = job[0]
        else:
            raise Excepion("more than one job to look at:" + ",".join(job))

        if len(nbline)==0:
            nbline = 20
            cont = True
        else:
            try:
                nbline = int(nbline[0])
                cont = True
            except ValueError:
                print("Usage:")
                print("     %tail_stderr [nblines] [job_id]")
                cont = False
                nbline = 0

        if cont:
            cl, bs = self.get_blob_connection()
            out, err = cl.standard_outputs(job, bs, cl.account_name, ".")

            lines = err.split("\n")
            show  = "\n".join( _.strip("\n\r") for _ in lines[-nbline:])
            show  = show.replace("ERROR", '<b><font color="#DD0000">ERROR</font></b>')

            if len(out) > 0 :
                lineo = out.split("\n")
                shoo  = "\n".join( _.strip("\n\r") for _ in lineo[-nbline:])
                return HTML("<pre>\n%s\n</pre><br /><b>OUT:</b><br /><pre>\n%s\n</pre>" % (show, shoo))
            else:
                return HTML("<pre>\n%s\n</pre><br />" % show)

    @cell_magic
    def runjython(self, line, cell = None):
        """
        defines command ``%%runjython``

        run a jython script used for streaming in HDInsight,
        the function appends fake decorator
        a timeout is set up at 10s

        The magic function create another file included the decoration.
        It runs the script with this version of Python.

        See `In a python script how can I ignore Apache Pig's Python Decorators for standalone unit testing <http://stackoverflow.com/questions/18223898/in-a-python-script-how-can-i-ignore-apache-pigs-python-decorators-for-standalon>`_

        ..versionadded:: 1.1
        """
        if line in [None, ""] :
            print("Usage:")
            print("     %%runjython <pythonfile.py> <function_name> <args>")
            print("     first row")
            print("     second row")
            print("     ...")
        else:
            filename = line.strip().split()
            if len(filename) <= 1:
                self.runjython("")
            else:
                args = " ".join(filename[2:])
                func_name = filename[1]
                filename = filename[0]

                with open(filename,'r',encoding="utf8") as pyf :
                    content = pyf.read()
                temp = filename.replace(".py", ".temp.py")
                with open(temp, "w", encoding="utf8") as pyf :
                    pyf.write("""
                            # -*- coding: utf8 -*-
                            if __name__ != '__lib__':
                                def outputSchema(dont_care):
                                    def wrapper(func):
                                        def inner(*args, **kwargs):
                                            return func(*args, **kwargs)
                                        return inner
                                    return wrapper
                            """.replace("                            ",""))
                    pyf.write(content.replace("except Exception,", "except Exception as "))
                    pyf.write("""
                            if __name__ != '__lib__':
                                import sys
                                for row in sys.stdin:
                                    row = row.strip()
                                    res = {0}(row)
                                    sys.stdout.write(str(res))
                                    sys.stdout.write("\\n")
                                    sys.stdout.flush()
                            """.format(func_name).replace("                            ",""))

                cmd = sys.executable.replace("pythonw", "python") + " " + temp + " " + args
                tosend = cell
                out,err = run_cmd(cmd, wait=True, sin=tosend, communicate=True, timeout=10, shell=False)
                if len(err) > 0 :
                    return HTML ('<font color="#DD0000">Error</font><br /><pre>\n%s\n</pre>' % err)
                else:
                    return HTML ('<pre>\n%s\n</pre>' % out)

    @cell_magic
    def jython(self, line, cell = None):
        """
        defines command ``%%runjython``

        run a jython script used for streaming in HDInsight,
        the function appends fake decorator
        a timeout is set up at 10s

        The magic function create another file included the decoration.
        It runs the script with Jython (see the default version)

        See `In a python script how can I ignore Apache Pig's Python Decorators for standalone unit testing <http://stackoverflow.com/questions/18223898/in-a-python-script-how-can-i-ignore-apache-pigs-python-decorators-for-standalon>`_

        ..versionadded:: 1.1
        """
        if line in [None, ""] :
            print("Usage:")
            print("     %%jython <pythonfile.py> <function_name> <args>")
            print("     first row")
            print("     second row")
            print("     ...")
        else:
            filename = line.strip().split()
            if len(filename) <= 1:
                self.jython("")
            else:
                args = " ".join(filename[2:])
                func_name = filename[1]
                filename = filename[0]

                with open(filename,'r',encoding="utf8") as pyf :
                    content = pyf.read()
                temp = filename.replace(".py", ".temp.py")
                with open(temp, "w", encoding="utf8") as pyf :
                    pyf.write("""
                            # -*- coding: utf8 -*-
                            if __name__ != '__lib__':
                                def outputSchema(dont_care):
                                    def wrapper(func):
                                        def inner(*args, **kwargs):
                                            return func(*args, **kwargs)
                                        return inner
                                    return wrapper
                            """.replace("                            ",""))
                    pyf.write(content)
                    pyf.write("""
                            if __name__ != '__lib__':
                                import sys
                                for row in sys.stdin:
                                    row = row.strip()
                                    res = {0}(row)
                                    sys.stdout.write(str(res))
                                    sys.stdout.write("\\n")
                                    sys.stdout.flush()
                            """.format(func_name).replace("                            ",""))

                download_java_standalone()
                tosend = cell
                out,err = run_jython(temp, sin = cell, timeout = 10)
                if len(err) > 0 :
                    return HTML ('<font color="#DD0000">Error</font><br /><pre>\n%s\n</pre>' % err)
                else:
                    return HTML ('<pre>\n%s\n</pre>' % out)


def register_azure_magics():
    """
    register magics function, can be called from a notebook
    """
    from IPython import get_ipython
    ip = get_ipython()
    ip.register_magics(MagicAzure)