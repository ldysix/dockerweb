#coding=utf-8

from django.http import HttpResponse
from readconfig import  ReadConfig
from execcmd import Exec

def test(request):
    return HttpResponse("hello test")

if __name__=="__main__":

    rc=ReadConfig();
    host,port,user,password,timeout=rc.readDockerweb()
    print host
    print port
    print user
    print  password
    print timeout

    e=Exec()
    e.execCommand("l /root")



