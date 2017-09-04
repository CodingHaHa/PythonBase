#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by fengL on 2017/9/4

#1：类和对象的基本使用:self就是指向具体的对象
# class Bar:
#     def foo(self,arg):
#         print(self,arg)
#
# z1 = Bar()
# print(z1)#直接打印对象地址：<__main__.Bar object at 0x0000000001E7D240>
# z1.foo(111)#self值为：<__main__.Bar object at 0x0000000001E7D240>
# #通过z1来调用foo方法时，self的值，就是z1对象的地址。即self执行调用方法的对象。


#2:给对象设置属性：给self设置属性
# class Bar:
#     def foo(self,arg):
#         print(self,self.name,self.age,arg)
# z = Bar()
# z.name = "feng"#给对象设置属性
# z.age = 34
# z.foo(666)
#
# z1 = Bar()
# z1.name = "lian"
# z1.age = "nan"
# z1.foo(444)
#
# #直接在外部访问对象的属性
# print(z.name)
# print(z1.age)

#3：既然self就表示对象，那么可以把2做如下修改
# class Bar:
#     def foo(self,content):
#         print(self.name,self.age,content)#注意这里的修改和2中进行对比
# obj = Bar()
# obj.name = "小米"
# obj.age = 110
# obj.foo("abc")#调用方法的时候就会自动把self（指代调用方法的具体对象实例）作为方法的第一个参数传入。


#4：面向对象三大特性之：封装(如果一个类里面有很多个方法，这些方法都会用到一些相同的参数)
# class Bar:
#     def add(self,content):
#         print(self.name,self.age,content)
#
#     def delete(self, content):
#         print(self.name, self.age, content)
#
#     def update(self, content):
#         print(self.name, self.age, content)
#
#     def get(self, content):
#         print(self.name, self.age, content)
#
# obj = Bar()
# #设置属性，（类似封装）
# obj.name = "熊明"
# obj.age = 10
#
# obj.add("add")
# obj.delete("delete")
# obj.update("update")
# obj.get("get")
#其实这里已经实现了封装，改进一下，使用构造方法。

#5：构造方法
class Bar:
    #构造方法，初始化公有的属性
    def __init__(self,name,age):
        print("init")
        #接收构造函数中的参数，并将参数值赋值给self指代的对象
        #如下，封装公有属性，每个对象都有这些公有的属性
        self.name = name
        self.age = age

    def add(self,content):
        print(self.name,self.age,content)

    def delete(self, content):
        print(self.name, self.age, content)

    def update(self, content):
        print(self.name, self.age, content)

    def get(self, content):
        print(self.name, self.age, content)
obj = Bar("feng",20)#这里的参数必须要和__init__()方法中的一样；这里会自动调用构造函数。
print(obj)

#注意：__init__方法对封装没有任何关系，只是我们强行使用它来进行数据的封装。
