import socket


client = socket.socket()
addr = ("127.0.0.1",8080)
conn = client.connect(addr)

while True:
    inp = input(">>>:")
    if inp == "exit":
        break
    #这里接收到的是传送的数据的大小
    client.send(bytes(inp,"utf8"))
    data_len = str(client.recv(1024),"utf8")
    print(data_len)
    #解决粘包，将两个send分开。
    client.send("ok")
    data = bytes()
    print(len(data))
    while len(data) != int(data_len) :
        recve = client.recv(1024)
        data+= recve
    # 这里有一个问题，若命令的执行结果内容很多，就会出现问题。
    # 这个问题是由于连接缓存只能接受固定大小的内容。若命令的内容超过了这个大小。就会接受不完。
    # 导致多次发送，其他命令的执行结果没有办法正常送回到client。
    print(str(data,"gbk"))
client.close()