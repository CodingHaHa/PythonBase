#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by fengL on 2017/9/3


#1：迭代器使用：
# l = [1,2,3]
# iter(l)#等价于：l.__iter__()
#2:迭代器：list,tuple,dict,string:Iterable

#3：将可迭代对象变为迭代器：同调用python提供的iter()方法
# l = [1,2,3]
# print(type(l))
# it = iter(l)#该方法把一个可迭代对象转为迭代器。
# print(type(it))

#4：直接使用for来直接调用list的neixt方法会报错，所以它先会把list转换为迭代器。
# for i in [1,2,3]:
#     print(i, end='')#python3中print不换行:print(i,end='')

#5:isinstance函数用于判断一个对象是不是那个类型的实例
from collections import  Iterable,Iterator
l = [1,2,5,8]
d = iter(l)
print(d)
print(isinstance(l,list))
print(isinstance(d,Iterator))#判断是不是一个迭代器
print(isinstance(d,Iterable))#判断是不是一个可迭代对象


