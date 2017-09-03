#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by fengL on 2017/9/2

#1：abs:取绝对值
#2：all(iterable):如果哟一个元素不再迭代器里面返回FALSE
#3：dict():创建一个字典
#4：eval():计算字符串表达式的值：eval("1+2+8")

#5:filter()：对序列进行一个筛选
# str = [1,2,5,8,9]
# def func(s):
#     if s != 8:
#         return s
# ret = filter(func,str)#返回的结果是一个元组
# print(list(ret))#list方法将一个元组转为list（list就是一个迭代器）


#6：map():对传入的每个参数进行处理，然后返回每个参数
# str = [1,2,5,8,9]
# def func(s):
#         return 1+s
# ret = map(func,str)#返回的结果是一个元组
# print(ret)
# print(list(ret))#list方法将一个元组转为list（list就是一个迭代器）

#注意filter和map区别：filter会过滤值，不会修改值，但是map不会过滤值会修改值。

#7:reduce:需要引入reduce模块
# from functools import reduce
# def add(x,y):
#     return x+y
# print(reduce(add,range(1,101)))#(1+2+..+101),每次取前两个求和，把和放到第一个个位置，再继续进行求和。

#8：lambda函数：lambda x,y:x*y
# def add(a,b):
#     return a+b
#匿名函数
add = lambda a,b:a+b
print(add(2,3))

