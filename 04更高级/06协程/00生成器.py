#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by fengL on 2017/9/16

#1:没有使用生成器的函数
# def f():
#     print ("ok1")
#
# #调用没有使用生成器的函数，会直接执行函数体
# f()#ok1

# #2：使用了生成器的函数(或者生成器的返回值)
# def f():
#     print ("ok1")
#     yield 5
#     print ("ok2")
#     yield 60
#
# #调用使用了生成器的函数，并不会执行函数体内容。
# f()
# #调用使用了生成器的函数，只是为我们返回了一个生成器。
# print(f())#<generator object f at 0x0000000001DEC888>
#
# #如果确实要执行生成器函数的函数体
# gen = f()
# #通过next()方法来执行
# print(next(gen))#每执行一个next(生成器)，就会执行到一个yield暂停。
# print(next(gen))#执行第二个next(生成器)，就会从上一个yield后的代码开始执行，直到下一个yield

#3：使用了生成器的函数(给生成器设置值)
def f():
    print ("ok1")
    count = yield 5
    print(count)
    print ("ok2")
    yield 60

gen = f()

#send可以第一次执行，但是第一次执行时就不要传递值了（gen.send(None)），效果等同于next(gen)
# x = gen.send(10)#TypeError: can't send non-None value to a just-started generator
x = gen.send(None)
print(x)

print(next(gen))#每执行一个next(生成器)，就会执行到一个yield暂停。
#调用生成器的send方法给生成器传递值，值传递给第一个yield前面的变量
# 生成器的调用send+next次数只和和yield个数相同。
# x = gen.send(10)#调用后会返回下一个yield的返回值。

print(x)#60