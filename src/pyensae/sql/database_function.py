"""
@file

@brief      generic class to access a SQL database
"""

import os


from pyquickhelper.loghelper.flog import run_cmd


def get_list_server():
    """
    @return     a list of the available servers from this machine
    """
    cmd = "sqlcmd -Lc"
    out, err = run_cmd(cmd, wait=True, shell=True, log_error=False)
    line = out.split("\n")
    line = [_.strip("\r\n ") for _ in line]
    line = [_ for _ in line if len(_) > 0]

    # we place all server containing the machine name in the first place
    machine = os.environ.get("COMPUTERNAME", "------")
    line = sorted([(-1 if _.startswith(machine) else 0, _) for _ in line])
    line = [_[1] for _ in line]
    return line


def get_list_instance(server):
    """
    @param      server      server name
    @return                 a list of the available instance on a server
    """
    cmd = 'sqlcmd -S %s -Q "SELECT @@ServerName"' % server
    out, err = run_cmd(cmd, wait=True, shell=True, log_error=False)
    if len(err) > 0:
        cmd = 'sqlcmd -S %s\\SQLEXPRESS -Q "SELECT @@ServerName"' % server
        out, err = run_cmd(cmd, wait=True, shell=True, log_error=False)
        if len(err) > 0:
            raise Exception(
                "unable to find instances for server %s (%s)" %
                (server, err))

    li = [_.strip("\r\n ") for _ in out.split("\n")]
    li = [_ for _ in li if len(_) > 0]
    li = li[1:-1]
    return li


def get_list_database(instance):
    """
    @param      instance    instance name
    @return                 a list of the available database
    """
    cmd = 'sqlcmd -S %s -Q "SELECT name FROM master..sysdatabases"' % instance
    out, err = run_cmd(cmd, wait=True, shell=True, log_error=False)
    li = [_.strip("\r\n ") for _ in out.split("\n")]
    no = ["master", "tempdb", "model", "msdb"]
    li = [_ for _ in li if len(_) > 0 and _ not in no]
    li = li[2:-1]
    return li


def create_database(instance, database, exc=True):
    """
    create a database
    @param      instance    instance name
    @param      database    database name
    @param      exc         if True and if the database exists, raise an Exception

    Example:
    @code
    fLOG (OutputPrint = True)
    fLOG (get_list_database ('PCXAVIER\\SQLEXPRESS'))
    create_database ('PCXAVIER\\SQLEXPRESS', "essai_database")
    drop_database ('PCXAVIER\\SQLEXPRESS', "essai_database")
    @endcode
    """
    ins = get_list_database(instance)
    if database in ins:
        if exc:
            raise Exception("database %s already exists" % database)
    else:
        cmd = 'sqlcmd -S %s -Q "CREATE DATABASE %s"' % (instance, database)
        out, err = run_cmd(cmd, wait=True, shell=True, log_error=False)
        if len(err) > 0:
            raise Exception("error: %s" % err)


def drop_database(instance, database, exc=True):
    """
    remove a database
    @param      instance    instance name
    @param      database    database name
    @param      exc         if True and if the database does not exist, raise an Exception
    """
    ins = get_list_database(instance)
    if database not in ins:
        if exc:
            raise Exception("database %s does not exist" % database)
    else:
        cmd = 'sqlcmd -S %s -Q "DROP DATABASE %s"' % (instance, database)
        out, err = run_cmd(cmd, wait=True, shell=True, log_error=False)
        if len(err) > 0:
            raise Exception("error: %s" % err)
