#-*- coding: utf-8 -*-
"""
@file
@brief Magic command to communicate with an Hadoop cluster (Linux).
"""
import os

from IPython.core.magic import magics_class, line_magic, cell_magic
from IPython.core.magic import line_cell_magic
from IPython.core.display import HTML
from pyquickhelper.ipythonhelper import MagicClassWithHelpers, MagicCommandParser
from .ssh_remote_connection import ASSHClient


@magics_class
class MagicRemoteSSH(MagicClassWithHelpers):

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

    @staticmethod
    def PIG_parser():
        """
        defines the way to parse the magic command ``%%PIG``
        """
        parser = MagicCommandParser(prog="PIG",
                                    description='The command store the content of the cell as a local file.')
        parser.add_argument(
            'file',
            type=str,
            help='file name')
        return parser

    @cell_magic
    def PIG(self, line, cell=None):
        """
        defines command ``%%PIG``

        .. nbref::
            :tag: Hadoop
            :title: PIG

            The code for magic command ``%PIG`` is equivalent to::

                with open(filename, "w", encoding="utf8") as f:
                    f.write(script)


        """
        parser = self.get_parser(MagicRemoteSSH.PIG_parser, "PIG")
        args = self.get_args(line, parser)

        if args is not None:
            filename = args.file
            with open(filename, "w", encoding="utf8") as f:
                f.write(cell.replace("\r", ""))

    @staticmethod
    def HIVE_parser():
        """
        defines the way to parse the magic command ``%%HIVE``
        """
        parser = MagicCommandParser(prog="HIVE",
                                    description='The command store the content of the cell as a local file.')
        parser.add_argument(
            'file',
            type=str,
            help='file name')
        return parser

    @cell_magic
    def HIVE(self, line, cell=None):
        """
        defines command ``%%HIVE``

        .. nbref::
            :tag: Hadoop
            :title: HIVE

            The code for magic command ``%HIVE`` is equivalent to::

                with open(filename, "w", encoding="utf8") as f:
                    f.write(script)


        """
        parser = self.get_parser(MagicRemoteSSH.HIVE_parser, "HIVE")
        args = self.get_args(line, parser)

        if args is not None:
            filename = args.file
            with open(filename, "w", encoding="utf8") as f:
                f.write(cell.replace("\r", ""))

    @staticmethod
    def pig_submit_parser():
        """
        defines the way to parse the magic command ``%pig_submit``
        """
        parser = MagicCommandParser(prog="pig_submit",
                                    description='Submits a job to the cluster, the job is local, the job ' +
                                    'is first uploaded to the cluster. The magic command populates the local variable last_job with the submitted job id.')
        parser.add_argument(
            'file',
            type=str,
            help='file name')
        parser.add_argument(
            '-d',
            '--dependency',
            nargs="*",
            type=str,
            help='dependency of the job, the python script')
        parser.add_argument(
            '-l',
            '--local',
            action='store_true',
            default=False,
            help='run locally on the bridge or on the cluster (default)')
        parser.add_argument(
            '-r',
            '--redirection',
            type=str,
            default="redirection.pig",
            help='list of options for the job')
        parser.add_argument(
            '--raw-output',
            default=False,
            action='store_true',
            help='display raw text instead of HTML')
        parser.add_argument(
            '-s',
            '--stop_on_failure',
            action='store_true',
            default=False,
            help='if true, the job stops on failure right away')
        parser.add_argument(
            '-o',
            '--option',
            nargs='*',
            type=str,
            help='list of options for the job')
        return parser

    @line_magic
    def pig_submit(self, line):
        """
        defines command ``%pig_submit``

        .. nbref::
            :tag: Hadoop
            :title: pig_submit

            The code for magic command ``%pig_submit`` is equivalent to::

                ssh = ASSHClient(server, username, password)
                ssh.connect()
                out, err = ssh.pig_submit(
                    pig, dependencies=dependencies, redirection=redirection, local=local, stop_on_failure=stop_on_failure)
                ssh.close()

        """
        parser = self.get_parser(
            MagicRemoteSSH.pig_submit_parser, "pig_submit")
        args = self.get_args(line, parser)

        if args is not None:
            pig = args.file
            pys = [_ for _ in args.dependency if _.endswith(
                ".py")] if args.dependency is not None else []
            redirection = None if args.redirection in [
                None, "None", "", "-"] else args.redirection

            ssh = self.get_connection()
            out, err = ssh.pig_submit(
                pig, dependencies=pys, redirection=redirection, local=args.local, stop_on_failure=args.stop_on_failure)

            if args.raw_output:
                if len(err) > 0 and (
                        len(out) == 0 or "ERROR" in err or "FATAL" in err or "Exception" in err):
                    return err
                else:
                    return out
            else:
                if len(err) > 0 and (
                        len(out) == 0 or "ERROR" in err or "FATAL" in err or "Exception" in err):
                    return HTML("<pre>\n%s\n</pre>" % err)
                else:
                    return HTML("<pre>\n%s\n</pre>" % out)

    @staticmethod
    def hive_submit_parser():
        """
        defines the way to parse the magic command ``%hive_submit``
        """
        parser = MagicCommandParser(prog="hive_submit",
                                    description='Submits a job to the cluster, the job is local, the job is first uploaded to the cluster. The magic ' +
                                    'command populates the local variable last_job with the submitted job id.')
        parser.add_argument(
            'file',
            type=str,
            help='file name')
        parser.add_argument(
            '-r',
            '--redirection',
            type=str,
            default="redirection",
            help='list of options for the job')
        parser.add_argument(
            '--raw-output',
            default=False,
            action='store_true',
            help='display raw text instead of HTML')
        return parser

    @line_magic
    def hive_submit(self, line):
        """
        defines command ``%hive_submit``

        .. nbref::
            :tag: Hadoop
            :title: hive_submit

            The code for magic command ``%hive_submit`` is equivalent to::

                ssh = ASSHClient(server, username, password)
                ssh.connect()
                out, err = ssh.hive_submit(
                    pig, redirection=redirection, local=local)
                ssh.close()

        """
        parser = self.get_parser(
            MagicRemoteSSH.hive_submit_parser, "hive_submit")
        args = self.get_args(line, parser)

        if args is not None:
            pig = args.file
            ssh = self.get_connection()
            out, err = ssh.hive_submit(
                pig, redirection=args.redirection, local=args.local)

            if args.raw_output:
                if len(err) > 0 and (
                        len(out) == 0 or "ERROR" in err or "FATAL" in err or "Exception" in err):
                    return err
                else:
                    return out
            else:
                if len(err) > 0 and (
                        len(out) == 0 or "ERROR" in err or "FATAL" in err or "Exception" in err):
                    return HTML("<pre>\n%s\n</pre>" % err)
                else:
                    return HTML("<pre>\n%s\n</pre>" % out)

    @staticmethod
    def remote_py_parser():
        """
        defines the way to parse the magic command ``%remote_py``
        """
        parser = MagicCommandParser(prog="remote_py",
                                    description='run a python script on the bridge')
        parser.add_argument(
            'file',
            type=str,
            help='file name')
        parser.add_argument(
            'args',
            nargs='*',
            type=str,
            help='list of options for the job')
        parser.add_argument(
            '-i',
            '--interpreter',
            type=str,
            default='python',
            help='change the interpreter, python by default')
        parser.add_argument(
            '--raw-output',
            default=False,
            action='store_true',
            help='display raw text instead of HTML')
        return parser

    @line_magic
    def remote_py(self, line):
        """
        defines command ``%remote_py``

        .. nbref::
            :tag: Hadoop
            :title: remote_py

            The code for magic command ``%remote_py`` is equivalent to::

                ssh = ASSHClient(server, username, password)
                ssh.connect()
                ssh.upload(filename, dest)
                args = " ".join('"{}"'.format(_)
                                for _ in args.args) if args.args is not None else ""
                out, err = ssh.execute_command(exe + " " + dest + " " + args, no_exception=True)
                ssh.close()


        """
        parser = self.get_parser(
            MagicRemoteSSH.remote_py_parser, "remote_py")
        args = self.get_args(line, parser)

        if args is not None:
            filename = args.file
            exe = args.interpreter
            args = " ".join('"{}"'.format(_)
                            for _ in args.args) if args.args is not None else ""

            dest = os.path.split(filename)[-1]
            ssh = self.get_connection()
            ssh.upload(filename, dest)

            cmd = exe + " " + dest + " " + args

            out, err = ssh.execute_command(cmd, no_exception=True)
            if args.raw_output:
                if len(err) > 0:
                    return err
                else:
                    return out
            else:
                if len(err) > 0:
                    return HTML(
                        "<b>ERR:</b><br /><pre>\n%s\n</pre><b>OUT:</b><br /><pre>\n%s\n</pre>" % (err, out))
                else:
                    return HTML("<pre>\n%s\n</pre>" % out)

    @staticmethod
    def job_syntax_parser():
        """
        defines the way to parse the magic command ``%job_syntax``
        """
        parser = MagicCommandParser(prog="remote_py",
                                    description='check syntax of a pig job')
        parser.add_argument(
            'file',
            type=str,
            help='file name')
        parser.add_argument(
            '--raw-output',
            default=False,
            action='store_true',
            help='display raw text instead of HTML')
        return parser

    @line_magic
    def job_syntax(self, line):
        """
        defines command ``%job_syntax``
        """
        parser = self.get_parser(
            MagicRemoteSSH.job_syntax_parser, "job_syntax")
        args = self.get_args(line, parser)

        if args is not None:
            filename = args.file
            if not os.path.exists(filename):
                raise FileNotFoundError(filename)

            ssh = self.get_connection()
            out, err = ssh.pig_submit(filename, check=True, no_exception=True)
            if args.raw_output:
                if len(err) > 0 and (
                        len(out) == 0 or "ERROR" in err or "FATAL" in err or "Exception" in err):
                    return err
                else:
                    return out
            else:
                if len(err) > 0 and (
                        len(out) == 0 or "ERROR" in err or "FATAL" in err or "Exception" in err):
                    return HTML("<pre>\n%s\n</pre>" % err)
                else:
                    return HTML("<pre>\n%s\n</pre>" % out)

    @staticmethod
    def remote_open_parser():
        """
        defines the way to parse the magic command ``%remote_open``
        """
        parser = MagicCommandParser(prog="remote_open",
                                    description='open a remote SSH connection tp the bridge')
        parser.add_argument(
            '-s',
            '--server',
            type=str,
            default='server',
            help='server name')
        parser.add_argument(
            '-u',
            '--username',
            type=str,
            default='username',
            help='username')
        parser.add_argument(
            '-p',
            '--password',
            type=str,
            default='password',
            help='password')
        return parser

    @line_magic
    def remote_open(self, line):
        """
        open a SSH connection and store the connection
        into the notebook workspace

        .. nbref::
            :tag: Hadoop
            :title: remote_open

            The code for magic command ``%remote_open`` is equivalent to::

                ssh = ASSHClient(server, username, password)
                ssh.connect()


        """
        parser = self.get_parser(
            MagicRemoteSSH.remote_open_parser, "remote_open")
        args = self.get_args(line, parser)

        if args is not None:
            if self.shell is None:
                raise Exception("No detected workspace.")

            ssh = ASSHClient(args.server, args.username, args.password)
            ssh.connect()

            self.shell.user_ns["remote_ssh"] = ssh
            return ssh

    @line_magic
    def remote_close(self, line):
        """
        close a SSH connection and store the connection
        into the notebook workspace

        .. nbref::
            :tag: Hadoop
            :title: remote_close

            The code for magic command ``%remote_close`` is equivalent to::

                ssh = ASSHClient(server, username, password)
                # ... ssh.connect()
                ssh.close()


        """
        self.get_connection().close()
        return True

    @line_cell_magic
    def remote_cmd(self, line, cell=None):
        """
        run a command on the remote machine

        Example::

            %remote_cmd ls

        Or::

            %%remote_cmd  <something>
            anything going to stdin

        In the second case, if __PASSWORD__ is found, it will be replaced by the password stored in
        workspace.

        .. nbref::
            :tag: Hadoop
            :title: remote_cmd

            The code for magic command ``%remote_cmd`` is equivalent to::

                ssh = ASSHClient(server, username, password)
                ssh.connect()
                out, err = ssh.execute_command(
                    line, no_exception=True, fill_stdin=cell)
                ssh.close()


        """
        if "--help" in line:
            print("Usage: %remote_cmd <cmd>")
        else:
            ssh = self.get_connection()

            if isinstance(cell, str):
                cell = self._replace_params(cell)

            out, err = ssh.execute_command(
                line, no_exception=True, fill_stdin=cell)
            if len(err) > 0 and (
                    len(out) == 0 or "ERROR" in err or "FATAL" in err or "Exception" in err):
                return HTML("<pre>\n%s\n</pre>" % err)
            else:
                return HTML("<pre>\n%s\n</pre>" % out)

    @line_cell_magic
    def remote_cmd_text(self, line, cell=None):
        """
        run a command on the remote machine and returns raw text (not HTML)

        Example::

            %remote_cmd_text ls

        Or::

            %%remote_cmd_text  <something>
            anything going to stdin

        In the second case, if __PASSWORD__ is found, it will be replaced by the password stored in
        workspace.
        """
        if "--help" in line:
            print("Usage: %remote_cmd_text <cmd>")
        else:
            ssh = self.get_connection()

            if isinstance(cell, str):
                cell = self._replace_params(cell)

            out, err = ssh.execute_command(
                line, no_exception=True, fill_stdin=cell)
            if len(err) > 0 and (
                    len(out) == 0 or "ERROR" in err or "FATAL" in err or "Exception" in err):
                return err
            else:
                return out

    @staticmethod
    def remote_up_parser():
        """
        defines the way to parse the magic command ``%remote_up``
        """
        parser = MagicCommandParser(prog="remote_up",
                                    description='upload a file to the remote machine')
        parser.add_argument(
            'localfile',
            type=str,
            help='local file to upload')
        parser.add_argument(
            'remotepath',
            type=str,
            help='remote path of the uploaded file')
        return parser

    @line_magic
    def remote_up(self, line):
        """
        upload a file to the remote machine,

        Example::

            %remote_up localfile remotepath

        the command does not allow spaces in files

        .. nbref::
            :tag: Hadoop
            :title: remote_up

            The code for magic command ``%remote_up`` is equivalent to::

                ssh = ASSHClient(server, username, password)
                ssh.connect()
                ssh.upload(localfile, remotepath)
                ssh.close()


        """
        parser = self.get_parser(MagicRemoteSSH.remote_up_parser, "remote_up")
        args = self.get_args(line, parser)

        if args is not None:
            localfile, remotepath = args.localfile, args.remotepath
            if not os.path.exists(localfile):
                raise FileNotFoundError(localfile)
            ssh = self.get_connection()
            ssh.upload(localfile, remotepath)
            return remotepath

    @staticmethod
    def remote_up_cluster_parser():
        """
        defines the way to parse the magic command ``%remote_up_cluster``
        """
        parser = MagicCommandParser(prog="remote_up_cluster",
                                    description='upload a file to the remote machine and then to the cluster')
        parser.add_argument(
            'localfile',
            type=str,
            help='local file to upload')
        parser.add_argument(
            'remotepath',
            type=str,
            help='remote path (HDFS) of the uploaded file')
        return parser

    @line_magic
    def remote_up_cluster(self, line):
        """
        upload a file to the remote machine and then to the remote cluster,

        Example::

            %remote_up_cluster localfile remotepath

        the command does not allow spaces in files

        .. nbref::
            :tag: Hadoop
            :title: remote_up_cluster

            The code for magic command ``%remote_up_cluster`` is equivalent to::

                ssh = ASSHClient(server, username, password)
                ssh.connect()
                ssh.upload_cluster(localfile, remotepath)
                ssh.close()



        .. versionadded:: 1.1
        """
        parser = self.get_parser(
            MagicRemoteSSH.remote_up_cluster_parser, "remote_up_cluster")
        args = self.get_args(line, parser)

        if args is not None:
            localfile, remotepath = args.localfile, args.remotepath
            if not os.path.exists(localfile):
                raise FileNotFoundError(localfile)
            ssh = self.get_connection()
            ssh.upload_cluster(localfile, remotepath)
            return remotepath

    @staticmethod
    def remote_down_parser():
        """
        defines the way to parse the magic command ``%remote_down``
        """
        parser = MagicCommandParser(prog="remote_down",
                                    description='download a file from the remote machine')
        parser.add_argument(
            'remotepath',
            type=str,
            help='remote path of the uploaded file')
        parser.add_argument(
            'localfile',
            type=str,
            help='local file to upload')
        parser.add_argument(
            '-o',
            '--overwrite',
            action='store_true',
            default=False,
            help='overwrite the local file')
        return parser

    @line_magic
    def remote_down(self, line):
        """
        download a file from the remote machine,

        Example::

            %remote_down remotepath localfile

        the command does not allow spaces in files

        .. nbref::
            :tag: Hadoop
            :title: remote_down

            The code for magic command ``%remote_down`` is equivalent to::

                ssh = ASSHClient(server, username, password)
                ssh.connect()
                ssh.download(remotepath, localfile)
                ssh.close()


        """
        parser = self.get_parser(
            MagicRemoteSSH.remote_down_parser, "remote_down")
        args = self.get_args(line, parser)

        if args is not None:
            localfile, remotepath = args.localfile, args.remotepath
            ssh = self.get_connection()
            if os.path.exists(localfile):
                if args.overwrite:
                    os.remove(localfile)
                else:
                    raise Exception(
                        "file {0} cannot be overwritten".format(localfile))
            ssh.download(remotepath, localfile)
            return localfile

    @staticmethod
    def remote_down_cluster_parser():
        """
        defines the way to parse the magic command ``%remote_down_cluster``
        """
        parser = MagicCommandParser(prog="remote_down_cluster",
                                    description='download a file from the cluster to the remote machine and then to your local machine')
        parser.add_argument(
            'remotepath',
            type=str,
            help='remote path (HDFS) of the uploaded file')
        parser.add_argument(
            'localfile',
            type=str,
            help='local file to upload')
        parser.add_argument(
            '-o',
            '--overwrite',
            action='store_true',
            default=False,
            help='overwrite the local file')
        parser.add_argument(
            '-m',
            '--merge',
            action='store_true',
            default=False,
            help='merges files in folder in a single file')
        return parser

    @line_magic
    def remote_down_cluster(self, line):
        """
        download a file from the cluster to the local machine through the bridge

        Example::

            %remote_down_cluster remotepath localfile

        the command does not allow spaces in files

        .. nbref::
            :tag: Hadoop
            :title: remote_down_cluster

            The code for magic command ``%remote_down_cluster`` is equivalent to::

                ssh = ASSHClient(server, username, password)
                ssh.connect()
                ssh.download_cluster(remotepath, localfile, merge=merge)
                ssh.close()



        .. versionadded:: 1.1
        """
        parser = self.get_parser(
            MagicRemoteSSH.remote_down_cluster_parser, "remote_down_cluster")
        args = self.get_args(line, parser)

        if args is not None:
            localfile, remotepath = args.localfile, args.remotepath
            if os.path.exists(localfile):
                if args.overwrite:
                    os.remove(localfile)
                else:
                    raise Exception(
                        "file {0} cannot be overwritten".format(localfile))
            ssh = self.get_connection()
            ssh.download_cluster(remotepath, localfile, merge=args.merge)
            return localfile

    @staticmethod
    def open_remote_shell_parser():
        """
        defines the way to parse the magic command ``%open_remote_shell``
        """
        parser = MagicCommandParser(prog="open_remote_shell",
                                    description='command will execute as if they were in a shell')
        parser.add_argument(
            '-f',
            '--format',
            type=str,
            default='html',
            help='formart of this output, html or plain')
        return parser

    @line_magic
    def open_remote_shell(self, line):
        """
        Defines ``%open_remote_shell``

        .. nbref::
            :tag: Hadoop
            :title: open_remote_shell

            The code for magic command ``%open_remote_shell`` is equivalent to::

                ssh = ASSHClient(server, username, password)
                ssh.connect()
                ssh.open_session(out_format=format)
                ssh.close()



        """
        parser = self.get_parser(
            MagicRemoteSSH.open_remote_shell_parser, "open_remote_shell")
        args = self.get_args(line, parser)

        if args is not None:
            ssh = self.get_connection()
            ssh.open_session(out_format=args.format)
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
        return HTML(self.shell_remote_text(line, cell))

    @line_cell_magic
    def shell_remote_text(self, line, cell=None):
        """
        Defines ``%shell_remote_text`` and ``%%shell_remote_text``
        """
        ssh = self.get_connection()
        if cell is None:
            out = ssh.send_recv_session(line)
        else:
            out = ssh.send_recv_session(cell)

        return out

    @staticmethod
    def remote_ls_parser():
        """
        defines the way to parse the magic command ``%remote_ls``
        """
        parser = MagicCommandParser(prog="remote_ls",
                                    description='returns the content of a folder as a dataframe')
        parser.add_argument(
            'path',
            type=str,
            help='path to look into')
        return parser

    @line_magic
    def remote_ls(self, line):
        """
        returns the content of a folder on the remote machine as a dataframe

        Example::

            %remote_ls .

        .. nbref::
            :tag: Hadoop
            :title: remote_ls

            The code for magic command ``%remote_ls`` is equivalent to::

                ssh = ASSHClient(server, username, password)
                ssh.connect()
                df = ssh.ls(path)
                ssh.close()



        .. versionadded:: 1.1
        """
        parser = self.get_parser(MagicRemoteSSH.remote_ls_parser, "remote_ls")
        args = self.get_args(line, parser)

        if args is not None:
            ssh = self.get_connection()
            df = ssh.ls(args.path)
            return df

    @staticmethod
    def dfs_ls_parser():
        """
        defines the way to parse the magic command ``%dfs_ls``
        """
        parser = MagicCommandParser(prog="dfs_ls",
                                    description='returns the content of a folder from the cluster as a dataframe')
        parser.add_argument(
            'path',
            type=str,
            help='path to look into')
        return parser

    @line_magic
    def dfs_ls(self, line):
        """
        returns the content of a folder on the cluster as a dataframe

        Example::

            %dfs_ls .

        .. nbref::
            :tag: Hadoop
            :title: dfs_ls

            The code for magic command ``%dfs_ls`` is equivalent to::

                ssh = ASSHClient(server, username, password)
                ssh.connect()
                df = ssh.dfs_ls(args.path)
                ssh.close()



        .. versionadded:: 1.1
        """
        parser = self.get_parser(MagicRemoteSSH.dfs_ls_parser, "dfs_ls")
        args = self.get_args(line, parser)

        if args is not None:
            ssh = self.get_connection()
            df = ssh.dfs_ls(args.path)
            return df

    @staticmethod
    def dfs_rm_parser():
        """
        defines the way to parse the magic command ``%dfs_rm``
        """
        parser = MagicCommandParser(prog="dfs_rm",
                                    description='remove a file on the cluster')
        parser.add_argument(
            'path',
            type=str,
            help='path to remove')
        parser.add_argument(
            '-r',
            '--recursive',
            action='store_true',
            default=False,
            help='to remove subfolders too')
        return parser

    @line_magic
    def dfs_rm(self, line):
        """
        remove a file on the cluster

        Example::

            %dfs_rm .

        .. nbref::
            :tag: Hadoop
            :title: dfs_rm

            The code for magic command ``%dfs_rm`` is equivalent to::

                ssh = ASSHClient(server, username, password)
                ssh.connect()
                df = ssh.dfs_rm(path, recursive=recursive)
                ssh.close()



        .. versionadded:: 1.1
        """
        parser = self.get_parser(MagicRemoteSSH.dfs_rm_parser, "dfs_rm")
        args = self.get_args(line, parser)

        if args is not None:
            ssh = self.get_connection()
            df = ssh.dfs_rm(args.path, recursive=args.recursive)
            return df

    @staticmethod
    def dfs_mkdir_parser():
        """
        defines the way to parse the magic command ``%dfs_mkdir``
        """
        parser = MagicCommandParser(prog="dfs_mkdir",
                                    description='create a folder')
        parser.add_argument(
            'path',
            type=str,
            help='path to remove')
        return parser

    @line_magic
    def dfs_mkdir(self, line):
        """
        create a folder on the cluster

        Example::

            %dfs_mkdir afolder

        .. nbref::
            :tag: Hadoop
            :title: dfs_mkdir

            The code for magic command ``%dfs_mkdir`` is equivalent to::

                ssh = ASSHClient(server, username, password)
                ssh.connect()
                df = ssh.dfs_mkdir(path)
                ssh.close()



        .. versionadded:: 1.1
        """
        parser = self.get_parser(MagicRemoteSSH.dfs_mkdir_parser, "dfs_mkdir")
        args = self.get_args(line, parser)

        if args is not None:
            ssh = self.get_connection()
            df = ssh.dfs_mkdir(args.path)
            return df


def register_magics_ssh(ip=None):
    """
    register magics function, can be called from a notebook

    @param      ip      from ``get_ipython()``
    """
    if ip is None:
        from IPython import get_ipython
        ip = get_ipython()
    ip.register_magics(MagicRemoteSSH)
