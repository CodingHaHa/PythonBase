#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by fengL on 2017/9/3

#1:生成器：
# s = (x for x in range(10))#这样就会获得一个生成器，我们需要的值没有在一一的包含在生成器里面。
# print(s)#<generator object <genexpr> at 0x00000000021427D8>

#2：生成器和列表的区别
#列表是所有的菜：你想吃哪一个菜就可以直接吃那个菜。但是它所有的内容都在内存里面，占用内存。
#生成器是厨师：它并没有把所有的菜都给你一次性的做出来，而是一个菜都没有做出来，要等到你给他说你要吃第一菜时，它才会给你做一道菜。每次都要告诉他你要吃菜，它才给你做。所以不会占用内存。

#3：很大的一个list，会很占用内存空间
# s = [x for x in range(10000000000000000)]
# print(s)

#4：从生成器中获取值：从0开始的。
# s = (x for x in range(10))
# print(s.__next__())#可以使用我这样的方式来从生成器中获取值
# print(next(s))#推荐使用这样的方式来从生成器中获取值

#5:生成器就是一个迭代器对象,所以可以使用for来进行遍历
# s = (x for x in range(10))
# for i in s:
#     print(i)
#for对迭代器所做的事情：
#①：调用迭代器的next方法
#②：检测错误

#6：生成的两种创建方式：
#:①：(x for x in range(10))
#:②：yield关键字
#使用yield来创建生成器：
def foo():#这是一个函数，但是当加入了yield后，就变成了生成器了。
    print("ok")
    yield 1#这里只有一道菜。
    # return 1#yield不是return；但是每次调用neixt() 方法时，yield也会返回他后面的值。

    print("ok2")
    yield 2

    print("ok4")
    yield 9

g = foo()
print(g)#<generator object foo at 0x0000000001E02830>;这样调用foo()不会在执行函数里面的代码
print(next(g ))
print(next(g ))
print(next(g ))

#遍历生成器。
for i in foo():#for循环后面可以接，list、迭代器【他们统称为可迭代对象】
    print(i)

#什么是可迭代对象？看内部有没有__iter__()方法的。
