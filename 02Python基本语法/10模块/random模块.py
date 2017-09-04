#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by fengL on 2017/9/4

import random

#1:返回0-1直接的随机数
print(random.random())

#2：返回一个范围内的随机整数
print(random.randint(1,8))#返回1-8包括8在内的随机整数

#3：返回一个随机字符
print(random.choice("hello"))
print(random.choice([1,2,8,9,5,3]))
print(random.choices(["hello",15,"abc",1010]))
print(random.sample(["hello",15,"abc",1010],2))#指定从序列中选指定数量的元素。
print(random.randrange(1,3))#取1-2的随机数，即不包含右边界
