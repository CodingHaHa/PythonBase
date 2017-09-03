#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by fengL on 2017/9/3

#1:列表生成式
a = [x for x in range(10)]#使用空格分割
print(a)

#2:对每个元素进行操作，然后在放入到列表中。
a = [x*2 for x in range(10)]
print(a)

#3:使用函数来查找列表生成式
#定义函数
def f(n):
    return n**3

a = [f(x) for x in range(10)]
print(a)
