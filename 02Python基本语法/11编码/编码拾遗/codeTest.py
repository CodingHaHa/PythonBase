#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by fengL on 2017/9/27



s = "hello封"#虽然看到的是一个个的字符，但是存在内存中是Unicode。
print(type(s))#<class 'str'>,记住一点，虽然数据类型是str，但是存放的是Unicode编码。

#把字符串转换为byte类型，为何要转换为byte类型
#因为byte类型是离计算机底层最近的（计算机只认识二进制）byte是十六进制。

#字符是我们人类认识的，字符是确定的。唯一的。
b = bytes(s,"utf8")#为何要添加utf8,为了编码为将字符编码为对应字符集的byte数据。
#从str>>>>>byte叫做编码。
print(b)#b'hello\xe5\xb0\x81'（utf8规则下的编码结果）
#为何hello没有被编码？
#   因为ASCII是Unicode的子集。
#为何汉字被编码了？
#   因为uft8的编码规定了汉字一般都占用三个字节。

#使用str的内置编码函数encode
sb = s.encode("gbk")
print(sb)#b'hello\xb7\xe2'(gbk规则下的编码结果)


#从bytes>>>>str叫做解码
#解码方式一：
ss = str(sb,"gbk")
# ss2 = str(sb,"utf8")
# ss3 = str(b,"gbk")
print(ss)
# print(ss2)#UnicodeDecodeError: 'utf-8' codec can't decode byte 0xb7 in position 5: invalid start byte
# print(ss3)#UnicodeDecodeError: 'utf-8' codec can't decode byte 0xb7 in position 5: invalid start byte

#解码时，必须按照编码是的字符串进行，否则就会出现乱码。

#解码方式二：
# ssb1 = sb.decode("utf8")
ssb2 = sb.decode("gbk")
# print(ssb1)
print(ssb2)
