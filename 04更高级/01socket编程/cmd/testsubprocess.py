#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by fengL on 2017/9/26

import subprocess

if __name__ == '__main__':
    #通过子进程去执行命令，然后把执行结果通过管道的方式发送到主进程里面。
    a = subprocess.Popen("dir", shell=True, stdout=subprocess.PIPE)
    print(a)#a是一个子进程。
    print(a.stdout.read())#将子进程执行的结果，通过管道的方式发送到主进程的stdout
    #结果是以byte的类型发送过来的，如果要查看就使用str（）转一下。
    print(str(a.stdout.read(),"utf8"))