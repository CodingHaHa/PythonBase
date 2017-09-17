#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by fengL on 2017/9/17

import shelve

# #1：序列化：shelve只有一个open()方法：
# f = shelve.open(r'shelve.txt')
# #添加多个数据到shelve
# f['stu1_info']={'name':'alex','age':'18'}
# f['stu2_info']={'name':'alvin','age':'20'}
# f['school_info']={'website':'oldboyedu.com','city':'beijing'}
# f.close()

#2:反序列化
# f = shelve.open(r'shelve.txt')
# print(f.get('stu1_info')["age"])