#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by fengL on 2017/9/5

#1:继承
# class F:
#     def f1(self):
#         print("f1")
#
#     def f2(self):
#         print("f2")
#
# class S(F):#继承
#     def s1(self):
#         print("s1")
#
#     def s2(self):
#         print("s2")
#
# s = S();
# s.s1()
# s.f1()#继承父类后，可以获得父类的f1()方法。

#2：方法覆盖，实现自己的逻辑，而不直接使用父类的逻辑。
class F:
    def f1(self):
        print("f1")

    def f2(self):
        print("f2")

class S(F):#继承
    def s1(self):
        print("s1")

    def s2(self):
        print("s2")

    #实现覆盖，即不继承父类逻辑，而是使用自己的逻辑
    def f2(self):
        # super(S,self).f2()#子类中执行父类的方法：方法一：;S大写（类名），格式：super(子类名,self).父类方法()
        print("S-f2")
        # F.f2(self)#子类中执行父类方法：方法二

s = S();
#self:永远指调用方法的调用者。
s.s1()#s1()中的self是形参，此时self代指s对象。
s.f1()#此时s执行f1()方法，此时f1()中的self是形参，此时self代指s对象。
s.f2()#会执行子类自己的逻辑，而不会去执行父类的相应逻辑。