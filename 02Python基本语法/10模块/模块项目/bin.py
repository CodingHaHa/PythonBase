#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by fengL on 2017/9/16

# #1:导入我们自定义的模块
# import calculate #（这里报错只是IDE的问题，其实是可以成功的）
# #2:执行模块中的函数
# print(calculate.add(1,2))

# #3:查看python解释器，搜索模块的路径
# import sys
# print(sys.path)#['H:\\MyLearnNotes\\Python\\PythonBase\\02Python基本语法\\10模块\\模块项目', 'H:\\MyLearnNotes\\Python\\PythonBase', 'D:\\SoftWare\\LearnSoftWare\\Python3.6\\python36.zip', 'D:\\SoftWare\\LearnSoftWare\\Python3.6\\DLLs', 'D:\\SoftWare\\LearnSoftWare\\Python3.6\\lib', 'D:\\SoftWare\\LearnSoftWare\\Python3.6', 'D:\\SoftWare\\LearnSoftWare\\Python3.6\\lib\\site-packages']


# #4：只导入模块中的某个部分
# from calculate import add
# print(add(1,5))

# #5：导入整个模看的另一个方式。
# from calculate import *
# # print(add(1,5))

# #6：修改导入函数的名称：
# from calculate import add as plus
# print(plus(1,5))
# #无法再继续使用老名称进行调用了。
# # print(add(1,5))----错

# #7:调用某个包里面的方法
# # import web.logger #不能在使用这样的方式，来导入包下面的模块了。----错
# #而要使用如下的方式导入包下面的模块。
# from web import logger
# logger.logger()

# #8：如果多层包结构，有如何导入多层包下的模块呢？
# #这样的方式
# from  web.web2 import logger2
# logger2.logger2()

# :9：只导入某个包下面的模块中的一个方法
# #这样的方式是不行的。
# # import web.web2.logger2----错
# #如下的导入方式是可以的。
# from  web.web2.logger2 import logger2
# logger2()

#10：import web #执行了_init_文件
import web #执行了_init_文件
#打印了ok（代码见_init_.py文件）
