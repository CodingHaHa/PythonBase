#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by fengL on 2017/9/27
import socketserver

#自定义一个server 为了使用socketserver，必须要继承BaseRequestHandler
class MyServer(socketserver.BaseRequestHandler):

    #方法名必须为handle，为了重写父类的方法。
    #handle是父类的一个方法。
    def handle(self):
        print ("服务端启动...")
        while True:
            conn = self.request#获取连接。这里只是一个变量重命名。
            print (self.client_address)
            while True:

                client_data=conn.recv(1024)

                print (str(client_data,"utf8"))
                print ("waiting...")
                server_response=input(">>>")
                conn.sendall(bytes(server_response,"utf8"))
                # conn.sendall(client_data)

            conn.close()
            # print self.request,self.client_address,self.server


if __name__ == '__main__':
    #这里使用ThreadingTCPServer来使用并发（多线程）的server
    server = socketserver.ThreadingTCPServer(('127.0.0.1',8098),MyServer)#可以实现并发
    # server = socketserver.TCPServer(('127.0.0.1',8098),MyServer)#不可以实现并发
    #启动服务器。
    server.serve_forever()


