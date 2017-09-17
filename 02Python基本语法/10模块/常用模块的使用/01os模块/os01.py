#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by fengL on 2017/9/17

import os
#1:获取当前工作目录
# print(os.getcwd())#H:\MyLearnNotes\Python\PythonBase\02Python基本语法\10模块\常用模块的使用\01os模块

#2：改变当前脚本工作目录；相当于shell下cd
# os.chdir("d://")
# print(os.getcwd())

#3:返回当前目录: ('.')
# print(os.curdir  )

#4：获取当前目录的父目录字符串名：('..')
# print(os.pardir)

#5:可生成多层递归目录
# os.makedirs('dirname1/dirname2')

#6:若目录为空，则删除，并递归到上一级目录，如若也为空，则删除，依此类推
# os.removedirs('dirname1/dirname2')

#7:生成单级目录；相当于shell中mkdir dirname
# os.mkdir('dirname')

#8:删除单级空目录，若目录不为空则无法删除，报错；相当于shell中rmdir dirname
# os.rmdir('dirname')

#9:列出指定目录下的所有文件和子目录，包括隐藏文件，并以列表方式打印
# print(os.listdir(r'H:\\MyLearnNotes\\Python\\PythonBase\\02Python基本语法\\10模块'))

#10:删除一个文件(只能删除文件，不能删除文件夹)
# os.remove(文件名)

#11:重命名文件/目录
# os.rename("dirname","dirname12")

#12:获取文件/目录信息
# print(os.stat(r'H:\MyLearnNotes\Python\PythonBase\02Python基本语法\10模块\常用模块的使用\01os模块'))

#13:输出操作系统特定的路径分隔符，win下为"\\",Linux下为"/"
# print(os.sep)

#14:输出当前平台使用的行终止符，win下为"\t\n",Linux下为"\n"
# print(os.linesep)

#15:输出用于分割文件路径的字符串
# print(os.pathsep)#;

#16:输出字符串指示当前使用平台。win->'nt'; Linux->'posix'
# print(os.name )#nt

#17：运行shell命令，直接显示
# print(os.system("bash command"))

#18：获取系统环境变量
# print(os.environ  )

#19:返回path规范化的绝对路径
# print(os.path.abspath("."))

#20:将path分割成目录和文件名二元组返回
# print(os.path.split(r'H:\MyLearnNotes\Python\PythonBase\02Python基本语法\10模块\常用模块的使用\01os模块'))

#21:返回path的目录。其实就是os.path.split(path)的第一个元素
# print(os.path.dirname(r'H:\MyLearnNotes\Python\PythonBase\02Python基本语法\10模块\常用模块的使用\01os模块'))
#返回path最后的文件名。如何path以／或\结尾，那么就会返回空值。即os.path.split(path)的第二个元素
# print(os.path.basename(r'H:\MyLearnNotes\Python\PythonBase\02Python基本语法\10模块\常用模块的使用\01os模块'))#01os模块

#22:如果path存在，返回True；如果path不存在，返回False
# print(os.path.exists("a")  )

#23：如果path是绝对路径，返回True
# print(os.path.isabs("a"))

#24:如果path是一个存在的文件，返回True。否则返回False
# print(os.path.isfile(r'H:\MyLearnNotes\Python\PythonBase\02Python基本语法\10模块\常用模块的使用\01os模块\os01.py'))

#25:如果path是一个存在的目录，则返回True。否则返回False
# print(os.path.isdir(r'H:\MyLearnNotes\Python\PythonBase\02Python基本语法\10模块\常用模块的使用\01os模块'))

#26:将多个路径组合后返回，第一个绝对路径之前的参数将被忽略
# os.path.join(path1[, path2[, ...]])

#27:返回path所指向的文件或者目录的最后存取时间
# print(os.path.getatime(r'H:\MyLearnNotes\Python\PythonBase\02Python基本语法\10模块\常用模块的使用\01os模块'))

#28:返回path所指向的文件或者目录的最后修改时间
# print(os.path.getmtime(r'H:\MyLearnNotes\Python\PythonBase\02Python基本语法\10模块\常用模块的使用\01os模块'))