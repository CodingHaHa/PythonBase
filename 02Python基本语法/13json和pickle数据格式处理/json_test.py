#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by fengL on 2017/9/17
import json
# #1：通过eval函数来将一个字符串转换为python对象
# x = "['a','true','false',1]"
# print(eval(x))
# #注意：eval方法是有局限性的，对于普通的数据类型，json.loads和eval都能用，但遇到特殊类型的时候，eval就不管用了,所以eval的重点还是通常用来执行一个字符串表达式，并返回表达式的值。

#2:json 的使用
#
#
# dic = {'name': 'alvin', 'age': 23, 'sex': 'male'}
# print(type(dic))  # <class 'dict'>
#
# #序列化
# j = json.dumps(dic)
# print(type(j))  # <class 'str'>
#
# f = open('序列化对象', 'w')
# f.write(j)  # -------------------等价于json.dump(dic,f)
# f.close()
#
# #反序列化
# f = open('序列化对象')
# data = json.loads(f.read())  # 等价于data=json.load(f)
# print(data)


#------------------dump-------load-----------------------
dic = {'name': 'alvin', 'age': 23, 'sex': 'male'}
f = open('序列化对象2', 'w')
data = json.dump(dic,f)

f = open('序列化对象2', 'r')
data = json.load(f)
print(data)