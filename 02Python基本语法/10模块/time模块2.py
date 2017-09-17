#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by fengL on 2017/9/17

import time

# 1 time() :返回当前时间的时间戳
time.time()  # 1473525444.037215

# ----------------------------------------------------------

# 2 localtime([secs])
# 将一个时间戳转换为当前时区的struct_time。secs参数未提供，则以当前时间为准。
time.localtime()  # time.struct_time(tm_year=2016, tm_mon=9, tm_mday=11, tm_hour=0,
# tm_min=38, tm_sec=39, tm_wday=6, tm_yday=255, tm_isdst=0)
time.localtime(1473525444.037215)

# ----------------------------------------------------------

# 3 gmtime([secs]) 和localtime()方法类似，gmtime()方法是将一个时间戳转换为UTC时区（0时区）的struct_time。

# ----------------------------------------------------------

# 4 mktime(t) : 将一个struct_time转化为时间戳。
print(time.mktime(time.localtime()))  # 1473525749.0

# ----------------------------------------------------------

# 5 asctime([t]) : 把一个表示时间的元组或者struct_time表示为这种形式：'Sun Jun 20 23:21:05 1993'。
# 如果没有参数，将会将time.localtime()作为参数传入。
print(time.asctime())  # Sun Sep 11 00:43:43 2016

# ----------------------------------------------------------

# 6 ctime([secs]) : 把一个时间戳（按秒计算的浮点数）转化为time.asctime()的形式。如果参数未给或者为
# None的时候，将会默认time.time()为参数。它的作用相当于time.asctime(time.localtime(secs))。
print(time.ctime())  # Sun Sep 11 00:46:38 2016

print(time.ctime(time.time()))  # Sun Sep 11 00:46:38 2016

# 7 strftime(format[, t]) : 把一个代表时间的元组或者struct_time（如由time.localtime()和
# time.gmtime()返回）转化为格式化的时间字符串。如果t未指定，将传入time.localtime()。如果元组中任何一个
# 元素越界，ValueError的错误将会被抛出。
print(time.strftime("%Y-%m-%d %X", time.localtime()))  # 2016-09-11 00:49:56

# 8 time.strptime(string[, format])
# 把一个格式化时间字符串转化为struct_time。实际上它和strftime()是逆操作。
print(time.strptime('2011-05-05 16:37:06', '%Y-%m-%d %X'))

# time.struct_time(tm_year=2011, tm_mon=5, tm_mday=5, tm_hour=16, tm_min=37, tm_sec=6,
#  tm_wday=3, tm_yday=125, tm_isdst=-1)

# 在这个函数中，format默认为："%a %b %d %H:%M:%S %Y"。


# 9 sleep(secs)
# 线程推迟指定的时间运行，单位为秒。

# 10 clock()
# 这个需要注意，在不同的系统上含义不同。在UNIX系统上，它返回的是“进程时间”，它是用秒表示的浮点数（时间戳）。