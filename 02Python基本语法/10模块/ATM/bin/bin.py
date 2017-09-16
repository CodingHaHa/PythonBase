#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by fengL on 2017/9/17

#1:解决方式一：直接写死环境path，问题：无法移植。
import sys
sys.path.append("H:\\MyLearnNotes\\Python\\PythonBase\\02Python基本语法\\10模块\ATM")
print(sys.path)

from module import main
main.main()

#__file__:当前执行文件的相对路径
print(__file__)
#通过一个相对路径，修改为绝对路径。
import os
print(os.path.abspath(__file__))
print(os.path.dirname(os.path.abspath(__file__)))
print(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
#获取基本路径：（这个是非常重要的）
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(BASE_DIR)
#将基路径放到path下：让包收索成功了。
sys.path.append(BASE_DIR)