#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by fengL on 2017/8/31


#1：元组基本使用：
classmates = ('Michael', 'Bob', 'Tracy')#classmates的值就不能改变了。
#它也没有append()，insert()这样的方法。其他获取元素的方法和list是一样的，你可以正常地使用classmates[0]，classmates[-1]，但不能赋值成另外的元素。

#2：不可变：不可变的tuple有什么意义？因为tuple不可变，所以代码更安全。如果可能，能用tuple代替list就尽量用tuple。

#3：tuple的陷阱：当你定义一个tuple时，在定义的时候，tuple的元素就必须被确定下来
t = (1,2)
print(t)

#4:如果要定义一个空的tuple，可以写成()：
t = ()
print(t)

#5:如果要定义有一个元素的tuple使用(1,)，而不能使用（1），它会被认为是1这个数，
t = (1,)
print(t)

#6：tuple不可变的理解：
t = ('a', 'b', ['A', 'B'])
t[2][0] = 'X'
t[2][1] = 'Y'
print(t)
#这里确实发生了变化，why?不是说tuple不可变么？
#其实不可变，说的是tuple的每个元素，指向永远不变。
#但是如果tuple中的元素本身就是可变的，例如list，那么list中的元素是可变的，而tuple的指向并没有变化。

#7:元组不可以被修改
a = (1,2,3)
print(a[1])
a[1]=5#TypeError: 'tuple' object does not support item assignment,元组不能被修改
print(a)