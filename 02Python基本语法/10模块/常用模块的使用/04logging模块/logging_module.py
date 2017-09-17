#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by fengL on 2017/9/17

import logging
# #1：logging的简单使用
# #不同的日志级别：
# logging.debug('debug message')
# logging.info('info message')
# #python的默认日志级别是WARNING，所以可以打印WARNING及其以下级别的日志。
# logging.warning('warning message')
# logging.error('error message')
# logging.critical('critical message')

# #2：设置日志的输出格式以及输出日志到文件中
# logging.basicConfig(level=logging.DEBUG,
#                     format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
#                     datefmt='%a, %d %b %Y %H:%M:%S',
#                     #filename='test.log',#注释后，就会使用默认的方式打印到控制台
#                     #filemode='w')
#
# logging.debug('debug message')
# logging.info('info message')
# logging.warning('warning message')
# logging.error('error message')
# logging.critical('critical message')

#注意：从这个输出可以看出logger = logging.getLogger()返回的Logger名为root。这里没有用logger.setLevel(logging.Debug)显示的为logger设置日志级别，所以使用默认的日志级别WARNIING，故结果只输出了大于等于WARNIING级别的信息。
