"""
@file
@brief A class to help connect with a remote machine and send command line.
"""

import time
import socket
import os
import io
import warnings

from pyquickhelper.loghelper import noLOG
from pyquickhelper.filehelper import is_file_string


class ASSHClient():

    """
    A simple class to access to remote machine through SSH.
    It requires modules
    `paramiko <http://www.paramiko.org/>`_,
    `pycrypto <https://pypi.python.org/pypi/pycrypto/>`_,
    `ecdsa <https://pypi.python.org/pypi/ecdsa>`_.

    This class is used in magic command @see me remote_open.
    On Windows, the installation of pycrypto can be tricky.
    See `Pycrypto on Windows <http://www.xavierdupre.fr/blog/2014-10-21_nojs.html>`_.
    Those modules are part of the `Anaconda <http://docs.continuum.io/anaconda/pkg-docs.html>`_ distribution.
    """

    def __init__(self, server, username, password):
        """
        constructor

        @param      server      server
        @param      username    username
        @param      password    password
        """
        self.server = server
        self.username = username
        self.password = password
        self.connection = None
        self.session = None

    def __str__(self):
        """
        usual
        """
        return "ASSHClient"

    def connect(self):
        """
        connect
        """
        import paramiko
        self.connection = paramiko.SSHClient()
        self.connection.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.connection.connect(
            self.server,
            username=self.username,
            password=self.password)

    def execute_command(self, command, no_exception=False, fill_stdin=None):
        """
        execute a command line, it raises an error
        if there is an error

        @param      command         command
        @param      no_exception    if True, do not raise any exception
        @param      fill_stdin      data to send on the stdin input
        @return                     stdout, stderr

        Example of commands::

            ssh.execute_command("ls")
            ssh.execute_command("hdfs dfs -ls")

        """
        stdin, stdout, stderr = self.connection.exec_command(command)

        if fill_stdin is not None:
            if isinstance(fill_stdin, list):
                fill_stdin = "\n".join(stdin)
            if isinstance(fill_stdin, str):
                stdin.write(fill_stdin)
                stdin.flush()
            else:
                raise TypeError(
                    "fill_stdin must be a string, not: {0}".format(
                        type(fill_stdin)))

        stdin.close()

        err = stderr.read()
        out = stdout.read()

        # weird...
        if isinstance(err, str) and err.startswith("b'"):
            err = eval(err)
        if isinstance(out, str) and out.startswith("b'"):
            out = eval(out)

        if isinstance(err, bytes):
            err = err.decode("utf-8")
        if isinstance(out, bytes):
            out = out.decode("utf-8")

        if not no_exception and len(err) > 0:
            raise Exception(
                "unable to run: {0}\nOUT:\n{1}\nERR:\n{2}".format(
                    command,
                    out,
                    err))

        return out, err

    def close(self):
        """
        close the connection
        """
        self.connection.close()
        self.connection = None

    def upload(self, localpath, remotepath):
        """
        upload a file to the remote machine (not on the cluster)

        @param      localpath     local file (or a list of files)
        @param      remotepath    remote file

        .. versionchanged:: 1.1
            it can upload multiple files if localpath is a list
        """
        sftp = self.connection.open_sftp()
        if isinstance(localpath, str):
            if not os.path.exists(localpath):
                raise FileNotFoundError(localpath)
            sftp.put(localpath, remotepath)
        else:
            for f in localpath:
                if not os.path.exists(f):
                    raise FileNotFoundError(f)
                sftp.put(f, remotepath + "/" + os.path.split(f)[-1])
        sftp.close()

    def upload_cluster(self, localpath, remotepath):
        """
        the function directly uploads the file to the cluster, it first goes
        to the bridge, uploads it to the cluster and deletes it from the bridge

        @param  localpath       local filename (or list of files)
        @param  remotepath      path to the cluster
        @return                 filename

        .. versionadded:: 1.1
        """
        if isinstance(localpath, str):
            filename = os.path.split(localpath)[-1]
            self.upload(localpath, filename)
            self.execute_command(
                "hdfs dfs -put {0} {1}".format(filename, remotepath))
            self.execute_command("rm {0}".format(filename))
        else:
            self.upload(localpath, ".")
            for afile in localpath:
                filename = os.path.split(afile)[-1]
                self.execute_command(
                    "hdfs dfs -put {0} {1}".format(filename, remotepath))
                self.execute_command("rm {0}".format(filename))

        return remotepath

    def download(self, remotepath, localpath):
        """
        download a file from the remote machine (not on the cluster)
        @param      localpath     local file
        @param      remotepath    remote file (it can be a list, localpath is a folder in that case)

        .. versionchanged:: 1.1
            remotepath can be a list of paths
        """
        sftp = self.connection.open_sftp()
        if isinstance(remotepath, str):
            sftp.get(remotepath, localpath)
        else:
            for path in remotepath:
                filename = os.path.split(path)[-1]
                sftp.get(path, localpath + "/" + filename)
        sftp.close()

    def download_cluster(self, remotepath, localpath, merge=False):
        """
        download a file directly from the cluster to the local machine
        @param      localpath       local file
        @param      remotepath      remote file (it can be a list, localpath is a folder in that case)
        @param      merge           True to use getmerge instead of get

        .. versionadded:: 1.1
        """
        cget = "getmerge" if merge else "get"
        if isinstance(remotepath, str):
            filename = os.path.split(localpath)[-1]
            self.execute_command(
                "hdfs dfs -{2} {0} {1}".format(remotepath, filename, cget))
            self.download(filename, localpath)
            self.execute_command("rm {0}".format(filename))
        else:
            tod = []
            for afile in remotepath:
                filename = os.path.split(afile)[-1]
                self.execute_command(
                    "hdfs dfs -{2} {0} {1}".format(afile, filename, cget))
                tod.append(filename)
            self.download(tod, localpath)
            for afile in tod:
                self.execute_command("rm {0}".format(afile))

        return remotepath

    _allowed_form = {None: None, "plain": None, "html": None}

    @staticmethod
    def _get_out_format(format):
        """
        returns a function which converts an ANSI string into a different format

        @param      format      string
        @return                 function
        """
        if format not in ASSHClient._allowed_form:
            raise KeyError(
                "unexpected format, it should be in " +
                ",".join(
                    ASSHClient._allowed_form.keys()))
        func = ASSHClient._allowed_form[format]
        if func is None:
            if format is None:
                def idfunc(s):
                    return s
                func = idfunc
            elif format == "plain":
                import ansiconv

                def convert_plain(s):
                    return ansiconv.to_plain(s)
                func = convert_plain
            elif format == "html":
                from ansi2html import Ansi2HTMLConverter
                conv = Ansi2HTMLConverter()

                def convert_html(s):
                    return conv.convert(s)
                func = convert_html
            ASSHClient._allowed_form[format] = func
        return func

    def open_session(self,
                     no_exception=False,
                     timeout=1.0,
                     add_eol=True,
                     prompts=("~$", ">>>"),
                     out_format=None):
        """
        open a session with method `invoke_shell <http://docs.paramiko.org/en/latest/api/client.html?highlight=invoke_shell#paramiko.client.SSHClient.invoke_shell>`_

        @param      no_exception    if True, do not raise any exception in case of error
        @param      timeout         timeout in s
        @param      add_eol         if True, the function will add a EOL to the sent command if it does not have one
        @param      prompts         if function terminates if the output ends by one of those strings.
        @param      out_format      None, plain, html

        .. exref::
            :title: How to open a remote shell?
            :tag: Hadoop

            ::

                ssh = ASSHClient(   "<server>",
                                    "<login>",
                                    "<password>")
                ssh.connect()
                out = ssh.send_recv_session("ls")
                print( ssh.send_recv_session("python") )
                print( ssh.send_recv_session("print('3')") )
                print( ssh.send_recv_session("import sys\\nsys.executable") )
                print( ssh.send_recv_session("sys.exit()") )
                print( ssh.send_recv_session(None) )
                ssh.close_session()
                ssh.close()

            The notebook :ref:`exampleofsshclientcommunicationrst` illustrates
            the output of these instructions.
        """
        if self.connection is None:
            raise Exception("No open connection.")
        if self.session is not None:
            raise Exception(
                "A session is already open. Cannot open a second one.")
        if out_format not in ASSHClient._allowed_form:
            raise KeyError(
                "unexpected format, it should be in {0}".format(
                    ";".join(
                        str(_) for _ in ASSHClient._allowed_form.keys())))

        self.session = self.connection.invoke_shell(width=300, height=1000)
        self.session_params = {
            "no_exception": no_exception,
            "timeout": timeout,
            "add_eol": add_eol,
            "prompts": [] if prompts is None else prompts,
            "out_format": out_format,
            "out_func": ASSHClient._get_out_format(out_format)
        }

        self.session.settimeout(timeout)

        return self.session

    def close_session(self):
        """
        close a session
        """
        if self.session is None:
            raise Exception("No open session. Cannot close anything.")

        self.session.close()
        self.session = None

    def send_recv_session(self, fillin):
        """
        Send something through a session,
        the function is supposed to return when the execute of the given command is done,
        but this is quite difficult to detect without knowing what exactly was send.

        So we add a timeout just to tell the function it has to return even if nothing
        tells the command has finished. It fillin is None, the function will just
        listen to the output.

        @param      fillin          sent to stdin
        @return                     stdout

        The output contains
        `escape codes <http://ascii-table.com/ansi-escape-sequences-vt-100.php>`_.
        They can be converted to plain text or HTML
        by using the module `ansiconv <http://pythonhosted.org/ansiconv/>`_
        and `ansi2html <https://github.com/ralphbean/ansi2html/>`_.
        This can be specified when opening the session.
        """
        prompts = self.session_params["prompts"]
        timeout = self.session_params["timeout"]
        add_eol = self.session_params["add_eol"]
        func = self.session_params["out_func"]

        if fillin is not None:
            self.session.send(fillin.encode("utf-8"))
            if add_eol and not fillin.endswith('\n'):
                self.session.send("\n".encode("utf-8"))

        buff = ''
        begin = time.perf_counter()
        while True:
            try:
                resp = self.session.recv(9999)
            except socket.timeout:
                resp = b""
            dec = resp.decode("unicode_escape")
            buff += dec
            for p in prompts:
                if buff.endswith(p):
                    break
            if time.perf_counter() - begin > timeout:
                break

        return func(buff.replace("\r", ""))

    @staticmethod
    def parse_lsout(out, local_schema=True):
        """
        parses the output of a command ls

        @param  out             output
        @param  local_schema    schema for the bridge or the cluster (False)
        @return                 DataFrame

        .. versionadded:: 1.1
        """
        import pandas
        if local_schema:
            names = ["attributes", "code", "alias", "folder",
                     "size", "unit", "name"]
        else:
            names = ["attributes", "code", "alias", "folder",
                     "size", "date", "time", "name"]
        kout = out
        out = out.replace("\r", "").split("\n")
        out = [_ for _ in out if len(_.split()) > 3]
        if len(out) == 0:
            df = pandas.DataFrame(columns=names)
            return df

        try:
            out_ = [_.split() for _ in out]
            if len(out_) > 0 and len(out_[0]) != len(names):
                if names[5] == "date" and len(out_[0]) == len(names) + 1:
                    # we merge 2 columns
                    out_ = [_[:5] + [" ".join(_[5:7])] + _[7:] for _ in out_]
            df = pandas.DataFrame(data=out_, columns=names)
        except AssertionError as e:
            out = "\n".join(out)
            buf = io.StringIO(out)
            try:
                df = pandas.read_fwf(buf, names=names, index=False)
            except ValueError as e:
                raise ValueError(
                    "unable to parse output:\nSCHEMA:\n{1}\nOUT:\n{0}".format(kout, ",".join(names))) from e

        df["isdir"] = df.apply(lambda r: r["attributes"][0] == "d", axis=1)
        return df

    def ls(self, path):
        """
        return the content of a folder on the bridge as a DataFrame

        @param  path        path on the bridge
        @return             DataFrame

        .. versionadded:: 1.1
        """
        out, err = self.execute_command("ls -l " + path)
        if len(err) > 0:
            raise Exception("unable to execute ls " + path + "\nERR:\n" + err)
        return ASSHClient.parse_lsout(out)

    def dfs_ls(self, path):
        """
        return the content of a folder on the cluster as a DataFrame

        @param  path        path on the cluster
        @return             DataFrame

        .. versionadded:: 1.1
        """
        out, err = self.execute_command("hdfs dfs -ls " + path)
        if len(err) > 0:
            raise Exception(
                "unable to execute hdfs dfs -ls " +
                path +
                "\nERR:\n" +
                err)
        return ASSHClient.parse_lsout(out, False)

    def exists(self, path):
        """
        tells if a file exists on the bridge

        @param      path        path
        @return                 boolean

        .. versionadded:: 1.1
        """
        try:
            df = self.ls(path)
        except Exception as e:
            if "No such file or directory" in str(e):
                return False
        ex = df[df.name == path]
        return len(ex) > 0

    def dfs_exists(self, path):
        """
        tells if a file exists on the cluster

        @param      path        path
        @return                 boolean

        .. versionadded:: 1.1
        """
        try:
            df = self.dfs_ls(path)
        except Exception as e:
            if "No such file or directory" in str(e):
                return False
            else:
                raise e
        if len(df) == 0:
            # it is a folder
            return True
        ex = df[df.name == path]
        if len(ex) > 0:
            return True
        ex = df[df.apply(lambda r: r["name"].startswith(path + "/"), axis=1)]
        if len(ex) > 0:
            return True
        return False

    def dfs_mkdir(self, path):
        """
        creates a directory on the cluster

        @param      path        path

        .. versionadded:: 1.1
        """
        return self.execute_command("hdfs dfs -mkdir " + path)

    def dfs_rm(self, path, recursive=False):
        """
        removes a file on the cluster

        @param      path        path
        @param      recursive   boolean

        .. versionadded:: 1.1
        """
        cmd = "hdfs dfs -rm "
        if recursive:
            cmd += "-r "
        out, err = self.execute_command(cmd + path, no_exception=True)
        if out.startswith("Moved"):
            return out, err
        else:
            raise Exception(
                "unable to remove " +
                path +
                "\nOUT\n" +
                out +
                "\nERR:\n" +
                err)

    @staticmethod
    def build_command_line_parameters(params, command_name="-param"):
        """
        builds a string for ``pig`` based on the parameters in params

        @param      params          dictionary
        @param      command_name    ``-param`` or ``-hiveconf``
        @return                     string

        .. versionadded:: 1.1
        """
        if params is None:
            return ""
        res = []
        for k, v in sorted(params.items()):
            if '"' in v:
                v = v.replace('"', '\\"')
            one = '{2} {0}="{1}"'.format(k, v, command_name)
            res.append(one)
        return " ".join(res)

    def pig_submit(self, pig_file,
                   dependencies=None,
                   params=None,
                   redirection="redirection.pig",
                   local=False,
                   stop_on_failure=False,
                   check=False,
                   no_exception=True,
                   fLOG=noLOG):
        """
        submits a PIG script, it first upload the script
        to the default folder and submit it

        @param      pig_file        pig script (local)
        @param      dependencies    others files to upload (still in the default folder)
        @param      params          parameters to send to the job
        @param      redirection     string empty or not
        @param      local           local run or not (option `-x local <https://cwiki.apache.org/confluence/display/PIG/PigTutorial>`_)  (in that case, redirection will be empty)
        @param      stop_on_failure if True, add option ``-stop_on_failure`` on the command line
        @param      check           if True, add option ``-check`` (in that case, redirection will be empty)
        @param      no_exception    sent to @see me execute_command
        @param      fLOG            logging function
        @return                     out, err from @see me execute_command

        If *redirection* is not empty, the job is submitted but
        the function returns after the standard output and error were
        redirected to ``redirection.out`` and ``redirection.err``.

        The first file will contain the results of commands
        `DESCRIBE <http://pig.apache.org/docs/r0.14.0/test.html#describe>`_
        `DUMP <http://pig.apache.org/docs/r0.14.0/test.html#dump>`_,
        `EXPLAIN <http://pig.apache.org/docs/r0.14.0/test.html#explain>`_.
        The standard error receives logs and exceptions.

        The function executes the command line::

            pig -execute -f <filename>

        With redirection::

            pig -execute -f <filename> 2> redirection.pig.err 1> redirection.pig.out &

        .. versionadded:: 1.1
        """
        dest = os.path.split(pig_file)[-1]
        self.upload(pig_file, dest)
        if dependencies is not None:
            for py in dependencies:
                self.upload(py, os.path.split(py)[-1])

        slocal = " -x local" if local else ""
        sstop_on_failure = " -stop_on_failure" if stop_on_failure else ""
        scheck = " -check" if check else ""

        if local or check:
            redirection = None

        if params is not None:
            sparams = ASSHClient.build_command_line_parameters(params)
            if len(sparams) > 0:
                sparams = " " + sparams
        else:
            sparams = ""

        if redirection is None:
            cmd = "pig{0}{1}{2} -execute -f {3}{4}".format(
                slocal,
                sstop_on_failure,
                scheck,
                dest,
                sparams)
        else:
            cmd = "pig{2}{3}{4} -execute -f {0}{5} 2> {1}.err 1> {1}.out &".format(
                dest,
                redirection,
                slocal,
                sstop_on_failure,
                scheck,
                sparams)

        if isinstance(cmd, list):
            raise TypeError("this should not happen:" + str(cmd))

        fLOG("[pig_submit]:", cmd)
        out, err = self.execute_command(cmd, no_exception=no_exception)
        return out, err

    def hive_submit(self, hive_file_or_query,
                    params=None,
                    redirection="redirection.hive",
                    no_exception=True,
                    fLOG=noLOG):
        """
        submits a PIG script, it first upload the script
        to the default folder and submit it

        @param      hive_file_or_query  pig script (local)
        @param      params              parameters to send to the job
        @param      redirection         string empty or not
        @param      no_exception        sent to @see me execute_command
        @param      fLOG                logging function
        @return                         out, err from @see me execute_command

        If *redirection* is not empty, the job is submitted but
        the function returns after the standard output and error were
        redirected to ``redirection.hive.out`` and ``redirection.hive.err``.

        The function executes the command line::

            hive -f <filename>

        Or::

            hive -e <query>

        With redirection::

            hive -execute -f <filename> 2> redirection.hive.err 1> redirection.hive.out &

        If there is no redirection, the function
        waits and return the output.

        .. exref::
            :title: Submit a HIVE query
            :tag: Hadoop

            ::

                client = ASSHClient()

                hive_sql = '''
                    DROP TABLE IF EXISTS bikes20;
                    CREATE TABLE bikes20 (sjson STRING);
                    LOAD DATA INPATH "/user/__USERNAME__/unittest2/paris*.txt" INTO TABLE bikes20;
                    SELECT * FROM bikes20 LIMIT 10;
                    '''.replace("__USERNAME__", self.client.username)

                out,err = client.hive_submit(hive_sql, redirection=None)

        .. versionadded:: 1.1
        """
        if is_file_string(hive_file_or_query) and os.path.exists(hive_file_or_query):
            dest = os.path.split(hive_file_or_query)[-1]
            self.upload(hive_file_or_query, dest)
            command = "-f"
        else:
            command = "-e"
            dest = hive_file_or_query.replace(
                "\n", " ").replace("\r", "").replace("\t", " ")
            dest = dest.replace("'", "\\'")
            dest = "'{}'".format(dest.strip())

        if params is not None:
            sparams = ASSHClient.build_command_line_parameters(
                params, "-hiveconf")
            if len(sparams) > 0:
                sparams = " " + sparams
        else:
            sparams = ""

        if redirection is None:
            cmd = "hive {0} {1}{2}".format(
                command,
                dest,
                sparams)
        else:
            cmd = "hive {0} {1}{2} 2> {3}.err 1> {3}.out &".format(
                command,
                dest,
                sparams,
                redirection)

        if isinstance(cmd, list):
            raise TypeError("this should not happen:" + str(cmd))

        warnings.warn("Hive submission is not tested. It will probably fail.")

        fLOG("[hive_submit]:", cmd)
        out, err = self.execute_command(cmd, no_exception=no_exception)
        return out, err
