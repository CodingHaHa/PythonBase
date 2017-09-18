#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by fengL on 2017/9/17



import pymysql

conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='Root', db='pymysql',charset="utf8")
cursor = conn.cursor()
cursor.executemany("insert into user(name,age) values(%s,%s)", [("1.1.1.11", 1)])
conn.commit()
cursor.close()
conn.close()

# 获取最新自增ID
new_id = cursor.lastrowid
print(new_id)