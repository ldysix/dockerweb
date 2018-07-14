#coding=utf-8

import paramiko
from readconfig import ReadConfig
#get ssh connection
class Exec:
    def __init__(self):
        pass
    def getSSHConnection(self):
        ssh = paramiko.SSHClient()
        key = paramiko.AutoAddPolicy()
        ssh.set_missing_host_key_policy(key)
        rc=ReadConfig()
        host,port,user,password,timeout=rc.readDockerweb()
        ssh.connect(host,int(port),user, password ,timeout=int(timeout))
        return ssh

    def execCommand(self,cmd):
        e=Exec()
        ssh=e.getSSHConnection();
        stdin,stdout,stderr=ssh.exec_command(cmd)
        #stdoutmsg=""
        #stderrmsg=""
        stdoutmsgl=[]
        stderrmsgl=[]
        sout=stdout.readlines();
        if sout:
            for st in sout:
                #stdoutmsg=stdoutmsg+st
                t=st.strip("\n")
                #print t
                stdoutmsgl.append(t)
        serr=stderr.readlines();
        if serr:
            for sr in serr:
                #stderrmsg=stdoutmsg+sr
                r=sr.strip("\n")
                #print r
                stderrmsgl.append(r)
        ssh.close();
        if stdoutmsgl:
            #print "stdout="+stdoutmsg
            return stdoutmsgl
        elif stderrmsgl:
            #print "stderr="+stderrmsg
            return  stderrmsgl
        else:
            return stdoutmsgl