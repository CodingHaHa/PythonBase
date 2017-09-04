import time

#1:使用help函数用于查看相应的帮助文档
# print(help(time))

#2：获取时间戳:time.time() ====*****
# print(time.time())

#3:计算cpu执行的时间：time.clock()
# time.sleep(3)#cpu在这3秒的时间内没有工作。
# print(time.clock())

#4：cpu休息time.sleep(3)：====****，这个经常被用到。


#5：gmtime()：结构化时间 和我们国加的北京时间差8个小时。
# print(time.gmtime())#time.struct_time(tm_year=2017, tm_mon=9, tm_mday=4, tm_hour=11, tm_min=13, tm_sec=31, tm_wday=0, tm_yday=247, tm_isdst=0)
# #UTC:

#6：本地时间
# print(time.localtime())

#7:格式化时间
# struct_time = time.localtime()#本地时间
# pattern = "%Y-%m-%d %H:%M:%S"
# str_time = time.strftime(pattern,struct_time)##把一个元组时间转换为字符串时间
# print(str_time)
# tuple_time = time.strptime(str_time,pattern)#把一个字符串时间转换为元组时间
# print(tuple_time)
#
# #获取每个时间字段的值：
# print(tuple_time.tm_year)#年
# print(tuple_time.tm_mon)#月
# print(tuple_time.tm_mday)#日
# print(tuple_time.tm_hour)#时
# print(tuple_time.tm_min)#分
# print(tuple_time.tm_sec)#秒
# print(tuple_time.tm_wday)#一周第几天
# print(tuple_time.tm_yday)#一年第几天

#当前时间
# print(time.ctime())#返回一个格式化的时间
# print(time.ctime(1234567890))#将一个时间戳，转换为格式化的字符串时间

#将一个结构化时间转换为时间戳。
# print(time.mktime(time.localtime()))

#时间日期：
import datetime
print(datetime.datetime.now())#日期时间