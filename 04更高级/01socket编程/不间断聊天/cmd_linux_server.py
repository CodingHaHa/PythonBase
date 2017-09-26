#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by fengL on 2017/9/26
#对于在Linux操作系统中，直接关闭client端连接
#它不会报错，而是使得从当前连接获取的数据为None.

import socket
server = socket.socket()
addr = ("127.0.0.1",8080)
server.bind(addr)
#listen表示除了正在进行通信的链接外，还可以让其他三个链接进行排队，但是不会与排队的链接进行通信。
#如果还有其他（第五个连接）想来连接server端，就会被server端积极的拒绝。
server.listen(3)
print("waiting........")

#1:整个while循环实现可以获取多个Client端连接
while 1:
    conn, addr = server.accept()
    print(addr)
    #2整个while循环实现，循环与当前连接进行通信。
    while 1:
        data = conn.recv(1024)#在Linux系统下如果client端连接直接被关了，不会报错，而是从当前client连接接收到的数据为None。
        if not data:break#当data中的数据为None时，直接就会跳出循环。
        print(".......", str(data, "utf8"))
        inp = input(">>>:")
        conn.send(bytes(inp,"utf8"))
server.close()