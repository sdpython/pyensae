"""
@file
@brief A class to help connect with a remote machine and send command line.
"""

import time, socket, os

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
        import paramiko
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
        self.connection.connect(self.server, username=self.username, password=self.password)

    def execute_command(self, command, no_exception = False, fill_stdin = None):
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
        stdin,stdout,stderr = self.connection.exec_command(command)

        if fill_stdin is not None:
            if isinstance(fill_stdin, list):
                fill_stdin = "\n".join(stdin)
            if isinstance(fill_stdin, str):
                stdin.write(fill_stdin)
                stdin.flush()
            else:
                raise TypeError("fill_stdin must be a string, not: {0}".format(type(fill_stdin)))

        stdin.close()

        err = stderr.read()
        out = stdout.read()

        # weird...
        if isinstance(err, str) and err.startswith("b'") : err = eval(err)
        if isinstance(out, str) and out.startswith("b'") : out = eval(out)

        if isinstance(err, bytes):
            err = err.decode("utf-8")
        if isinstance(out, bytes):
            out = out.decode("utf-8")

        if not no_exception and len(err) > 0 :
            raise Exception("unable to run: {0}\nOUT:\n{1}\nERR:\n{2}".format(command, out, err))

        return out,err

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
        if not os.path.exists(localpath):
            raise FileNotFoundError(localpath)
        if isinstance(localpath, str):
            sftp.put(localpath, remotepath)
        else:
            for f in localpath:
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
            self.execute_command("hdfs dfs -put {0} {1}".format(filename, remotepath))
            self.execute_command("rm {0}".format(filename))
        else:
            self.upload(localpath, ".")
            for afile in localpath:
                filename = os.path.split(afile)[-1]
                self.execute_command("hdfs dfs -put {0} {1}".format(filename, remotepath))
                self.execute_command("rm {0}".format(filename))
                
        return remotepath

    def download(self, remotepath, localpath):
        """
        download a file from the remote machine (not on the cluster)
        @param      localpath     local file
        @param      remotepath    remote file (it can be a list, localpath is a folder in that case)
        
        ..versionchanged:: 1.1
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

    def download_cluster(self, remotepath, localpath):
        """
        download a file directly from the cluster to the local machine
        @param      localpath     local file
        @param      remotepath    remote file (it can be a list, localpath is a folder in that case)
        
        ..versionadded:: 1.1
        """
        if isinstance(remotepath, str):
            filename = os.path.split(localpath)[-1]
            self.execute_command("hdfs dfs -get {0} {1}".format(remotepath, filename))
            self.download(filename, localpath)
            self.execute_command("rm {0}".format(filename))
        else:
            for afile in remotepath:
                filename = os.path.split(afile)[-1]
                self.execute_command("hdfs dfs -get {0} {1}".format(remotepath, filename))
            self.download(filename, localpath)
            for afile in remotepath:
                filename = os.path.split(afile)[-1]
                self.execute_command("rm {0}".format(filename))
                
        return remotepath
        
    _allowed_form = { None:None, "plain":None, "html":None }

    @staticmethod
    def _get_out_format(format):
        """
        returns a function which converts an ANSI string into a different format

        @param      format      string
        @return                 function
        """
        if format not in ASSHClient._allowed_form:
            raise KeyError("unexpected format, it should be in " + ",".join(ASSHClient._allowed_form.keys()))
        func = ASSHClient._allowed_form[format]
        if func is None:
            if format is None: func = lambda s : s
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
                        no_exception = False,
                        timeout = 1.0,
                        add_eol = True,
                        prompts = ("~$", ">>>"),
                        out_format = None):
        """
        open a session with method `invoke_shell <http://docs.paramiko.org/en/latest/api/client.html?highlight=invoke_shell#paramiko.client.SSHClient.invoke_shell>`_

        @param      no_exception    if True, do not raise any exception in case of error
        @param      timeout         timeout in s
        @param      add_eol         if True, the function will add a EOL to the sent command if it does not have one
        @param      prompts         if function terminates if the output ends by one of those strings.
        @param      out_format      None, plain, html

        @example(How to open a remote shell?)
        @code
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
        @endcode

        The notebook :ref:`exampleofsshclientcommunicationrst` illustrates
        the output of these instructions.

        @endexample
        """
        if self.connection is None:
            raise Exception("No open connection.")
        if self.session is not None:
            raise Exception("A session is already open. Cannot open a second one.")
        if out_format not in ASSHClient._allowed_form:
            raise KeyError("unexpected format, it should be in {0}".format(";".join(str(_) for _ in ASSHClient._allowed_form.keys())))

        self.session = self.connection.invoke_shell(width=300, height=1000)
        self.session_params = {
                    "no_exception":no_exception,
                    "timeout":timeout,
                    "add_eol":add_eol,
                    "prompts":[] if prompts is None else prompts,
                    "out_format":out_format,
                    "out_func":ASSHClient._get_out_format(out_format)
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
        func    = self.session_params["out_func"]

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

        return func ( buff.replace("\r","") )