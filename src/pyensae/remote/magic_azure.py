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
from .azure_connection import AzureClient

@magics_class
class MagicAzure(Magics):
    """
    Defines magic commands to access `blob storage <http://azure.microsoft.com/fr-fr/documentation/articles/storage-dotnet-how-to-use-blobs/>`_
    and `HDInsight <http://azure.microsoft.com/fr-fr/services/hdinsight/>`_.
    """
    
    def _replace_params(self, cell):
        """
        replaces parameter such ``__PASSWORD__`` by variable in the notebook environnement
        
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
    def blob_open (self, line):
        """
        open a connection to blob service
        """
        spl = line.strip().split()
        if len(spl) != 3 and len(spl) != 0:
            print("Usage:")
            print("   blob_open <blobstorage> <blobalias> <blobpassword>")
            print("   blob_open")
            print("")
            print("No parameter means blobstorage, blobalias, blobpassword will be found in the workspace")
        else:
            if len(spl)==3:
                server,username,password = spl
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
            
    def create_client(self, account_name, account_key):
        """
        Create a @see cl AzureClient and stores in the workspace.
        
        @param      account_name        login
        @param      account_key         password
        """
        cl = AzureClient(account_name, account_key)
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
        
    @line_magic
    def blob_ls(self, line):
        """
        defines command %blob_ls
        """
        if line is None or len(line.strip()) == 0:
            print("Usage:")
            print("    blob_ls  container/path")
        else :
            line = line.strip()
            if line.startswith("/"):
                raise FileNotFoundError("path cannot start with '/': " + path)
                
            spl = line.split("/")
            container = spl[0]
            remotepath = None if len(spl)==1 else "/".join(spl[1:])
            cl, bs = self.get_blob_connection()
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
            print("")
            print("no space allowed in file names")
        else :
            localfile,remotepath = spl
            if not os.path.exists(localfile) :
                raise FileNotFoundError(localfile)
                
            if remotepath.startswith("/"):
                raise FileNotFoundError("remotepath cannot start with '/': " + remotepath)
                
            spl = remotepath.split("/")
            if len(spl) <= 1 :
                raise FileNotFoundError("the path is too short: " + remotepath)
            container = spl[0]
            remotepath = "/".join(spl[1:])
            cl, bs = self.get_blob_connection()
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
            print("   blob_down <remotepath> <localfile>")
            print("")
            print("no space allowed in file names")
        else :
            remotepath,localfile = spl
            if os.path.exists(localfile) :
                raise Exception("file {0} cannot be overwritten".format(localfile))

            if remotepath.startswith("/"):
                raise FileNotFoundError("remotepath cannot start with '/': " + remotepath)
                
            spl = remotepath.split("/")
            if len(spl) == 1 :
                raise FileNotFoundError("the path is too short: " + remotepath)
            container = spl[0]
            remotepath = "/".join(spl[1:])

            cl, bs = self.get_blob_connection()
            cl.download(bs, container, remotepath, localfile)
            return localfile
            
    @line_magic
    def blob_delete(self, line):
        """
        deletes a blob
        """
        if line is None or len(line.strip()) == 0:
            print("Usage:")
            print("   blob_delete <remotepath>")
            print("")
            print("no space allowed in file names")
        else :
            remotepath = line.strip()

            if remotepath.startswith("/"):
                raise FileNotFoundError("remotepath cannot start with '/': " + remotepath)
                
            spl = remotepath.split("/")
            if len(spl) == 1 :
                raise FileNotFoundError("the path is too short: " + remotepath)
            container = spl[0]
            remotepath = "/".join(spl[1:])

            cl, bs = self.get_blob_connection()
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
            print("   blob_copy <source> <dest>")
            print("")
            print("no space allowed in file names")
        else :
            src,dest = spl

            if src.startswith("/"):
                raise FileNotFoundError("remotepath cannot start with '/': " + src)
            if dest.startswith("/"):
                raise FileNotFoundError("remotepath cannot start with '/': " + dest)
                
            spl = src.split("/")
            if len(spl) == 1 :
                raise FileNotFoundError("the path is too short: " + src)
            container = spl[0]
            src = "/".join(spl[1:])
            
            spl = dest.split("/")
            if len(spl) == 1 :
                raise FileNotFoundError("the path is too short: " + dest)
            if container != spl[0]:
                raise Exception("the two containers should be the same: {0} != {1}".format(container, spl[0]))
            dest = "/".join(spl[1:])
            
            cl, bs = self.get_blob_connection()
            cl.copy_blob(bs, container, dest, src)
            return True

    @line_magic
    def azurepigsubmit(self, line):
        """
        defines command ``%azurepigsubmit``
        """
        if line in [None, ""]:
            print("Usage:")
            print("  %azurepigsubmit <jobname.pig>")
            print("")
            print("The file <jobname.pig> is local.")
        else:
            filename = line.strip()
            spl = filename.split()
            filename = spl[0]
            raise NotImplementedError()
            
    @line_magic
    def azurejobsyntax(self, line):
        """
        defines command ``%azurejobsyntax``
        """
        if line in [None, ""]:
            print("Usage:")
            print("  %azurejobsyntax <jobname.pig>")
            print("")
        else:
            filename = line.strip()
            if not os.path.exists(filename):
                raise FileNotFoundError(filename)
                
            dest = os.path.split(filename)[-1]
            raise NotImplementedError()
    

def register_azure_magics():
    """
    register magics function, can be called from a notebook
    """
    ip = get_ipython()
    ip.register_magics(MagicAzure)
    