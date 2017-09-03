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

#
s = (x for x in range(10))
print(s.__next__())
print(s.__next__())
print(s.__next__())

