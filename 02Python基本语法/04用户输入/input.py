#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by fengL on 2017/8/30

#用户输入：
name = input("your name:")
age = input("your age:")
print (age,name)

#一个小程序：
print("you can buy:",name,age,"ddd")

#数字转换为字符串：
#str:字符串
#int:整数
print(str(20))

#input函数接收到的所有内容都是字符串，即使是数字也会被当做字符串处理。
num1 = input("num1:")
num2 = input("num2:")
#print (num1 -num2)#TypeError: unsupported operand type(s) for -: 'str' and 'str'
#先转换为数字，再进行加减处理。
#把数字转换为字符串：str(20)
#把字符串转换为数字：int("20")
print ("abc",int(num1) -int(num2),"def")
# print ("abc"+int(num1) -int(num2)+"def")#报错，字符串和数字不能进行拼接。

age_of_your = 20
guess_age = int(input(">>:"))
if guess_age == age_of_your:
    print("yes")
else:
    print("no")