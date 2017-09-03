#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by fengL on 2017/9/2


#1:给函数直接传入一个字典作为参数：
# def f(**kwargs):
#     print(kwargs)
#
# #定直接把一个dict作为参数传递给以函数时，要在字典前面加**
# f(**{"name":"feng","age":"10"})

#2:直接把一个list作为参数传递给一个函数：
# def f(*args):
#     print(args)
# #当直接把一个list作为参数传递给函数时，会把这个list作为元组的一个元素，这个元素是list
# f([1,2,3])#([1, 2, 3],)
# #当把一个list作为参数传递给函数时，在list前加一个*就会把list中的元素组合为一个元组
# f(*[1,2,3],)#(1, 2, 3)
