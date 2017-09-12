import socket


client = socket.socket()
addr = ("127.0.0.1",8080)
conn = client.connect(addr)

while True:
    inp = input(">>>:")
    if inp == "exit":
        break
    client.send(bytes(inp,"utf8"))
    data = client.recv(1024)
    print(str(data,"utf8"))
client.close()