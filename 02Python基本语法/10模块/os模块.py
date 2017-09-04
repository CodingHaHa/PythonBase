#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by fengL on 2017/9/4

import os
#改变当前脚本工作目录，相当于shell下的cd
path = "H:\MyLearnNotes\Python\PythonBase"
os.chdir(path)
#回到当前目录
print(os.curdir)

#上一级目录
print(os.pardir)

# os模块的常用功能：
print(os.name)#显示当前使用的平台

print(os.getcwd())#显示当前python脚本工作路径

print(os.listdir(path))#返回指定目录下的所有文件和目录名

# print(os.remove(path))#删除一个文件

# print(os.makedirs(path))#可生成多层递规目录

# print(os.rmdir(path))#删除单级目录

# print(os.rename("oldname","newname"))#重命名文件

print(os.system("echo 'hello'"))#运行shell命令,注意：这里是打开一个新的shell，运行命令，当命令结束后，关闭shell

print(os.sep)#显示当前平台下路径分隔符

print(os.linesep)#给出当前平台使用的行终止符

print(os.environ)#获取系统环境变量

print(os.path.abspath(path))#显示当前绝对路径

print(os.path.dirname(path))#返回该路径的父目录

print(os.path.basename(path))#返回该路径的最后一个目录或者文件,如果path以／或\结尾，那么就会返回空值。

print(os.path.isfile(path))#如果path是一个文件，则返回True

print(os.path.isdir(path))#如果path是一个目录，则返回True

print(os.stat(path))#获取文件或者目录信息

print(os.path.split(path))#将path分割成路径名和文件名。（事实上，如果你完全使用目录，它也会将最后一个目录作为文件名而分离，同时它不会判断文件或目录是否存在）

print(os.path.join(path,"appendDirName"))#连接目录与文件名或目录 结果为path/appendDirName

print(os.removedirs("待删除的目录"))#删除文件夹，只能山地车空文件


