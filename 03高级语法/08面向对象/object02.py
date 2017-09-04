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

#2：覆盖，实现自己的逻辑，而不直接使用父类的逻辑。
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
        print("S-f2")

s = S();
s.s1()
s.f2()#会执行子类自己的逻辑，而不会去执行父类的相应逻辑。