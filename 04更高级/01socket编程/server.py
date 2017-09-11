import socketserver,socket

#1:创建socket对象；使用默认参数创建socket对象。
sk = socket.socket()
print(sk)
#2:绑定ip和端口
address = ("127.0.0.1",8088)
sk.bind(address)#参数必须是元组
#3:让服务器监听端口，等待客户端链接。
sk.listen(3)#参数3指定允许排队的个数
#4:接受客户端链接
print("waiting for client.......")
conn,addr = sk.accept()#接受client端请求；conn，是客户端的socket对象。
# # print(conn)
# inp = input(">>>")
# # conn.send(inp)#python2中可以使用str类型
# conn.send(bytes(inp,"utf8"))#Python3中接收数据都需是byte类型

#接收数据：使用链接[conn]来获取数据;
#server段的conn对象其实就是client的socket对象。
data = conn.recv(1024)
print(str(data,"utf8"))




#区别close方法：
# conn.close()#不和某个确定的client继续通信了。
# sk.close()#不在接受任何链接请求



