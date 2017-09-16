#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by fengL on 2017/9/16

#1：多进程的基本使用：创建多进程
# from multiprocessing import Process
# import time
# def f(name):
#     time.sleep(1)
#     print('hello', name,time.ctime())
#
# #在Windows下面启动子进程需要添加如下的语句。
# if __name__ == '__main__':
#     p_list=[]
#     #这里创建了三个子进程。
#     for i in range(3):
#         p = Process(target=f, args=('alvin',))
#         p_list.append(p)
#         p.start()
#     #等到所有的子进程都执行完毕
#     for i in p_list:
#         p.join()
#     print('end')


#2：创建自定义的进程：通过继承Process的方式实现
# from multiprocessing import Process
# import time
#
# class MyProcess(Process):
#     def __init__(self):
#         super(MyProcess, self).__init__()
#         #self.name = name
#
#     def run(self):
#         time.sleep(1)
#         print ('hello', self.name,time.ctime())
#
#
# if __name__ == '__main__':
#     p_list=[]
#     for i in range(3):
#         p = MyProcess()
#         p.start()
#         p_list.append(p)
#
#     for p in p_list:
#         p.join()
#
#     print('end')


#3：获取pid：每一个进程都有一个父进程。意味着有一个根进程。
# from multiprocessing import Process
# import os
# import time
# def info(title):
#     print(title)
#     print('module name:', __name__)
#     print('parent process:', os.getppid())
#     print('process id:', os.getpid())
#
#
# def f(name):
#     info('\033[31;1mfunction f\033[0m')
#     print('hello', name)
#
# if __name__ == '__main__':
#     info('\033[32;1mmain process line\033[0m')
#     time.sleep(100)
#     p = Process(target=info, args=('bob',))
#     p.start()
#     p.join()

#4：manager：数据共享
from multiprocessing import Process, Manager

def f(d, l,n):
    d[n] = '1'
    d['2'] = 2
    d[0.25] = None
    l.append(n)
    print(l)

if __name__ == '__main__':
    #使用就不用手动进行关闭
    with Manager() as manager:
        #通过manager创建一个共享的字典
        d = manager.dict()
        #通过manager创建一个共享的list
        l = manager.list(range(5))
        p_list = []
        for i in range(10):
            p = Process(target=f, args=(d, l,i))
            p.start()
            p_list.append(p)
        for res in p_list:
            res.join()

        print(d)
        print(l)