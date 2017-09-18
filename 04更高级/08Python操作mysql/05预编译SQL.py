#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by fengL on 2017/9/18
import pymysql


#创建数据库连接
conn = pymysql.connect(host="127.0.0.1",port=3306,user="root",passwd="Root",db="pymysql",charset="utf8")

#创建游标
cursor = conn.cursor()

# name = input("请输入用户名:")
# print(name)
# age = int(input("请求输入年龄："))
# print(age)
#执行SQL，返回结果为受影响的行数
#一定要使用这样的方式，而避免使用字符串拼接的方式，为了防止SQL注入。
# r = cursor.execute("insert into user(name) values (%s)",name)
#如果要传入多个参数，就通过传入一个元组的方式
# r = cursor.execute("insert into user(name,age) values (%s,%s)",(name,age))

#批量执行SQL:通过传入一个list，里面存多个元组。
# l = [("age",10),("feng",55),("fengluian",88)]
#然后调用cursor.executemany方法
# r = cursor.executemany("insert into user(name,age) values (%s,%s)",l)

#增删改查都可以使用cursor.execute方法来执行。

#update
# r = cursor.execute("update user set name=%s where name =%s",("fengLian","feng"))
#提交SQL,查询时不用进行commit操作。
# conn.commit()


#查询操作：查询所欲结构
data = cursor.execute("select * from user where name =%s",("fengLian"))
#取所有记录
# r = cursor.fetchall()
#获取多个记录
# r = cursor.fetchmany(2)
#获取一条记录：fetchone类似指针，每取一次往下移动一条记录。
r = cursor.fetchone()
print(r)
#
r = cursor.fetchone()
print(r)
r = cursor.fetchone()
print(r)

#游标实际就是指针，我们可以直接操作指针，来移动
#mode模式可以取值为：absolute（指针回到绝对位置，）；relative(相对位置1向下移动一个位置，-1向上移动一个位置。)
cursor.scroll(0,mode="absolute")

# 关闭游标
cursor.close()
# 关闭连接
conn.close()

#注意：数据库分页和游标获取记录不冲突的，数据库分页是在数据库里面进行的，而游标只是把数据库里面的数据拿到内存厘里面，通过游标的相应fetch查询来以不同的方式获取这些分页后的数据。