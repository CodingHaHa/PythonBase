#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by fengL on 2017/9/16

#1：使用queue实现进程间的通信
# from multiprocessing import Process, Queue
#
# def f(q,n):
#     q.put([42, n, 'hello'])
#
# if __name__ == '__main__':
#     #在主线程中创建Queue
#     q = Queue()#这里是进程queue与线程queue没有任何关系。
#     p_list=[]
#     #创建3个进程
#     for i in range(3):
#         p = Process(target=f, args=(q,i))
#         p_list.append(p)
#         p.start()
#     #获取数据
#     print(q.get())
#     print(q.get())
#     print(q.get())
#
#     for i in p_list:
#             i.join()

#2：使用pipe实现进程通信：子进程和父进程进程通信。
from multiprocessing import Process, Pipe

def f(conn):
    #通过子进程的管道，子进程可以从父进程发送和接收数据
    conn.send([42, None, 'hello'])
    conn.close()

if __name__ == '__main__':
    #主进程，和子进程的管道
    parent_conn, child_conn = Pipe()
    p = Process(target=f, args=(child_conn,))
    p.start()
    #父进程通过管道，可以接收和发送数据给子进程。
    print(parent_conn.recv())  # prints "[42, None, 'hello']"
    p.join()