import socket
server = socket.socket()
addr = ("127.0.0.1",8080)
server.bind(addr)
server.listen(5)
conn,addr = server.accept()
while 1:
    data = conn.recv(1024)#如果客户端直接发送一个（空数据，例如不发数据直接回车），这里就是阻塞，不会执行。
    print(".......",str(data,"utf8"))
    if not data:
        conn.close()
        conn,addr = server.accept()
        print(addr)
        continue
    inp = input(">>>:")
    conn.send(bytes(inp,"utf8"))

server.close()