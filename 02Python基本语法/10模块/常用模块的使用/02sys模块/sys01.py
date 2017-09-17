#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by fengL on 2017/9/17

import sys

#1:命令行参数List，第一个元素是程序本身路径
# print(sys.argv)#可以到cmd下去实现具体的效果。

#2:退出程序，正常退出时exit(0)
# sys.exit(0)

#3:获取Python解释程序的版本信息
# print(sys.version)#3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:57:36) [MSC v.1900 64 bit (AMD64)]

#4:最大的Int值
# print(sys.maxint)

# #5：返回模块的搜索路径，初始化时使用PYTHONPATH环境变量的值
# print(sys.path)
# sys.path.append("abc")#添加搜索路径到PYTHONPATH
# print(sys.path)
#
# #6:返回操作系统平台名称
# print(sys.platform)#win32
# #7:输出的控制台：
# sys.stdout.write('please:')
#
# #7：从控制台获取输入：
# val = sys.stdin.readline()[:-1]
# print(val)