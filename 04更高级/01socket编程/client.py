import  socket
#1:创建socket对象
sk = socket.socket()
#2：链接服务器端（通过设置服务器的ip和端口）
address = ("127.0.0.1",8088)
conn = sk.connect(address)

#接收数据
# data = sk.recv(1024)
# # print(data)#打印的是字节数据（对于中文我们就看不到内容）
# print(str(data,"utf-8"))#要看到中文，需要进行编码


#发送数据
sk.send(bytes("client send data","utf8"))#数据为byte