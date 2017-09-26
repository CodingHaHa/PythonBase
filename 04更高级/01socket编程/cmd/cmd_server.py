import socket
import subprocess

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
        if not data:break
        print(".......", str(data, "utf8"))
        #接收到的数据是一个byte类型，所以需要通过str()的方式进行转换。
        #执行的命令是一个str类型。
        obj = subprocess.Popen(str(data,"utf8"),shell=True,stdout=subprocess.PIPE)
        result = obj.stdout.read()
        #由于发生的数据必须是一个byte类型，所以不用进行str转换。直接发送就可以了。
        #int和byte不能直接进行类型转换。需要通过中间的str帮助。
        result_len = bytes(str(len(result)),"utf8")

        conn.sendall(result_len)#注意：需要把长度从int->str->byte(因为只能传送byte类型的数据)

        #粘包现象。这里的两个发送会在一次进行。
        #这样的情况是时不时的出现的。
        #可以使用time.sleep()实现但是太low了。你加长了浪费CPU，短了不够用。
        # import time
        # time.sleep(1)

        #高大上的方法（简单方法）
        conn.recv(1024)#

        conn.sendall(result)




server.close()