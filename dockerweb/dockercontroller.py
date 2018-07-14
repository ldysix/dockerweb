#coding=utf-8

from django.http import HttpResponse
from django.shortcuts import render_to_response
import json
from service import Service
from django.views.decorators.csrf import csrf_exempt


def showMain(request):
    return render_to_response('main.html')

'''
版本信息
flag=1,简单版本信息
flag=2，详细的版本信息
'''
def showVersion(request):
    print 'start showVersion'
    if request.method=="GET":
        flag=request.GET.get("flag")
        print flag
        s=Service()
        stdmsg=s.showVersion(flag)
        return HttpResponse(json.dumps({"rst":stdmsg}))
    else:
        return HttpResponse(json.dumps({"rst":"系统升级中"}))


'''
docker操作
flag="1",启动
flag="2",停止
flag="3",重启
flag="4",状态
xtbb=1,ubuntu
xtbb=2,centos6及以下
xtbb=3,centos7及以上
'''
def execDocker(request):
    print  "start execDocker()"
    if request.method=="GET":
        flag=request.GET.get("flag")
        xtbb=request.GET.get("xtbb")
        s=Service()
        stdmsg=s.execDocker(flag,xtbb)
        return HttpResponse(json.dumps({"rst":stdmsg}))
    else:
        return HttpResponse(json.dumps({"rst":"系统升级中"}))

'''
flag=1,查看镜像
flag=2,删除镜像
flag=3,拉取镜像
flag=4,上传镜像
'''
def execImages(request):
    print "start execImages"
    if request.method=="GET":
        flag=request.GET.get("flag")
        str=request.GET.get("str")
        s=Service()
        stdmsg=s.execImages(flag,str)
        return HttpResponse(json.dumps({"rst":stdmsg}))
    else:
        return  HttpResponse(json.dumps({"rst":"系统升级中"}));

'''
容器
flag=1，查看全部容器
flag=2，查看运行容器
flag=3，删除全部容器
flag=4，创建容器（按步骤）
flag=5，创建容器（默认）
flag=6，创建容器（自己）
flag=7，正常删除容器
flag=8，强制删除容器
flag=9，启动容器
flag=10，停止容器
flag=11，容器详细信息
'''
def execContainer(request):
    print "start execContainer"
    if request.method=="GET":
        flag=request.GET.get("flag")
        if flag=="4":
            return render_to_response("createcontainer.html")
        else:
            str=request.GET.get("str")
            s=Service()
            stdmsg=s.execContainer(flag,str)
            return HttpResponse(json.dumps({"rst":stdmsg}))
    else:
        return HttpResponse(json.dumps({"rst":"系统升级中"}))

'''
创建容器（按步骤）
'''
def createContainer(request):
    print "start createContainer()"
    if request.method=="GET":
        return render_to_response("createcontainer.html")

'''
创建容器（按步骤）
'''
def execCreateContainer(request):
    print "start execCreateContainer()"
    if request.method=="GET":
        dictCon={}
        rqmc=request.GET.get("rqmc")
        dictCon["rqmc"]=rqmc
        rqzjm=request.GET.get("rqzjm")
        dictCon["rqzjm"]=rqzjm
        wlpz=request.GET.get("wlpz")
        dictCon["wlpz"]=wlpz
        srsclx=request.GET.get("srsclx")
        dictCon["srsclx"]=srsclx
        rqdnsfwq=request.GET.get("rqdnsfwq")
        dictCon["rqdnsfwq"]=rqdnsfwq
        rqdnsssym=request.GET.get("rqdnsssym")
        dictCon["rqdnsssym"]=rqdnsssym
        szjdk=request.GET.get("szjdk")
        dictCon["szjdk"]=szjdk
        rqdk=request.GET.get("rqdk")
        dictCon["rqdk"]=rqdk
        jxm=request.GET.get("jxm")
        dictCon["jxm"]=jxm
        s=Service()
        stdmsg=s.createContainer(dictCon)
        #print "stdmsg="+stdmsg
        return HttpResponse(json.dumps({"rst":stdmsg}))

'''
执行指令
'''
def execInputCommand(request):
    print "start execInputCommand"
    if request.method=="GET":
        cmd=request.GET.get("srzl")
        s=Service()
        stdmsg=s.execInputCommand(cmd)
        return HttpResponse(json.dumps({"rst":stdmsg}))

