#-*- coding: utf-8 -*-
"""
@file
@brief Magic command to run PIG script with Azure.
"""
import sys
import os

from pyquickhelper.loghelper import run_cmd
from pyquickhelper.ipythonhelper import MagicClassWithHelpers, MagicCommandParser

from IPython.core.magic import magics_class, line_magic, cell_magic
from IPython.core.display import HTML
from .azure_connection import AzureClient, AzureException
from ..file_helper.jython_helper import run_jython, download_java_standalone


@magics_class
class MagicAzure(MagicClassWithHelpers):

    """
    Defines magic commands to access `blob storage <http://azure.microsoft.com/fr-fr/documentation/articles/storage-dotnet-how-to-use-blobs/>`_
    and `HDInsight <http://azure.microsoft.com/fr-fr/services/hdinsight/>`_.

    When the container is not specified, it will take the default one.

    .. faqref::
        :title: Magic command %blob_open does not work

        Try this::

            %load_ext pyensae

        The exception tells more about what goes wrong.
        Usually a module is missing.

    .. faqref::
        :title: Incorrect padding

        The following crypted message happens sometimes::

            Error: Incorrect padding

        It is usually due to an incorrect password.
        Some notebooks uses::

            import pyquickhelper.ipythonhelper as ipy
            params={"blob_storage":"hdblobstorage", "password":""}
            ipy.open_html_form(params=params,title="credentials",key_save="blobservice")

            blobstorage = blobservice["blob_storage"]
            blobpassword = blobservice["password"]

            import pyensae
            %blob_open

        This code avoids the author letting password in a notebook
        but you can just replace everything by::

            blobstorage = "<username>"
            blobpassword = "****long*key*******=="

            import pyensae
            %blob_open
    """

    def create_client(self, account_name, account_key,
                      hadoop_server=None, hadoop_password=None, username=None):
        """
        Create a @see cl AzureClient and stores in the workspace.

        @param      account_name        login
        @param      account_key         password
        @param      hadoop_server       hadoop server
        @param      hadoop_password     hadoop password
        @param      username            username
        @return                         instance of @see cl AzureClient
        """
        if username is None:
            username = "any"
        cl = AzureClient(
            account_name,
            account_key,
            hadoop_server,
            hadoop_password,
            pseudo=username)
        self.shell.user_ns["remote_azure_client"] = cl
        return cl

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
    def azureclient(self, line):
        """
        returns the AzureClient object
        """
        cl, bs = self.get_blob_connection()
        return cl

    @line_magic
    def blobservice(self, line):
        """
        returns the BlobService object
        """
        cl, bs = self.get_blob_connection()
        return bs

    @line_magic
    def blobcontainer(self, line):
        """
        returns the Blob Storage container
        """
        cl, bs = self.get_blob_connection()
        return cl.account_name

    @staticmethod
    def blob_open_parser():
        """
        defines the way to parse the magic command ``%blob_open``
        """
        parser = MagicCommandParser(prog="blob_open",
                                    description='open a connection to an Azure blob storage, by default, ' +
                                    'the magic command takes blobstorage and blobpassword local variables as default values')
        parser.add_argument(
            '-b',
            '--blobstorage',
            type=str,
            default='blobstorage',
            help='blob storage name')
        parser.add_argument(
            '-p',
            '--blobpassword',
            type=str,
            default='blobpassword',
            help='blob password')
        return parser

    @line_magic
    def blob_open(self, line):
        """
        .. nbref::
            :tag: Azure
            :title: blob_open

            Open a connection to blob service.
            It returns objects @see cl AzureClient and
            `BlobService <http://www.xavierdupre.fr/app/azure-sdk-for-python/helpsphinx/storage/blobservice.html?highlight=blobservice#azure.storage.blobservice.BlobService>`_.

            The code for magic command ``%blob_open`` is equivalent to::

                from pyensae.remote import AzureClient
                cl = AzureClient(account_name, account_key, hadoop_server, hadoop_password, pseudo=username)
                bs = cl.open_blob_service()

        .. versionchanged:: 1.1
        """
        parser = self.get_parser(MagicAzure.blob_open_parser, "blob_open")
        args = self.get_args(line, parser)

        if args is not None:
            server = args.blobstorage
            password = args.blobpassword
            if self.shell is None:
                raise Exception("No detected workspace.")

            if "remote_azure_blob" in self.shell.user_ns:
                raise Exception(
                    "a connection is still open, close it first (stored in remote_azure_blob local variable)")

            cl = self.create_client(server, password)
            bs = cl.open_blob_service()
            self.shell.user_ns["remote_azure_blob"] = bs
            return cl, bs

    @staticmethod
    def hd_open_parser():
        """
        defines the way to parse the magic command ``%hd_open``
        """
        parser = MagicCommandParser(prog="hd_open",
                                    description='open a connection to an Azure blob storage and a HD Insight cluster, ' +
                                    'by default, the magic command takes blobstorage, blobpassword, hadoop_server, ' +
                                    'hadoop_password local variables as default values')
        parser.add_argument(
            '-b',
            '--blobstorage',
            type=str,
            default='blobstorage',
            help='blob storage name')
        parser.add_argument(
            '-p',
            '--blobpassword',
            type=str,
            default='blobpassword',
            help='blob password')
        parser.add_argument(
            '-s',
            '--hadoop_server',
            type=str,
            default='hadoop_server',
            help='hadoop server name')
        parser.add_argument(
            '-P',
            '--hadoop_password',
            type=str,
            default='hadoop_password',
            help='hadoop password')
        parser.add_argument(
            '-u',
            '--username',
            type=str,
            default='username',
            help='username (used as a prefix to avoid conflict when multiple users are using the same connection')
        return parser

    @line_magic
    def hd_open(self, line):
        """
        open a connection to blob service

        .. nbref::
            :tag: Azure
            :title: hd_open

            Open a connection to blob service.
            It returns objects @see cl AzureClient and
            `BlobService <http://www.xavierdupre.fr/app/azure-sdk-for-python/helpsphinx/storage/blobservice.html?highlight=blobservice#azure.storage.blobservice.BlobService>`_.

            The code for magic command ``%hd_open`` is equivalent to::

                from pyensae.remote import AzureClient
                cl = AzureClient(account_name, account_key, hadoop_server, hadoop_password, pseudo=username)
                bs = cl.open_blob_service()


        """
        parser = self.get_parser(MagicAzure.hd_open_parser, "hd_open")
        args = self.get_args(line, parser)

        if args is not None:
            server = args.blobstorage
            password = args.blobpassword
            hadoop_server = args.hadoop_server
            hadoop_password = args.hadoop_password
            username = args.username

            if self.shell is None:
                raise Exception("No detected workspace.")

            if "remote_azure_blob" in self.shell.user_ns:
                raise Exception(
                    "a connection is still open, close it first (stored in remote_azure_blob local variable)")

            cl = self.create_client(
                server,
                password,
                hadoop_server,
                hadoop_password,
                username=username)
            bs = cl.open_blob_service()
            self.shell.user_ns["remote_azure_blob"] = bs
            return cl, bs

    @line_magic
    def blob_close(self, line):
        """
        close the connection and remove the connection
        from the notebook workspace

        .. nbref::
            :tag: Azure
            :title: blob_close

            Does nothing.


        """
        cl, bs = self.get_blob_connection()
        # bs.close()
        del self.shell.user_ns["remote_azure_blob"]
        return True

    @line_magic
    def blob_containers(self, line):
        """
        returns the list of containers
        """
        if "-h" in line or "--help" in line:
            print("Usage: %blob_containers")
        else:
            cl, bs = self.get_blob_connection()
            res = bs.list_containers()
            return [r.name for r in res]

    def _interpret_path(self, line, cl, bs, empty_is_value=False):
        """
        interpret a path

        @param      line                line (see :ref:`l-magic-path-container`)
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
            remotepath = None if len(spl) == 1 else "/".join(spl[1:])

        if not empty_is_value and (remotepath is None or len(remotepath) == 0):
            raise FileNotFoundError("path should not be empty: " + line)

        return container, remotepath

    @staticmethod
    def blob_ls_parser():
        """
        defines the way to parse the magic command ``%blob_ls``
        """
        parser = MagicCommandParser(prog="blob_ls",
                                    description='describes the content of folder in a blob storage')
        parser.add_argument(
            'path',
            type=str,
            help='path to look into, </path> or <container>/<path>')
        return parser

    @line_magic
    def blob_ls(self, line):
        """
        defines command %blob_ls, see :ref:`l-magic-path-container`

        .. nbref::
            :tag: Azure
            :title: blob_ls

            The code for magic command ``%blob_ls`` is equivalent to::

                from pyensae.remote import AzureClient
                cl = AzureClient(account_name, account_key, hadoop_server, hadoop_password, pseudo=username)
                bs = cl.open_blob_service()
                df = cl.ls(bs, container, remotepath)


        """
        parser = self.get_parser(MagicAzure.blob_ls_parser, "blob_ls")
        args = self.get_args(line, parser)

        if args is not None:
            cl, bs = self.get_blob_connection()
            container, remotepath = self._interpret_path(
                args.path, cl, bs, True)
            df = cl.ls(bs, container, remotepath)
            if len(df) > 0:
                return df[["name", "last_modified",
                           "content_type", "content_length", "blob_type"]]
            else:
                return df

    @staticmethod
    def blob_lsl_parser():
        """
        defines the way to parse the magic command ``%blob_lsl``
        """
        parser = MagicCommandParser(prog="blob_lsl",
                                    description='describes the content of folder in a blob storage + metadata')
        parser.add_argument(
            'path',
            type=str,
            help='path to look into, </path> or <container>/<path>')
        return parser

    @line_magic
    def blob_lsl(self, line):
        """
        defines command %blob_lsl (extended version of blob_lsl),
        see :ref:`l-magic-path-container`

        .. nbref::
            :tag: Azure
            :title: blob_lsl

            The code for magic command ``%blob_lsl`` is equivalent to::

                from pyensae.remote import AzureClient
                cl = AzureClient(account_name, account_key, hadoop_server, hadoop_password, pseudo=username)
                bs = cl.open_blob_service()
                df = cl.ls(bs, container, remotepath, add_metadata=True)


        """
        parser = self.get_parser(MagicAzure.blob_lsl_parser, "blob_lsl")
        args = self.get_args(line, parser)

        if args is not None:
            cl, bs = self.get_blob_connection()
            container, remotepath = self._interpret_path(
                args.path, cl, bs, True)
            return cl.ls(bs, container, remotepath, add_metadata=True)

    @staticmethod
    def blob_up_parser():
        """
        defines the way to parse the magic command ``%blob_up``
        """
        parser = MagicCommandParser(prog="blob_up",
                                    description='upload a file on a blob storage, we assume the container is the first element to the remote path')
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
    def blob_up(self, line):
        """
        upload a file to the blob storage,
        we assume the container is the first element of the path,
        see :ref:`l-magic-path-container`

        Example::

            %blob_up localfile remotepath

        the command does not allow spaces in files

        .. nbref::
            :tag: Azure
            :title: blob_up

            The code for magic command ``%blob_up`` is equivalent to::

                from pyensae.remote import AzureClient
                cl = AzureClient(account_name, account_key, hadoop_server, hadoop_password, pseudo=username)
                bs = cl.open_blob_service()
                cl.upload(bs, container, remotepath, localfile)


        """
        parser = self.get_parser(MagicAzure.blob_up_parser, "blob_up")
        args = self.get_args(line, parser)

        if args is not None:
            localfile, remotepath = args.localfile, args.remotepath
            if not os.path.exists(localfile):
                raise FileNotFoundError(localfile)

            cl, bs = self.get_blob_connection()
            container, remotepath = self._interpret_path(remotepath, cl, bs)
            cl.upload(bs, container, remotepath, localfile)
            return remotepath

    @staticmethod
    def blob_down_parser():
        """
        defines the way to parse the magic command ``%blob_down``
        """
        parser = MagicCommandParser(prog="blob_down",
                                    description='download a file from a blob storage, we assume the container is the first element to the remote path')
        parser.add_argument(
            'remotepath',
            type=str,
            help='remote path of the file to download')
        parser.add_argument(
            'localfile',
            type=str,
            help='local name for the downloaded file')
        parser.add_argument(
            '-o',
            '--overwrite',
            action='store_true',
            default=False,
            help='overwrite the local file')
        return parser

    @line_magic
    def blob_down(self, line):
        """
        download a file from the blob storage,
        see :ref:`l-magic-path-container`

        Example::

            %blob_down remotepath localfile

        the command does not allow spaces in file names

        .. nbref::
            :tag: Azure
            :title: blob_down

            The code for magic command ``%blob_down`` is equivalent to::

                from pyensae.remote import AzureClient
                cl = AzureClient(account_name, account_key, hadoop_server, hadoop_password, pseudo=username)
                bs = cl.open_blob_service()
                cl.download(bs, container, remotepath, localfile)


        """
        parser = self.get_parser(MagicAzure.blob_down_parser, "blob_down")
        args = self.get_args(line, parser)

        if args is not None:
            localfile, remotepath = args.localfile, args.remotepath
            if os.path.exists(localfile):
                if args.overwrite:
                    os.remove(localfile)
                else:
                    raise Exception(
                        "file {0} cannot be overwritten".format(localfile))
            cl, bs = self.get_blob_connection()
            container, remotepath = self._interpret_path(remotepath, cl, bs)
            cl.download(bs, container, remotepath, localfile)
            return localfile

    @staticmethod
    def blob_downmerge_parser():
        """
        defines the way to parse the magic command ``%blob_downmerge``
        """
        parser = MagicCommandParser(prog="blob_downmerge",
                                    description='download a set of files from a blob storage folder, files will ' +
                                    'be merged, we assume the container is the first element to the remote path')
        parser.add_argument(
            'remotepath',
            type=str,
            help='remote path of the folder to download')
        parser.add_argument(
            'localfile',
            type=str,
            help='local name for the downloaded merged file')
        parser.add_argument(
            '-o',
            '--overwrite',
            action='store_true',
            default=False,
            help='overwrite the local file')
        return parser

    @line_magic
    def blob_downmerge(self, line):
        """
        download all files from a folder,
        see :ref:`l-magic-path-container`

        Example::

            %blob_downmerge remotepath localfile

        the command does not allow spaces in file names

        .. nbref::
            :tag: Azure
            :title: blob_downmerge

            The code for magic command ``%blob_downmerge`` is equivalent to::

                from pyensae.remote import AzureClient
                cl = AzureClient(account_name, account_key, hadoop_server, hadoop_password, pseudo=username)
                bs = cl.open_blob_service()
                cl.download_merge(bs, container, remotepath, localfile)



        .. versionadded:: 1.1
        """
        parser = self.get_parser(
            MagicAzure.blob_downmerge_parser, "blob_downmerge")
        args = self.get_args(line, parser)

        if args is not None:
            localfile, remotepath = args.localfile, args.remotepath
            if os.path.exists(localfile):
                if args.overwrite:
                    os.remove(localfile)
                else:
                    raise Exception(
                        "file {0} cannot be overwritten".format(localfile))

            cl, bs = self.get_blob_connection()
            container, remotepath = self._interpret_path(remotepath, cl, bs)
            cl.download_merge(bs, container, remotepath, localfile)
            return localfile

    @line_magic
    def blob_rm(self, line):
        """
        calls @see me blob_delete

        .. versionadded:: 1.1
        """
        return self.blob_delete(line)

    @staticmethod
    def blob_delete_parser():
        """
        defines the way to parse the magic command ``%blob_delete``
        """
        parser = MagicCommandParser(prog="blob_delete",
                                    description='remove a remote path')
        parser.add_argument(
            'remotepath',
            type=str,
            help='remote path to remove')
        return parser

    @line_magic
    def blob_delete(self, line):
        """
        deletes a blob,
        see :ref:`l-magic-path-container`

        .. nbref::
            :tag: Azure
            :title: blob_delete

            The code for magic command ``%blob_delete`` is equivalent to::

                from pyensae.remote import AzureClient
                cl = AzureClient(account_name, account_key, hadoop_server, hadoop_password, pseudo=username)
                bs = cl.open_blob_service()
                cl.delete_blob(bs, container, remotepath)


        """
        parser = self.get_parser(MagicAzure.blob_delete_parser, "blob_delete")
        args = self.get_args(line, parser)

        if args is not None:
            cl, bs = self.get_blob_connection()
            container, remotepath = self._interpret_path(
                args.remotepath, cl, bs)
            cl.delete_blob(bs, container, remotepath)
            return True

    @staticmethod
    def blob_rmr_parser():
        """
        defines the way to parse the magic command ``%blob_rmr``
        """
        parser = MagicCommandParser(prog="blob_rmr",
                                    description='remove a remote folder')
        parser.add_argument(
            'remotepath',
            type=str,
            help='remote path to remove')
        return parser

    @line_magic
    def blob_rmr(self, line):
        """
        deletes a folder,
        see :ref:`l-magic-path-container`

        .. nbref::
            :tag: Azure
            :title: blob_rmr

            The code for magic command ``%blob_rmr`` is equivalent to::

                from pyensae.remote import AzureClient
                cl = AzureClient(account_name, account_key, hadoop_server, hadoop_password, pseudo=username)
                bs = cl.open_blob_service()
                cl.delete_folder(bs, container, remotepath)


        """
        parser = self.get_parser(MagicAzure.blob_rmr_parser, "blob_rmr")
        args = self.get_args(line, parser)

        if args is not None:
            cl, bs = self.get_blob_connection()
            container, remotepath = self._interpret_path(
                args.remotepath, cl, bs)
            return cl.delete_folder(bs, container, remotepath)

    @staticmethod
    def blob_copy_parser():
        """
        defines the way to parse the magic command ``%blob_copy``
        """
        parser = MagicCommandParser(prog="blob_copy",
                                    description='copy a blob folder')
        parser.add_argument(
            'remotepath',
            type=str,
            help='remote path to remove')
        parser.add_argument(
            'remotedest',
            type=str,
            help='remote destination')
        return parser

    @line_magic
    def blob_copy(self, line):
        """
        copy a blob storage,
        see :ref:`l-magic-path-container`

        .. nbref::
            :tag: Azure
            :title: blob_copy

            The code for magic command ``%blob_copy`` is equivalent to::

                from pyensae.remote import AzureClient
                cl = AzureClient(account_name, account_key, hadoop_server, hadoop_password, pseudo=username)
                bs = cl.open_blob_service()
                cl.copy_blob(bs, container, dest, src)


        """
        parser = self.get_parser(MagicAzure.blob_copy_parser, "blob_copy")
        args = self.get_args(line, parser)

        if args is not None:
            src, dest = args.remotepath, args.remotedest
            cl, bs = self.get_blob_connection()
            container, src = self._interpret_path(src, cl, bs)
            container_, dest = self._interpret_path(dest, cl, bs)
            if container != container_:
                raise AzureException(
                    "containers should be the same: {0} != {1}".format(
                        container,
                        container_),
                    None)
            cl.copy_blob(bs, container, dest, src)
            return True

    @staticmethod
    def hd_queue_parser():
        """
        defines the way to parse the magic command ``%hd_queue``
        """
        parser = MagicCommandParser(prog="hd_queue",
                                    description='displays the job queue')
        parser.add_argument(
            '-s',
            '--showall',
            action="store_true",
            default=False,
            help="show all jobs, only users'")
        return parser

    @line_magic
    def hd_queue(self, line):
        """
        defines ``%hd_queue``

        .. nbref::
            :tag: Azure
            :title: hd_queue

            The code for magic command ``%hd_queue`` is equivalent to::

                from pyensae.remote import AzureClient
                cl = AzureClient(account_name, account_key, hadoop_server, hadoop_password, pseudo=username)
                bs = cl.open_blob_service()
                cl.job_queue(showall=showall)


        """
        parser = self.get_parser(MagicAzure.hd_queue_parser, "hd_queue")
        args = self.get_args(line, parser)

        if args is not None:
            showall = args.showall
            cl, bs = self.get_blob_connection()
            return cl.job_queue(showall=showall)

    @staticmethod
    def hd_job_status_parser():
        """
        defines the way to parse the magic command ``%hd_job_status``
        """
        parser = MagicCommandParser(prog="hd_job_status",
                                    description='get the status of the job')
        parser.add_argument(
            'jobid',
            type=str,
            help='job id')
        return parser

    @line_magic
    def hd_job_status(self, line):
        """
        defines ``%hd_job_status``

        .. nbref::
            :tag: Azure
            :title: hd_job_status

            The code for magic command ``%hd_job_status`` is equivalent to::

                from pyensae.remote import AzureClient
                cl = AzureClient(account_name, account_key, hadoop_server, hadoop_password, pseudo=username)
                bs = cl.open_blob_service()
                cl.job_status(jobid)


        """
        parser = self.get_parser(
            MagicAzure.hd_job_status_parser, "hd_job_status")
        args = self.get_args(line, parser)

        if args is not None:
            jobid = args.jobid
            cl, bs = self.get_blob_connection()
            return cl.job_status(jobid)

    @staticmethod
    def hd_job_kill_parser():
        """
        defines the way to parse the magic command ``%hd_job_kill``
        """
        parser = MagicCommandParser(prog="hd_job_kill",
                                    description='kill a job')
        parser.add_argument(
            'jobid',
            type=str,
            help='job id')
        return parser

    @line_magic
    def hd_job_kill(self, line):
        """
        defines ``%hd_job_kill``

        .. nbref::
            :tag: Azure
            :title: hd_job_kill

            The code for magic command ``%hd_job_kill`` is equivalent to::

                from pyensae.remote import AzureClient
                cl = AzureClient(account_name, account_key, hadoop_server, hadoop_password, pseudo=username)
                bs = cl.open_blob_service()
                cl.job_kill(jobid)


        """
        parser = self.get_parser(MagicAzure.hd_job_kill_parser, "hd_job_kill")
        args = self.get_args(line, parser)

        if args is not None:
            jobid = args.jobid
            cl, bs = self.get_blob_connection()
            return cl.job_kill(jobid)

    @line_magic
    def hd_wasb_prefix(self, line):
        """
        defines ``%hd_wasb_prefix``, returns the prefix used to connect to the blob storage,
        it includes the *container* name
        """
        cl, bs = self.get_blob_connection()
        return cl.wasb_to_file(cl.account_name, "")

    @staticmethod
    def PIG_azure_parser():
        """
        defines the way to parse the magic command ``%%PIG_azure``
        """
        parser = MagicCommandParser(prog="PIG_azure",
                                    description='The command store the content of the cell as a local file.')
        parser.add_argument(
            'file',
            type=str,
            help='file name')
        return parser

    @cell_magic
    def PIG_azure(self, line, cell=None):
        """
        defines command ``%%PIG_azure``

        .. nbref::
            :tag: Azure
            :title: PIG_azure

            The code for magic command ``%PIG_azure`` is equivalent to::

                with open(filename, "w", encoding="utf8") as f:
                    f.write(script)


        """
        parser = self.get_parser(MagicAzure.PIG_azure_parser, "PIG_azure")
        args = self.get_args(line, parser)

        if args is not None:
            filename = args.file
            script = cell.replace("\r", "")
            with open(filename, "w", encoding="utf8") as f:
                f.write(script)

    @staticmethod
    def HIVE_azure_parser():
        """
        defines the way to parse the magic command ``%HIVE_azure``
        """
        parser = MagicCommandParser(prog="HIVE_azure",
                                    description='The command store the content of the cell as a local file.')
        parser.add_argument(
            'file',
            type=str,
            help='file name')
        return parser

    @cell_magic
    def HIVE_azure(self, line, cell=None):
        """
        defines command ``%%HIVE_azure``

        .. nbref::
            :tag: Azure
            :title: HIVE_azure

            The code for magic command ``%HIVE_azure`` is equivalent to::

                with open(filename, "w", encoding="utf8") as f:
                    f.write(script)


        """
        parser = self.get_parser(MagicAzure.HIVE_azure_parser, "HIVE_azure")
        args = self.get_args(line, parser)

        if args is not None:
            filename = args.file
            script = cell.replace("\r", "")
            with open(filename, "w", encoding="utf8") as f:
                f.write(script)

    @staticmethod
    def HIVE_azure_submit_parser():
        """
        defines the way to parse the magic command ``%HIVE_azure_submit``
        """
        parser = MagicCommandParser(prog="HIVE_azure_submit",
                                    description='Submits a job to the cluster, the job is local, the job is ' +
                                    'first uploaded to the cluster. The magic command populates the local variable last_job with the submitted job id.')
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
            '-s',
            '--stop-on-failure',
            action='store_true',
            default=False,
            help='if true, the job stops on failure right away')
        parser.add_argument(
            '-o',
            '--options',
            nargs='*',
            type=str,
            help='list of options for the job')
        return parser

    @line_magic
    def HIVE_azure_submit(self, line):
        """
        defines command ``%HIVE_azure_submit``

        .. nbref::
            :tag: Azure
            :title: HIVE_azure_submit

            The code for magic command ``%HIVE_azure_submit`` is equivalent to::

                from pyensae.remote import AzureClient
                cl = AzureClient(account_name, account_key, hadoop_server, hadoop_password, pseudo=username)
                bs = cl.open_blob_service()
                cl.hive_submit(bs, cl.account_name, hive_file_name, dependencies, **options)


        """
        parser = self.get_parser(
            MagicAzure.HIVE_azure_submit_parser, "HIVE_azure_submit")
        args = self.get_args(line, parser)

        if args is not None:
            pig = args.file
            pys = [_ for _ in args.dependency if _.endswith(
                ".py")] if args.dependency is not None else []

            if not os.path.exists(pig):
                raise FileNotFoundError(pig)

            options = {"stop_on_failure": False}
            if args.options is not None:
                options.update({k: True for k in args.options})

            cl, bs = self.get_blob_connection()
            r = cl.HIVE_submit(bs, cl.account_name, pig, pys, **options)

            self.shell.user_ns["last_job"] = r
            return r

    @staticmethod
    def hd_pig_submit_parser():
        """
        defines the way to parse the magic command ``%hd_pig_submit``
        """
        parser = MagicCommandParser(prog="hd_pig_submit",
                                    description='Submits a job to the cluster, the job is local, the job is ' +
                                    'first uploaded to the cluster. The magic command populates the local variable last_job with the submitted job id.')
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
            '-s',
            '--stop-on-failure',
            action='store_true',
            default=False,
            help='if true, the job stops on failure right away')
        parser.add_argument(
            '-o',
            '--options',
            nargs='*',
            type=str,
            help='list of options for the job')
        return parser

    @line_magic
    def hd_pig_submit(self, line):
        """
        defines command ``%hd_pig_submit``

        .. nbref::
            :tag: Azure
            :title: hd_pig_submit

            The code for magic command ``%hd_pig_submit`` is equivalent to::

                from pyensae.remote import AzureClient
                cl = AzureClient(account_name, account_key, hadoop_server, hadoop_password, pseudo=username)
                bs = cl.open_blob_service()
                cl.pig_submit(bs, cl.account_name, pig_file_name, dependencies, **options)


        """
        parser = self.get_parser(
            MagicAzure.hd_pig_submit_parser, "hd_pig_submit")
        args = self.get_args(line, parser)

        if args is not None:
            pig = args.file
            pys = [_ for _ in args.dependency if _.endswith(
                ".py")] if args.dependency is not None else []

            if not os.path.exists(pig):
                raise FileNotFoundError(pig)

            options = {"stop_on_failure": False}
            if args.options is not None:
                options.update({k: True for k in args.options})

            cl, bs = self.get_blob_connection()
            r = cl.pig_submit(bs, cl.account_name, pig, pys, **options)

            self.shell.user_ns["last_job"] = r
            return r

    @staticmethod
    def hd_tail_stderr_parser():
        """
        defines the way to parse the magic command ``%hd_tail_stderr``
        """
        parser = MagicCommandParser(prog="hd_tail_stderr",
                                    description='Submits a job to the cluster, the job is local, the job is first ' +
                                    'uploaded to the cluster. The magic command populates the local variable last_job with the submitted job id.')
        parser.add_argument(
            'jobid',
            type=str,
            help='job id')
        parser.add_argument(
            '-n',
            '--nblines',
            type=int,
            default=20,
            help='number of lines to display')
        parser.add_argument(
            '--raw-output',
            default=False,
            action='store_true',
            help='display raw text instead of HTML')
        return parser

    @line_magic
    def hd_tail_stderr(self, line):
        """
        defines ``%hd_tail_stderr``

        @warning This function gets the status of the job to get the script name.
                 But the rediction uses the script name and not the job id. As a consequence,
                 if the same script name is run multiple times, the redirection will contain
                 the output of multiples jobs.

        .. nbref::
            :tag: Azure
            :title: hd_tail_stderr

            The code for magic command ``%hd_tail_stderr`` is equivalent to::

                from pyensae.remote import AzureClient
                cl = AzureClient(account_name, account_key, hadoop_server, hadoop_password, pseudo=username)
                bs = cl.open_blob_service()
                cl.standard_outputs(job_id, bs, cl.account_name, ".")


        """
        parser = self.get_parser(
            MagicAzure.hd_tail_stderr_parser, "hd_tail_stderr")
        args = self.get_args(line, parser)

        if args is not None:
            job = args.jobid
            nbline = args.nblines
            if len(job) == 0:
                if self.shell is None or "last_job" not in self.shell.user_ns:
                    raise Exception("no submitted jobs found in the workspace")
                else:
                    job = self.shell.user_ns["last_job"]["jid"]

            cl, bs = self.get_blob_connection()
            out, err = cl.standard_outputs(job, bs, cl.account_name, ".")

            lines = err.split("\n")
            show = "\n".join(_.strip("\n\r") for _ in lines[-nbline:])
            show = show.replace(
                "ERROR",
                '<b><font color="#DD0000">ERROR</font></b>')

            if args.raw_output:
                if len(out) > 0:
                    lineo = out.split("\n")
                    shoo = "\n".join(_.strip("\n\r") for _ in lineo[-nbline:])
                    return shoo
                else:
                    return show
            else:
                if len(out) > 0:
                    lineo = out.split("\n")
                    shoo = "\n".join(_.strip("\n\r") for _ in lineo[-nbline:])
                    return HTML(
                        "<pre>\n%s\n</pre><br /><b>OUT:</b><br /><pre>\n%s\n</pre>" % (show, shoo))
                else:
                    return HTML("<pre>\n%s\n</pre><br />" % show)

    def _run_jython(self, cell, filename, func_name, args, true_jython=None):
        """
        run a jython script

        @param      cell            content of the cell
        @param      filename        filename used to store the content of the cell
        @param      func_name       function name
        @param      args            list of arguments to run
        @param      true_jython     jython (True) or this Python (False)
        @return                     out, err
        """
        with open(filename, 'r', encoding="utf8") as pyf:
            content = pyf.read()
        temp = filename.replace(".py", ".temp.py")
        with open(temp, "w", encoding="utf8") as pyf:
            pyf.write("""
                            # -*- coding: utf8 -*-
                            if __name__ != '__lib__':
                                def outputSchema(dont_care):
                                    def wrapper(func):
                                        def inner(*args, **kwargs):
                                            return func(*args, **kwargs)
                                        return inner
                                    return wrapper
                                def outputSchemaFunction(schema_def):
                                    def decorator(func):
                                        func.outputSchemaFunction = schema_def
                                        return func
                                    return decorator
                                def schemaFunction(schema_def):
                                    def decorator(func):
                                        func.schemaFunction = schema_def
                                        return func
                                    return decorator
                        """.replace("                            ", ""))
            pyf.write(
                content.replace(
                    "except Exception,",
                    "except Exception as "))
            s_func_name = func_name if isinstance(
                func_name, str) else func_name.__name__.split(".")[-1]
            pyf.write("""
                            if __name__ != '__lib__':
                                import sys
                                for row in sys.stdin:
                                    row = row.strip()
                                    res = {0}(row)
                                    sys.stdout.write(str(res))
                                    sys.stdout.write("\\n")
                                    sys.stdout.flush()
                    """.format(s_func_name).replace("                            ", ""))

        cmd = sys.executable.replace(
            "pythonw",
            "python") + " " + temp + " " + " ".join("{}".format(_) for _ in args)
        tosend = cell

        if true_jython:
            download_java_standalone()
            out, err = run_jython(temp, sin=cell, timeout=10)
        else:
            out, err = run_cmd(
                cmd, wait=True, sin=tosend, communicate=True, timeout=10, shell=False)
        return out, err

    @staticmethod
    def runjython_parser():
        """
        defines the way to parse the magic command ``%%runjython``
        """
        parser = MagicCommandParser(prog="runjython",
                                    description='run a jython script used for streaming in HDInsight, ' +
                                    'the function appends fake decorator a timeout is set up at 10s')
        parser.add_argument(
            'file',
            type=str,
            help='file name')
        parser.add_argument(
            'function_name',
            type=str,
            help='function name')
        parser.add_argument(
            '--raw-output',
            default=False,
            action='store_true',
            help='display raw text instead of HTML')
        parser.add_argument(
            'args',
            type=str,
            nargs="*",
            help='arguments')
        return parser

    @cell_magic
    def runjpython(self, line, cell=None):
        """
        defines command ``%%runjython``

        .. nbref::
            :tag: Azure
            :title: runjpython

            Run a jython script used for streaming in HDInsight,
            the function appends fake decorator
            a timeout is set up at 10s

            The magic function create another file included the decoration.
            It runs the script with this version of Python.

            See `In a python script how can I ignore Apache Pig's Python Decorators for standalone unit testing <http://stackoverflow.com/questions/18223898/in-a-python-script-how-can-i-ignore-apache-pigs-python-decorators-for-standalon>`_

            See @see me _run_jython to see the code.



        .. versionadded:: 1.1
        """
        parser = self.get_parser(MagicAzure.runjpython_parser, "runjpython")
        args = self.get_args(line, parser)

        if args is not None:
            filename = args.file
            func_name = args.function_name
            args = args.args
            out, err = self._run_jython(cell, filename, func_name, args, False)
            if args.raw_output:
                if len(err) > 0:
                    return err
                else:
                    return out
            else:
                if len(err) > 0:
                    return HTML(
                        '<font color="#DD0000">Error</font><br /><pre>\n%s\n</pre>' % err)
                else:
                    return HTML('<pre>\n%s\n</pre>' % out)

    @staticmethod
    def jython_parser():
        """
        defines the way to parse the magic command ``%%jython``
        """
        parser = MagicCommandParser(prog="jython",
                                    description='run a jython script used for streaming in HDInsight, it does it using Jython')
        parser.add_argument(
            'file',
            type=str,
            help='file name')
        parser.add_argument(
            'function_name',
            type=str,
            help='function name')
        parser.add_argument(
            '--raw-output',
            default=False,
            action='store_true',
            help='display raw text instead of HTML')
        parser.add_argument(
            'args',
            type=str,
            nargs="*",
            help='arguments')
        return parser

    @cell_magic
    def jython(self, line, cell=None):
        """
        defines command ``%%runjython``

        run a jython script used for streaming in HDInsight,
        the function appends fake decorator
        a timeout is set up at 10s

        The magic function create another file included the decoration.
        It runs the script with Jython (see the default version)

        See `In a python script how can I ignore Apache Pig's Python Decorators for standalone unit testing <http://stackoverflow.com/questions/18223898/in-a-python-script-how-can-i-ignore-apache-pigs-python-decorators-for-standalon>`_

        .. versionadded:: 1.1
        """
        parser = self.get_parser(MagicAzure.jython_parser, "jpython")
        args = self.get_args(line, parser)

        if args is not None:
            filename = args.file
            func_name = args.function_name
            raw_output = args.raw_output
            args = args.args
            out, err = self._run_jython(cell, filename, func_name, args, True)
            if raw_output:
                if len(err) > 0:
                    return err
                else:
                    return out
            else:
                if len(err) > 0:
                    return HTML(
                        '<font color="#DD0000">Error</font><br /><pre>\n%s\n</pre>' % err)
                else:
                    return HTML('<pre>\n%s\n</pre>' % out)

    @staticmethod
    def blob_head_parser():
        """
        defines the way to parse the magic command ``%blob_head``
        """
        parser = MagicCommandParser(prog="blob_head",
                                    description='get the head of stream in a dataframe')
        parser.add_argument(
            'remotepath',
            type=str,
            help='remote path of the file to download')
        parser.add_argument(
            '-m',
            '--merge',
            action='store_true',
            default=False,
            help='merges files in a folder')
        parser.add_argument(
            '-d',
            '--df',
            action='store_true',
            default=True,
            help='results as a dataframe')
        parser.add_argument(
            '-s',
            '--size',
            type=int,
            default=2 ** 20,
            help='size of data to get')
        parser.add_argument(
            '-e',
            '--encoding',
            type=str,
            default="utf8",
            help='encoding')
        parser.add_argument(
            '--sep',
            type=str,
            default="\t",
            help='column separator')
        parser.add_argument(
            '--header',
            default='infer',
            help='results as a dataframe')
        return parser

    @line_magic
    def blob_head(self, line):
        """
        download a file from the blob storage
        and display its head, see :ref:`l-magic-path-container`

        Example::

            %blob_head remotepath

        the command does not allow spaces in file names

        .. nbref::
            :tag: Azure
            :title: blob_head

            The code for magic command ``%blob_head`` is equivalent to::

                from pyensae.remote import AzureClient
                cl = AzureClient(account_name, account_key, hadoop_server, hadoop_password, pseudo=username)
                bs = cl.open_blob_service()
                df = cl.df_head(bs, container, remotepath, localfile)

        """
        parser = self.get_parser(MagicAzure.blob_head_parser, "blob_head")
        args = self.get_args(line, parser)

        if args is not None:
            remotepath = args.remotepath
            cl, bs = self.get_blob_connection()
            container, remotepath = self._interpret_path(remotepath, cl, bs)
            res = cl.df_head(bs, container, remotepath,
                             stop_at=args.size, encoding=args.encoding,
                             as_df=args.df, merge=args.merge, sep=args.sep,
                             header=args.header)
            return res

    @staticmethod
    def blob_path_parser():
        """
        defines the magic command ``%blob_path``,
        checks the path used in commands ``blob_down``, ``blob_up``
        """
        parser = MagicCommandParser(prog="blob_path",
                                    description='remove a remote path')
        parser.add_argument(
            'remotepath',
            type=str,
            help='remote path to interpret')
        return parser

    @line_magic
    def blob_path(self, line):
        """
        checks the path used in commands ``blob_down``, ``blob_up``,
        see @see me _interpret_path, :ref:`l-magic-path-container`

        .. nbref::
            :tag: Azure
            :title: blob_path

            The code for magic command ``%blob_path`` is equivalent to::

                if line.startswith("/"):
                    container = account_name
                    remotepath = remotepath.lstrip("/")
                else:
                    spl = line.split("/")
                    container = spl[0]
                    remotepath = None if len(spl) == 1 else "/".join(spl[1:])

                result = container, remotepath


        """
        parser = self.get_parser(MagicAzure.blob_delete_parser, "blob_delete")
        args = self.get_args(line, parser)

        if args is not None:
            cl, bs = self.get_blob_connection()
            container, remotepath = self._interpret_path(
                args.remotepath, cl, bs)
            return container, remotepath


def register_azure_magics(ip=None):
    """
    register magics function, can be called from a notebook

    @param      ip      from ``get_ipython()``
    """
    if ip is None:
        from IPython import get_ipython
        ip = get_ipython()
    ip.register_magics(MagicAzure)
