#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by fengL on 2017/9/2

#1:高阶函数的使用：
#被传入的函数定义
# def func(n):
#     return n*n
#
# def foo(a,b,f):
#     return f(a)+f(b)
#
# print(foo(10,20,func))


#2:函数可以作为函数参数也可以作为函数的返回值。
#一般的值作为函数的返回值。
# def foo():
#     x = 5
#     return x
#
# print(foo())

#函数作为函数的返回值
# def foo():
#     def inner():
#         print("I'm inner")
#     return inner#返回一个函数时，不能加()
# ret = foo()#返回的是一个函数
# print(ret)#返回值是一个函数对象的内存地址


