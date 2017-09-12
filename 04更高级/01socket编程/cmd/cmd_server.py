import socket
server = socket.socket()
addr = ("127.0.0.1",8080)
server.bind(addr)
server.listen(5)
print("waiting........")

while 1:
    conn, addr = server.accept()
    print(addr)
    while 1:
        try:
            data = conn.recv(1024)#
        except Exception:
            break
        if not data:
            print(".......", str(data, "utf8"))
            inp = input(">>>:")
            conn.send(bytes(inp,"utf8"))
server.close()