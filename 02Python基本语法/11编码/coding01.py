#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by fengL on 2017/9/15


#1:python2中的编码：str和Unicode
# s = "中国"
# print len(s)#6，打印为6，由于utf8导致的。（python2中len（）表示字节个数）
# print repr(s)#真实存放的是：'\xe4\xb8\xad\xe5\x9b\xbd'（字节）
# print type(s)#<type 'str'>，虽然存放的是字节，但是、
#
# #这里有一个问题：我们存的是中国的字节形式，但是打印出来确实“中国”两个字符。其实print方法内部为我们进行了一个转换，把字节转换为了字符
# print s#中国


# #改变为Unicode字符。
# s = u"中国"
# print len(s)#2，打印为2(字符个数)，由于utf8导致的。（python2中len（）表示字节个数）
# print repr(s)#真实存放的是：u'\u4e2d\u56fd'（Unicode）
# print type(s)#<type 'unicode'>，虽然存放的是字节，但是

#2python2中编码特点：
#byte+unicode不能直接进行拼接
#其实print内部进行了一个同一，将byte转换为了Unicode。（使其可以进行拼接）
# print "hello" +u"feng"
#python2，默认值为对ASCII范围中的字符的字节进行转换为Unicode，
# 对于非ASCII范围的字符他就不知道如何转换（解码）了。所以会报错。
# "中国"+u"成都"#UnicodeDecodeError: 'ascii' codec can't decode byte 0xe4 in position 0: ordinal not in range(128)

# print u"\u82d1"#苑


#3python3字符串编码的特点：
#python3严格区分开了byte和Unicode。
#byte是专门用于和计算机打交道，而Unicode是专门用于和用户打
# 交道
#这样的拼接在python3中是不被允许的。
#python3中b"字符串"就是转换为byte类型。
print(b"abc"+"feng")
