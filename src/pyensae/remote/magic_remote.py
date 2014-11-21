#-*- coding: utf-8 -*-
"""
@file
@brief Magic command to communicate with an Hadoop cluster.
"""
import os, sys

from IPython.core.magic import Magics, magics_class, line_magic, cell_magic
from IPython.core.magic import line_cell_magic
from IPython.core.display import HTML
from .remote_connection import ASSHClient

from pyquickhelper import run_cmd

@magics_class
class MagicRemote(Magics):
    """
    Defines commands to access a remote machine (bridge) through SSH,
    for the time being, all the command do not accept another parameters
    such as a SSH client which means only one connection
    can be opened at the same time.

    The notebooks :ref:`pythonhadooppigrst` and
    :ref:`exampleofsshclientcommunicationrst` show how these commands can be used.
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

    def get_connection(self):
        """
        returns the connection stored in the workspace
        """
        if self.shell is None:
            raise Exception("No detected workspace.")

        if "remote_ssh" not in self.shell.user_ns:
            raise KeyError("No opened SSH connection.")

        return self.shell.user_ns["remote_ssh"]

    @cell_magic
    def PIG(self, line, cell = None):
        """
        defines command ``%%PIG``
        """
        if line in [None, ""] :
            print("Usage:")
            print("     %%PIG <filename>")
            print("")
            print("The command store the content of the cell as a local file.")
        else:
            filename = line.strip()
            with open(filename, "w", encoding="utf8") as f :
                f.write(cell.replace("\r",""))

    @cell_magic
    def PYTHON(self, line, cell = None):
        """
        defines command ``%%PIG``
        """
        if line in [None, ""] :
            print("Usage:")
            print("     %%PYTHON <filename>")
            print("")
            print("The command store the content of the cell as a local file.")
        else:
            filename = line.strip()
            with open(filename, "w", encoding="utf8") as f :
                f.write(cell.replace("\r",""))

    @cell_magic
    def runpy(self, line, cell = None):
        """
        defines command ``%%runpy``

        run a python script which accepts standards input and produces standard outputs,
        a timeout is set up at 10s

        ..versionadded:: 1.1
        """
        if line in [None, ""] :
            print("Usage:")
            print("     %%runpy <pythonfile.py> <args>")
            print("     first row")
            print("     second row")
            print("     ...")
        else:
            filename = line.strip().split()
            if len(filename) == 0:
                self.runpy("")
            else:
                args = " ".join(filename[1:])
                filename = filename[0]
                cmd = sys.executable.replace("pythonw", "python") + " " + filename + " " + args
                tosend = cell
                out,err = run_cmd(cmd, wait=True, sin=tosend, communicate=True, timeout=10, shell=False)
                if len(err) > 0 :
                    return HTML ('<font color="#DD0000">Error</font><br /><pre>\n%s\n</pre>' % err)
                else:
                    return HTML ('<pre>\n%s\n</pre>' % out)

    @line_magic
    def pigsubmit(self, line):
        """
        @see me jobsubmit
        """
        return self.jobsubmit(line)

    @line_magic
    def jobsubmit(self, line):
        """
        defines command ``%jobsubmit``
        """
        if line in [None, ""]:
            print("Usage:")
            print("  %jobsubmit <jobname.pig> [files.py] [redirection] [-local]")
            print("")
            print("The file <jobname.pig> is local.")
            print("Some streaming files can be added such as stream.py. They must have the extension .py.")
            print("If redirection is specified, the standard output and error are redirected to")
            print("redirection.out, redirection.err and the function does not wait.")
            print("If -local is added, the job runs locally (option -x local).")
        else:
            filename = line.strip()
            spl = filename.split()
            if "-local" in spl:
                local = True
                spl = [ _ for _ in spl if _ != "-local" ]
            else:
                local = False

            filename = spl[0]
            pythons = [ _ for _ in spl if _.endswith(".py") ]
            spl = [ _ for _ in spl if not _.endswith(".py") ]

            redirection = None if len(spl) == 1 else spl[1]
            if not os.path.exists(filename):
                raise FileNotFoundError(filename)

            dest = os.path.split(filename)[-1]
            ssh = self.get_connection()
            ssh.upload(filename, dest)
            for py in pythons:
                ssh.upload(py, os.path.split(py)[-1])
            slocal = " -x local" if local else ""

            if redirection is None:
                cmd = "pig{0} -execute -f ".format(slocal) + dest
            else:
                cmd = "pig{2} -execute -f {0} 2> {1}.err 1> {1}.out &".format(filename, redirection, slocal)

            out, err = ssh.execute_command(cmd, no_exception = True)
            if len(err) > 0 and (len(out) == 0 or "ERROR" in err or "FATAL" in err or "Exception" in err):
                return HTML("<pre>\n%s\n</pre>" % err)
            else:
                return HTML("<pre>\n%s\n</pre>" % out)

    @line_magic
    def remote_py(self, line):
        """
        defines command ``%remote_py``
        """
        if line in [None, ""]:
            print("Usage:")
            print("  %remote_py <program.py> [args]")
        else:
            filename = line.strip()
            spl = filename.split()

            filename = spl[0]

            if filename.startswith("[") and filename.endswith("]"):
                # the first parameter is the executable to use
                exe = filename.strip("[]")
                if len(spl) < 2:
                    raise Exception("the command expects a filename: %remote_py [interpreter] filename.py")
                filename = spl[1]
                args = " ".join(spl[2:])
            else:
                exe = "python"
                args = " ".join(spl[1:])

            dest = os.path.split(filename)[-1]
            ssh = self.get_connection()
            ssh.upload(filename, dest)

            cmd = exe + " " + dest + " " + args

            out, err = ssh.execute_command(cmd, no_exception = True)
            if len(err) > 0 :
                return HTML("<b>ERR:</b><br /><pre>\n%s\n</pre><b>OUT:</b><br /><pre>\n%s\n</pre>" % (err, out))
            else:
                return HTML("<pre>\n%s\n</pre>" % out)

    @line_magic
    def jobsyntax(self, line):
        """
        defines command ``%jobsyntax``
        """
        if line in [None, ""]:
            print("Usage:")
            print("  %jobsyntax <jobname.pig>")
            print("")
        else:
            filename = line.strip()
            if not os.path.exists(filename):
                raise FileNotFoundError(filename)

            dest = os.path.split(filename)[-1]
            ssh = self.get_connection()
            ssh.upload(filename, dest)
            out, err = ssh.execute_command("pig -check " + dest, no_exception = True)
            if len(err) > 0 and (len(out) == 0 or "ERROR" in err or "FATAL" in err or "Exception" in err):
                return HTML("<pre>\n%s\n</pre>" % err)
            else:
                return HTML("<pre>\n%s\n</pre>" % out)

    @line_magic
    def remote_open (self, line):
        """
        open a SSH connection and store the connection
        into the notebook workspace
        """
        spl = line.strip().split()
        if len(spl) != 3 and len(spl) != 0:
            print("Usage:")
            print("   remote_open <server> <username> <password>")
            print("   remote_open")
            print("")
            print("No parameter means server, username, password will be found in the workspace")
        else:
            if len(spl)==3:
                server,username,password = spl
            elif self.shell is not None:
                server   = self.shell.user_ns.get("server",None)
                username = self.shell.user_ns.get("username",None)
                password = self.shell.user_ns.get("password",None)
                if server is None : raise KeyError("unable to find server")
                if username is None : raise KeyError("unable to find username")
                if password is None : raise KeyError("unable to find password")
            else:
                raise Exception("No detected workspace.")

            if self.shell is None:
                raise Exception("No detected workspace.")

            ssh = ASSHClient(server, username, password)
            ssh.connect()

            self.shell.user_ns["remote_ssh"] = ssh
            return ssh

    @line_magic
    def remote_close (self, line):
        """
        close a SSH connection and store the connection
        into the notebook workspace
        """
        self.get_connection().close()
        return True

    @line_cell_magic
    def remote_cmd(self, line, cell = None):
        """
        run a command on the remote machine

        Example::

            %remote_cmd ls

        Or::

            %%remote_cmd  <something>
            anything going to stdin

        In the second case, if __PASSWORD__ is found, it will be replaced by the password stored in
        workspace.
        """
        ssh = self.get_connection()

        if isinstance(cell, str):
            cell = self._replace_params(cell)

        out, err = ssh.execute_command(line, no_exception = True, fill_stdin=cell)
        if len(err) > 0 and (len(out) == 0 or "ERROR" in err or "FATAL" in err or "Exception" in err):
            return HTML("<pre>\n%s\n</pre>" % err)
        else:
            return HTML("<pre>\n%s\n</pre>" % out)

    @line_magic
    def remote_up(self, line):
        """
        upload a file to the remote machine,

        Example::

            %remote_up localfile remotepath

        the command does not allow spaces in files
        """
        spl = line.strip().split()
        if len(spl) != 2 :
            print("Usage:")
            print("   remote_up <localfile> <remotepath>")
            print("")
            print("no space allowed in file names")
        else :
            ssh = self.get_connection()
            localfile,remotepath = spl
            if not os.path.exists(localfile) :
                raise FileNotFoundError(localfile)
            ssh.upload(localfile, remotepath)
            return remotepath

    @line_magic
    def remote_up_cluster(self, line):
        """
        upload a file to the remote machine and then to the remote cluster,

        Example::

            %remote_up_cluster localfile remotepath

        the command does not allow spaces in files

        .. versionadded:: 1.1
        """
        spl = line.strip().split()
        if len(spl) != 2 :
            print("Usage:")
            print("   remote_up_cluster <localfile> <remotepath>")
            print("")
            print("no space allowed in file names")
        else :
            ssh = self.get_connection()
            localfile,remotepath = spl
            if not os.path.exists(localfile) :
                raise FileNotFoundError(localfile)
            ssh.upload_cluster(localfile, remotepath)
            return remotepath

    @line_magic
    def remote_down(self, line):
        """
        download a file from the remote machine,

        Example::

            %remote_down remotepath localfile

        the command does not allow spaces in files
        """
        spl = line.strip().split()
        if len(spl) != 2 :
            print("Usage:")
            print("   remote_up <localfile> <remotepath>")
            print("")
            print("no space allowed in file names")
        else :
            ssh = self.get_connection()
            remotepath,localfile = spl
            if os.path.exists(localfile) :
                raise Exception("file {0} cannot be overwritten".format(localfile))
            ssh.download(remotepath,localfile)
            return localfile

    @line_magic
    def open_remote_shell(self, line):
        """
        Defines ``%open_remote_shell``
        """
        ssh = self.get_connection()
        ssh.open_session(out_format="html")
        return True

    @line_magic
    def close_remote_shell(self, line):
        """
        Defines ``%close_remote_shell``
        """
        ssh = self.get_connection()
        ssh.close_session()
        return True

    @line_cell_magic
    def shell_remote(self, line, cell=None):
        """
        Defines ``%shell_remote`` and ``%%shell_remote``
        """
        ssh = self.get_connection()
        if cell is None:
            out = ssh.send_recv_session(line)
        else :
            out = ssh.send_recv_session(cell)

        return HTML(out)

    @line_magic
    def remote_ls(self, line):
        """
        returns the content of a folder as a dataframe

        Example::

            %remote_ls .

        ..versionadded:: 1.1
        """
        ssh = self.get_connection()
        df = ssh.ls(line)
        return df

    @line_magic
    def dfs_ls(self, line):
        """
        returns the content of a folder on the cluster as a dataframe

        Example::

            %dfs_ls .

        ..versionadded:: 1.1
        """
        ssh = self.get_connection()
        df = ssh.dfs_ls(line)
        return df

    @line_magic
    def dfs_rm(self, line):
        """
        remove a file on the cluster

        Example::

            %dfs_rm .

        ..versionadded:: 1.1
        """
        ssh = self.get_connection()
        df = ssh.dfs_rm(line)
        return df

    @line_magic
    def dfs_rmr(self, line):
        """
        remove a folder on the cluster

        Example::

            %dfs_rmr .

        ..versionadded:: 1.1
        """
        ssh = self.get_connection()
        df = ssh.dfs_rm(line, recursive = True)
        return df

    @line_magic
    def dfs_mkdir(self, line):
        """
        create a folder on the cluster

        Example::

            %dfs_mkdir afolder

        ..versionadded:: 1.1
        """
        ssh = self.get_connection()
        df = ssh.dfs_mkdir(line)
        return df


def register_magics():
    """
    register magics function, can be called from a notebook
    """
    from IPython import get_ipython
    ip = get_ipython()
    ip.register_magics(MagicRemote)