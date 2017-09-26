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
        try:#对下面的代码进行异常检测。
            data = conn.recv(1024)#
        except Exception:
            print("client连接中断了。。。。")
            break#当出现异常了，就直接跳出循环，继续接受下一个连接。从而实现不间断的通信。不会因为某个client端的链接中断就使得整个server挂掉。
        if not data:break
        print(".......", str(data, "utf8"))
        inp = input(">>>:")
        conn.send(bytes(inp,"utf8"))
server.close()