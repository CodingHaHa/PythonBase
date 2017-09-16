#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by fengL on 2017/9/16


# s = "中国"
# print(type(s))#<class 'str'>,虽然打印的是<class 'str'>，但是实际存放的是Unicode。
# #编码：变为byte类型。
# b1 = s.encode("utf8")
# print(b1,type(b1))
# #解码:变为Unicode
# print(b1.decode("utf8"))#b1.decode("utf8") ==  u"\u82d1",打印时会把Unicode编码转换为对应的字符。
# # print(b1.decode("gbk"))#UnicodeDecodeError: 'gbk' codec can't decode byte 0xad in position 2: illegal multibyte sequence，3.6中报错


# s = "中国"
# b2 = s.encode("gbk")
# print(b2,type(b2))
# print(b2.decode("gbk"))
# # print(b2.decode("utf-8"))


#第二种编码解码方式：
s = "中国"
b = bytes(s,"utf8")#获取字节
print(b)
ss = str(b,"utf8")
print(ss)