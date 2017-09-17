#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by fengL on 2017/9/17



import pymysql

conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='123', db='t1')
cursor = conn.cursor()
cursor.executemany("insert into hosts(host,color_id)values(%s,%s)", [("1.1.1.11", 1), ("1.1.1.11", 2)])
conn.commit()
cursor.close()
conn.close()

# 获取最新自增ID
new_id = cursor.lastrowid