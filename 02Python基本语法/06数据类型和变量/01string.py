#1:字符串的基本操作：
# print("你好Python")#python3默认的编码为Unicode，所以默认是支持中文的。

#2：字符-和字符编码
# print(ord('A'))#获取字符的整数表示
# print(chr(66))#编码转换为对应的字符

#3:字符串和字节互换
print('ABC'.encode('ascii'))#以Unicode表示的str通过encode()方法可以编码为指定的bytes(b'ABC')
print(b'ABC'.decode('ascii'))#如果我们从网络或磁盘上读取了字节流，那么读到的数据就是bytes。要把bytes变为str，就需要用decode()方法：


#4：获取字符数
print (len("你好"))#如果是字符，则获取字符个数
print (len("你好".encode("utf-8")))#如果是字节，则获取字节个数


#5:格式化字符串
