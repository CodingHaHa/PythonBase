#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by fengL on 2017/8/31

#1：对于可变对象，比如list，对list进行操作，list内部的内容是会变化的，比如：
a = ['c', 'b', 'a']
a.sort()
print(a)


#2:对于不可变对象，比如str，对str进行操作呢：
a = 'abc'
b =  a.replace('a', 'A')
print(a)
print(b)

#对于不变对象来说，调用对象自身的任意方法，也不会改变该对象自身的内容。相反，这些方法会创建新的对象并返回，这样，就保证了不可变对象本身永远是不可变的。
