#coding=utf-8

from execcmd import Exec

class Service:
    def __init__(self):
        pass
    '''
    版本信息
    '''
    def showVersion(self,flag):
        e=Exec()
        if flag=="1":
            cmd="docker -v"
            stdmsg=e.execCommand(cmd)
        elif flag=="2":
            cmd="docker version"
            stdmsg=e.execCommand(cmd)
        #print stdmsg
        return stdmsg

    '''
    docker操作
    '''
    def execDocker(self,flag,xtbb):
        e=Exec()
        cmd=""
        print "flag="+flag
        print "xtbb="+xtbb
        if flag=="1":
            if xtbb=="1":
                cmd="/etc/init.d/docker start"
                #stdmsg=e.execCommand(cmd)
            elif xtbb=="2":
                cmd="service docker start"
                #stdmsg=e.execCommand(cmd)
            elif xtbb=="3":
                cmd="systemctl start docker.service"
                #stdmsg=e.execCommand(cmd)
        elif flag=="2":
            if xtbb=="1":
                cmd="/etc/init.d/docker stop"
                #stdmsg=e.execCommand(cmd)
            elif xtbb=="2":
                cmd="service docker stop"
                #stdmsg=e.execCommand(cmd)
            elif xtbb=="3":
                cmd="systemctl stop docker.service"
        elif flag=="3":
            if xtbb=="1":
                cmd="/etc/init.d/docker restart"
            elif xtbb=="2":
                cmd="service docker restart"
            elif xtbb=="3":
                cmd="systemctl restart docker.service"
        elif flag=="4":
            if xtbb=="1":
                cmd="/etc/init.d/docker status"
            elif xtbb=="2":
                cmd="service docker status"
            elif xtbb=="3":
                cmd="systemctl status docker.service"
        elif flag=="5":
            cmd="docker info"
        stdmsg=e.execCommand(cmd)
        #print "stdmsg="+stdmsg
        return stdmsg

    '''
    镜像
    '''
    def execImages(self,flag,str):
        cmd=None
        if flag=="1":
            cmd="docker images"
        if flag=="2" and str:
            cmd="docker rmi "+str
        if flag=="3" and str:
            cmd="docker pull "+str
        if flag=="4" and str:
            cmd="docker "
        if flag=="5" and str:
            cmd="docker search "+str
        e=Exec()
        stdmsg=e.execCommand(cmd)
        #print "stdmsg="+stdmsg
        return stdmsg

    '''
容器
flag=1，查看全部容器
flag=2，查看运行容器
flag=3，删除全部容器
flag=4，创建容器（按步骤）
flag=5，创建容器（默认）
flag=6，创建容器（自己指令）
flag=7，正常删除容器
flag=8，强制删除容器
flag=9，启动容器
flag=10，停止容器
flag=11，容器详细信息
'''
    def execContainer(self,flag,str):
        cmd=None
        stdmsg=None
        if flag=="1":
            cmd="docker ps -a"
        elif flag=="2":
            cmd="docker ps"
        elif flag=="3":
            cmd="docker rm $(docker ps -aq)"
        elif flag=="4":
            return
        elif flag=="5" and str:
            cmd="docker run -d "+str+" /bin/bash"
        elif flag=="6" and str:
            cmd=str
        elif flag=="7" and str:
            cmd="docker rm "+str
        elif flag=="8" and str:
            cmd="docker stop "+str+" & "+"docker rm "+str
        elif flag=="9" and str:
            cmd="docker start "+str
        elif flag=="10" and str:
            cmd="docker stop "+str
        elif flag=="11" and str:
            cmd="docker inspect "+str
        e=Exec()
        stdmsg=e.execCommand(cmd)
        return stdmsg

    '''
    创建容器
    '''
    def createContainer(self,dictCon):
        cmd="docker create "
        if dictCon["rqmc"]:
            cmd=cmd+"--name "+dictCon["rqmc"]+" "
        if dictCon["rqzjm"]:
            cmd=cmd+"-h "+dictCon["rqzjm"]+" "
        if dictCon["wlpz"]:
            if dictCon["wlpz"]=="1":
                pass
            elif dictCon["wlpz"]=="2":
                cmd=cmd+"--net=none "
            elif dictCon["wlpz"]=="3":
                cmd=cmd+"--net=host "
            elif dictCon["wlpz"]=="4":
                #cmd=cmd+"--net=container:container_naem/id"
                pass
        if dictCon["srsclx"]:
            if dictCon["srsclx"]=="1":
                cmd=cmd+"-a stdin "
            elif dictCon["srsclx"]=="2":
                cmd=cmd+"-a stdout "
            elif dictCon["srsclx"]=="3":
                cmd=cmd+"-a stderr "
        if dictCon["rqdnsfwq"]:
            cmd=cmd+"--dns "+dictCon["rqdnsfwq"]+" "
        if dictCon["rqdnsssym"]:
            cmd=cmd+"--dns-search "+dictCon["rqdnsssym"]+" "
        if dictCon["szjdk"] and dictCon["rqdk"]:
            cmd=cmd+"-p "+dictCon["szjdk"]+":"+dictCon["rqdk"]+" "
        if dictCon["jxm"]:
            cmd=cmd+dictCon["jxm"]+" "
        cmd=cmd+"/bin/bash"
        print 'cmd='+cmd
        e=Exec()
        stdmsg=[]
        stdmsg=e.execCommand(cmd)
        return stdmsg
    '''
    输入指令
    '''
    def execInputCommand(self,cmd):
        e=Exec()
        stdmsg=e.execCommand(cmd)
        return stdmsg
