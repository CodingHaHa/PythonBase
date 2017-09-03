#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by fengL on 2017/9/3

#引入时间模块
import time

#1:时间：功能
# start = time.time()
# time.sleep(100)#线程在这里停止100秒
# print(start)

#目标函数
# def foo():
#     print("foo.....")


#2:需求：计算出函数执行的时间：
#实现如下：这样不行，不满足开闭原则。
# def foo():
#     start = time.time()
#     print("foo.....")
#     end = time.time()
#     print(end - start)

#一个开闭原则：对修改关闭，对扩展开放。


#3:这样可以满足计算时间的问题：但是有一个问题，别人如果要调用这个函数，都要重新添加这样的函数。
# def show_time(f):
#     start = time.time()
#     f()
#     end = time.time()
#     print(end - start)


#4:可以使用装饰器，来完成这个需求：
# def show_time(f):#show_time函数就是一个装饰器
#     def inner():
#         start = time.time()
#         f()
#         end = time.time()
#         print(end - start)
#     return  inner

#inner就是一个闭包。

#将foo函数名进行重写赋值
# foo = show_time(foo)
# foo()

#5:以上都是学习过程：仅供参考使用
######################python提供的实现==============
#1：目标函数：
def foo():
    print("foo.....")

#2:装饰器：
def show_time(f):#show_time函数就是一个装饰器
    def inner():
        start = time.time()
        f()
        end = time.time()
        print(end - start)
    return  inner

#3:实现函数名的再赋值
#实现函数名的覆盖
# foo = show_time(foo)

#python提供的装饰器：
@show_time#等价于foo = show_time(foo)、、、(格式：@将装饰器函数名，发到目标函数的定义上)
def foo():
    print("foo.....")

#调用
# foo()


# #6:======================功能函数添加参数：实现带参数的装饰器=======================
# #实现带参数的装饰器：#（参数）处的参数需要被统一
# #:装饰器：
# def show_time_bar(f):#show_time函数就是一个装饰器
#     def wrapper(*x,**y):#（参数）#添加参数
#         start = time.time()
#         f(*x,**y)#（参数）
#         end = time.time()
#         print(end - start)
#     return  wrapper
#
# @show_time_bar
# def add(*a,**b):#（参数）一#接收任意参数
#     sums = 0;
#     for x in a:
#         sums+=x
#     print(sums)
#     time.sleep(1)
#
# #调用
# add(1,2,2,8,9,5)



#7:装饰器函数加参数：添加某些其他的参数，例如，可以用于控制其他的效果
#为了给装饰器添加参数，再在装饰器外面，加一个装饰器
#思考：为何不能直接给装饰器添加需要的参数？以为@装饰器  => 目标函数名 = 装饰器函数    ； 这样就限定了装饰器函数只能有一个参数。
def logger(flag):
    def show_time(f):
        def inner(*x,**y):
            start = time.time()
            f(*x,**y)
            end = time.time()
            print(end - start)
            if flag == "log":
                print("打印日志信息。。。。")
        return inner
    return show_time

@logger(flag="log")#@show_time
def bar(*a,**b):
    print("bar")
    time.sleep(3)

bar(1,2,3)

