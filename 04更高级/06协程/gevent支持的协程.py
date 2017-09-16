#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by fengL on 2017/9/16

#1：使用greenlet对象来实现协程，任务间的切换
# from greenlet import  greenlet
#
# def test1():
#     print(12)
#     gr2.switch()#切换到gr2
#     print(34)
#     gr2.switch()
#
#
# def test2():
#     print(56)
#     gr1.switch()
#     print(78)
#
# gr1 = greenlet(test1)
# #生成两个greenlet对象
# print(gr1)#<greenlet.greenlet object at 0x0000000001DF1898>
# gr2 = greenlet(test2)
# #第一次进行切换到grl，让它开始执行。
# gr1.switch()
#
# #通过switch来进行任务之间的切换。这是是我们可以手动控制的。


#2：gevent支持的并发编程
# import gevent
#
#
# def func1():
#     print('\033[31;1m李闯在跟海涛搞...\033[0m')
#     gevent.sleep(2)#模拟IO阻塞情况
#     #一遇到io阻塞，就会进行切换（协程在一个线程里面进行切换）而time.sleep是CPU的切换
#     print('\033[31;1m李闯又回去跟继续跟海涛搞...\033[0m')
#
#
# def func2():
#     print('\033[32;1m李闯切换到了跟海龙搞...\033[0m')
#     gevent.sleep(1)#模拟IO阻塞情况
#     # 一遇到io阻塞，就会进行切换（协程在一个线程里面进行切换）而time.sleep是CPU的切换
#     print('\033[32;1m李闯搞完了海涛，回来继续跟海龙搞...\033[0m')
#
# #通过joinall激活
# gevent.joinall([
#     gevent.spawn(func1),
#     gevent.spawn(func2),
#     # gevent.spawn(func3),
# ])

#3：爬取网页
from gevent import monkey
#最大程度监听IO阻塞
monkey.patch_all()

from urllib.request import urlopen
import gevent
import time

def f(url):
    print("GET: %s" % url)
    resp = urlopen(url)
    data = resp.read()

    with open("xiaohua.html","wb",) as f:
        f.write(data)
    print("%d bytes received from %s" % (len(data),url) )



l = ["https://www.python.org/","https://www.yahoo.com/","https://github.com"]
start = time.time()

#直接串行执行
# for i in l:
#     f(i)

#使用协程
gevent.joinall([
    gevent.spawn(f,"https://www.python.org/"),
    gevent.spawn(f,"https://www.yahoo.com/"),
    gevent.spawn(f,"https://github.com")
])

print(time.time() -start)