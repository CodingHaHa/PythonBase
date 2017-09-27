import socket
import os

server = socket.socket()
addr = ("127.0.0.1",8080)
server.bind(addr)
server.listen(5)
print("waiting........")

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

while 1:
    conn, addr = server.accept()
    print(addr)
    while 1:
        data = conn.recv(1024)
        cmd,filenaem,filesize = str(data,"utf8").split("|")
        path = os.path.join(BASE_DIR,"yuan",filenaem)
        filesize = int(filesize)

        f = open(path,"ab")
        has_receive = 0
        while has_receive != filesize:
            #循环接收
            data = conn.recv(1024)
            f.write(data)
            has_receive += len(data)

        f.close()
server.close()