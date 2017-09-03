#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by fengL on 2017/9/2

# if True:
#     x = 3
# print(x)
#
# def f():
#     a = 10
# f()
# # print(a)

# LEGB:
#L:local,局部作用域，即函数中定义的变量
#E:enclosing,嵌套的父级函数的局部作用域，即包含此函数的上级函数的局部作用域，但不是全局的。
#G:globa,全局变量，就是模块级别定义的变量
#B:built-in,系统固定模块里面的变量，比如，int
#搜索变量的优先级顺序依次是：局部作用域>外层作用域>当前模块的全局>python内置作用域
# x = int(2.9)#int built-in
# g_count = 0 #global
# def outer():
#     o_out = 1
#     def inner():
#         i_count = 2
#         print(i_count)
#     # print(i_count)#找不到
#     inner()
#
# outer()


#变量的修改：
x = 6
def f():
    print(x)#UnboundLocalError: local variable 'x' referenced before assignment
    x = 5
f()
#错误原因：print(x)时，解释器会在局部作用域中，查找，会找x = 5(函数已经加载)
#