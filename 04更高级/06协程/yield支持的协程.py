#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by fengL on 2017/9/16


import time,queue
def consumre(name):
    print("--->starting eating baozi.......")
    while True:
        new_baozi = yield
        print("[%s] is eating baozi %s" % (name,new_baozi))
        # time.sleep(1)

def producer():
    con.__next__()
    con2.__next__()
    n = 0
    while n < 5:
        n+=1
        con.send(n)
        con2.send(n)
        print("\033[32;1m[producer]\033[0m is making baoz %s]]" % n)


if __name__ == "__main__":
    con = consumre("c1")#创建一个生成器 con
    con2 = consumre("c2")#创建一个生成器 con2
    p = producer()#执行producer函数。

