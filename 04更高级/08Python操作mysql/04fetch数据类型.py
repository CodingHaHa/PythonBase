#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by fengL on 2017/9/17

#关于默认获取的数据是元祖类型，如果想要或者字典类型的数据
import pymysql

conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='123', db='t1')

# 游标设置为字典类型
cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
r = cursor.execute("call p1()")

result = cursor.fetchone()

conn.commit()
cursor.close()
conn.close()