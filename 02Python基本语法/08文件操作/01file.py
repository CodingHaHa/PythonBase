#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by fengL on 2017/9/2

#文件操作的流程：
#1：创建一个文件（打开一个文件）
# file = open("file","r",encoding="gbk")#创建一个文件
# #2：读取文件内容
# data = file.read()#读取所有的内容
# print(data)
# #3：关闭文件
# file.close()

#二：read方法：
# file = open("file","r",encoding="gbk")#
# d1 = file.read(1)#参数表示要读取多少个字符
# print(d1)
# # file.write("abc")#io.UnsupportedOperation: not writable:读的时候是不能写的

#三：写操作：在创建写模式的文件是就会把文件清空
# file = open("file","w",encoding="gbk")#w模式会对整个文件内容进行覆盖；在创建写模式的文件是就会把文件清空
# d1 = file.write("abc")#参数表示要读取多少个字符
# print(d1)
# # file.read(10)#io.UnsupportedOperation: not readable:写的时候不能读
# file = open("file2","w",encoding="gbk")#如果写的时候没有对应的文件，那么此时就会创建一个新的文件

#四：write的文件位置：
# file = open("file2","w",encoding="gbk")#创建文件是就会清空文件内容。
# file.write("hello world\n")
# file.write("fenglian")#hello worldfenglian；默认调用write方法不会自动换行。
# file.close()
#文件操作是内部会使用到指针，而我们不用去关心指针。文件句柄。


#五：文件的追加
# file = open("file2","a",encoding="gbk")
# # file.read()#io.UnsupportedOperation: not readable:不能读
# file.write("1254")#执行这个方法后，内容并没有直接存到磁盘文件上，而是在内存中。
# import  time
# time.sleep(50)
# print(file.fileno())#文件部署符
# file.close()#手动关闭文件，避免资源的占用，造成内存的浪费。每次都这么写实在太繁琐，所以，Python引入了with语句来自动帮我们调用close()方法：


#六：readline:读取一行。
# file = open("file","r",encoding="utf-8")
# data = file.readline()#第一行{readline:会把行末尾的换行符，也一起打印出来}
# print(data)
# data = file.readline()#第二行
# print(data)
#
# #readlines多行
# lines = file.readlines()#返回一个列表，每个元素都是一个行的字符串。
# print(lines)
# for x in lines:#for内部把lines对象封装为一个迭代器，用一个取一个。
#     print(x)


#七：读取文件时指针光标处理的方法:tell(打印光标位置),seek（设置光标位置）
# file = open("file","r",encoding="utf-8")
# print(file.tell())#显示指针的真实位置，tell方法会更加具体的内容来设置光标的值
# file.read(2)#读取两个中文字符，光标移动了6位（一个中文字符3个字节）
# print(file.tell())#读取文件后光标的位置发生了变化
# file.seek(0)#重新设置光标的位置。
# print(file.tell())
# #由于seek可以重写设置光标，所以可以在文件传输时，实现观点续传。

#八：flush操作
# file = open("file3","w",encoding="utf-8")
# file.write("ABC")
# file.flush()#刷新文件缓冲区，立马写回到磁盘文件中
# import  time
# time.sleep(10)

#九：sys模块获取控制台输入和输出
# import sys
# line = sys.stdin.readline()#控制台输入
# sys.stdout.write(line+"abc")
# sys.stdout.flush()

#十：with语句：自动关闭文件：这样我们就不用手动来关闭文件.。可以同时管理多个文件
with open("file0","r",encoding="utf-8") as f1,open("file1","r",encoding="utf-8") as f2:
    print(f1.read())
    print(f2.read())
