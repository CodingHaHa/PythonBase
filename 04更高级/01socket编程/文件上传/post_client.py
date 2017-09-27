import socket
import os

client = socket.socket()
addr = ("127.0.0.1",8080)
conn = client.connect(addr)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

while True:
    inp = input(">>>:")#post|11.png
    cmd,path = inp.split("|")
    path = os.path.join(BASE_DIR,path)

    filename = os.path.basename(path)#获取文件名，给服务器的文件名。
    file_size = os.stat(path).st_size#文件状态，大小。

    #发送给服务器端的命令。
    file_info = "post|%s|%s"%(filename,file_size)
    client.sendall(bytes(file_info,"utf8"))

    with open(path,"rb") as f:
        has_send = 0
        while has_send != file_size:
            data = f.read(1024)
            client.sendall(data)
            has_send += len(data)
    print("client send over")
client.close()