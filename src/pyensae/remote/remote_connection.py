"""
@file
@brief A class to help connect with a remote machine and send command line.
"""

class ASSHClient():
    """
    A simple class to access to remote machine through SSH.
    It requires modules 
    `paramiko <http://www.paramiko.org/>`_,
    `pycrypto <https://pypi.python.org/pypi/pycrypto/>`_,
    `ecdsa <https://pypi.python.org/pypi/ecdsa>`_.
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

    def connect(self):
        """
        connect
        """
        import paramiko
        self.connection = paramiko.SSHClient()
        self.connection.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.connection.connect(self.server, username=self.username, password=self.password)

    def execute_command(self, command):
        """
        execute a command line, it raises an error
        if there is an error
        
        @param      command     command
        @return                 stdout, stderr
        
        Example of commands::
        
            execute_command("ls")
            execute_command("hdfs dfs -ls")
            
        """
        stdin,stdout,stderr = self.connection.exec_command(command)
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
            
        if len(err) > 0 :
            raise Exception("unable to run: {0}\nOUT:\n{1}\nERR:\n{2}".format(command, out, err))
            
        return out,err

    def close(self):
        """
        close the connection
        """
        self.connection.close()
        
    def upload(self, localpath, remotepath):
        """
        upload a file to the remote machine (not on the cluster)
        
        @param      localpath     local file
        @param      remotepath    remote file
        """
        sftp = self.connection.open_sftp()
        sftp.put(localpath, remotepath)
        sftp.close()        

    def download(self, remotepath, localpath):
        """
        download a file from the remote machine (not on the cluster)
        @param      localpath     local file
        @param      remotepath    remote file
        """
        sftp = self.connection.open_sftp()
        sftp.get(remotepath, localpath)
        sftp.close()        
        
