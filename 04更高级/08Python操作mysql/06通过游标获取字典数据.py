#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by fengL on 2017/9/18
#1：默认通过游标获取的数据是元组类型的。
import pymysql
conn = pymysql.connect(host="127.0.0.1",port=3306,user="root",passwd="Root",db="pymysql",charset="utf8")
#2：设置游标为字典类型
cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
r = cursor.execute("select * from user")
data = cursor.fetchall()
print(data)
conn.commit()
cursor.close()
conn.close()

