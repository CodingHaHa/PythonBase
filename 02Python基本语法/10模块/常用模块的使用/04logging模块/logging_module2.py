#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by fengL on 2017/9/17

# #1：logging对象，实现同时在文件和控制台打印日志。
# import logging
# logger = logging.getLogger()
# # 创建一个handler，用于写入日志文件
# fh = logging.FileHandler('test.log')
# # 再创建一个handler，用于输出到控制台
# ch = logging.StreamHandler()
#
# #设置日志格式化器
# formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
# fh.setFormatter(formatter)
# ch.setFormatter(formatter)
#
# #设置日志级别:注意要在记录日志之前进行设置
# # logger.setLevel(logging.DEBUG)
#
# #同时在文件和控制台中打印日志
# logger.addHandler(fh) #logger对象可以添加多个fh和ch对象
# logger.addHandler(ch)
#
# logger.debug('logger debug message')
# logger.info('logger info message')
# logger.warning('logger warning message')
# logger.error('logger error message')
# logger.critical('logger critical message')


#2：创建两个logger对象、
import logging
logger1 = logging.getLogger('mylogger')
logger1.setLevel(logging.DEBUG)

logger2 = logging.getLogger('mylogger')
logger2.setLevel(logging.INFO)

fh = logging.FileHandler('test.log')
ch = logging.StreamHandler()

logger1.addHandler(fh)
logger1.addHandler(ch)

logger2.addHandler(fh)
logger2.addHandler(ch)

logger1.debug('logger1 debug message')
logger1.info('logger1 info message')
logger1.warning('logger1 warning message')
logger1.error('logger1 error message')
logger1.critical('logger1 critical message')

logger2.debug('logger2 debug message')
logger2.info('logger2 info message')
logger2.warning('logger2 warning message')
logger2.error('logger2 error message')
logger2.critical('logger2 critical message')

# 这里有两个个问题：
#
#       <1>我们明明通过logger1.setLevel(logging.DEBUG)将logger1的日志级别设置为了DEBUG，为何显示的时候没有显示出DEBUG级别的日志信息，而是从INFO级别的日志开始显示呢？
#
#        原来logger1和logger2对应的是同一个Logger实例，只要logging.getLogger（name）中名称参数name相同则返回的Logger实例就是同一个，且仅有一个，也即name与Logger实例一一对应。在logger2实例中通过logger2.setLevel(logging.INFO)设置mylogger的日志级别为logging.INFO，所以最后logger1的输出遵从了后来设置的日志级别。
#
#       <2>为什么logger1、logger2对应的每个输出分别显示两次?
#        这是因为我们通过logger = logging.getLogger()显示的创建了root Logger，而logger1 = logging.getLogger('mylogger')创建了root Logger的孩子(root.)mylogger,logger2同样。而孩子,孙子，重孙……既会将消息分发给他的handler进行处理也会传递给所有的祖先Logger处理。
#         <3>Filter
#              限制只有满足过滤规则的日志才会输出。
#              比如我们定义了filter = logging.Filter('a.b.c'),并将这个Filter添加到了一个Handler上，则使用该Handler的Logger中只有名字带          a.b.c前缀的Logger才能输出其日志。
#                 filter = logging.Filter('mylogger')
#
#                 logger.addFilter(filter)
#
#                 这是只对logger这个对象进行筛选
#
#                 如果想对所有的对象进行筛选，则：
#
#                 filter = logging.Filter('mylogger')
#
#                 fh.addFilter(filter)
#
#                 ch.addFilter(filter)
#
#                 这样，所有添加fh或者ch的logger对象都会进行筛选。