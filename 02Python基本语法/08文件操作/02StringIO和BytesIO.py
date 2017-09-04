#1：StringOI的使用
# #从IO模块中导入StringIO
# from io import StringIO
# #创建StringIO对象
# f = StringIO()
# #调用相应的写方法
# f.write("hello")
# f.write(" ")
# f.write("world!")
# #调用getvalue()方法用于获取写入后的str
# print(f.getvalue())


#2：读取StringIO对象
# from io import StringIO
# f = StringIO("Hello\nHi\nPython")
# while True:
#     s = f.readline()
#     if s=="":
#         break
#     print(s.strip())


#3:BytesIO的使用：在内存中创建一个BytesIO，然后写入一些bytes
from io import BytesIO
f = BytesIO()
f.write("中文".encode("utf-8"))#写入的是经过UTF-8编码的bytes。
print(f.getvalue())
