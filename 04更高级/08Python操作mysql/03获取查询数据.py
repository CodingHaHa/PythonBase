#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by fengL on 2017/9/17



import pymysql

conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='123', db='t1')
cursor = conn.cursor()
cursor.execute("select * from hosts")

# 获取第一行数据
row_1 = cursor.fetchone()

# 获取前n行数据
# row_2 = cursor.fetchmany(3)
# 获取所有数据
# row_3 = cursor.fetchall()

conn.commit()
cursor.close()
conn.close()

#注：在fetch数据时按照顺序进行，可以使用cursor.scroll(num,mode)来移动游标位置，如：
# cursor.scroll(1,mode='relative')  # 相对当前位置移动
# cursor.scroll(2,mode='absolute') # 相对绝对位置移动