#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by fengL on 2017/9/3

"""
闭包定义：
    如果在一个内部函数里，对在外部作用域（但不是全局作用域）的变量进行引用，那么内部函数就被认为是闭包(closure)
"""
def outer():
    x = 10#这里是写死的，也可以把x作为参数传入进来。
    def inner():
        print(x)
    return inner

#外部函数的入参：内部函数，可以引用，外部函数的入参。
def outer2(x):
    def inner():
        print(x)
    return inner

#inner函数就是闭包：说明它是一个内部函数，它引用了外部函数outer的x变量（outer的作用域，而不是全部作用域）
outer()()
outer2(20)()
#一般按照常理：当outer函数执行完毕后，它内部的变量都会被作为垃圾回收。
#但是它执行完毕后，返回的inner函数，内部引用了outer中的x变量，x变量并没有作为垃圾被回收。
#闭包可以脱离，它原本所在的外部作用域，来引用，外部作用域的变量。

#关于闭包：
#   闭包就是，内部函数块+定义函数时的环境。