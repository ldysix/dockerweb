#coding=utf-8

import os

class ReadConfig:
    def __init__(self):
        self.host=None
        self.port=None
        self.user=None
        self.password=None
        self.timeout=None

    def readDockerweb(self):
        #host=None
        #port=None
        #user=None
        #password=None
        #timeout=None
        rootdir=os.getcwd();
        #print "rootdir="+rootdir
        path=rootdir+"/config/dockerweb.config"
        f=open(path,"r")
        #lines=f.readlines()
        for line in f:
            line=line.strip("\n")
            #print line
            subLine=line.split("=")
            if len(subLine)==2 and subLine[0]=="host":
                self.host=subLine[1]
            elif len(subLine)==2 and subLine[0]=="port":
                self.port=subLine[1]
            elif len(subLine)==2 and subLine[0]=="user":
                self.user=subLine[1]
            elif len(subLine)==2 and subLine[0]=="password":
                self.password=subLine[1]
            elif len(subLine)==2 and subLine[0]=="timeout":
                self.timeout=subLine[1]
        return self.host,int(self.port),self.user,self.password,int(self.timeout)
