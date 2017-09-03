#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by fengL on 2017/9/2


#1:必须参数：调用函数时，传参数要和定义的顺序一致
# def print_info(name,age):
#     print("name=%s" % (name))
#     print("age=%s" % (age))
#
# print_info("feng",20)

#2:关键参数：调用函数时，通过名称来匹配对应的形参
# print_info(name="agc",age=15)

#3：默认参数：定义函数时指定参数的默认值：
# def print_person_info(name,age,sex="男"):
#     print("name=%s" % (name))
#     print("age=%s" % (age))
#     print("sex=%s" % (sex))
# #若函数有默认参数，那么调用函数时，不传该参数，就使用默认值
# print_person_info(name="dd",age="45")

#4：可变参数：
#①：对于没有名字的可变参数：*args（把参数放到一个元组中）
# def add(*args):
#     num = 0
#     for x in args:
#         num += x;
#     print(num)
# add(1,2,5,8,9)

#②：对于有名字的参数：k-v类型的参数：**args（把参数放到一个dict中）
# def print_person_info(*args,**kwargs):#这样就可以接收全部的参数了
#     print(args)
#     print(kwargs)
#     for i in kwargs:
#         print("%s:%s" %(i,kwargs[i]))

# print_person_info(1,5,"abc",name="feng",age = 78)#注意：顺序问题

#list参数也是被*args接收到的
# print_person_info(1,5,[4,8,9],"abc",name="feng",age = 78)

#:③：关于不定长参数的位置：*args和**kwargs（放在最后）的位置：*args必须在*kwargs前面。
    #关键字参数放到最开始。
    #如果有默认参数放到左边。


