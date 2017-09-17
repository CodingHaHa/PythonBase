#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by fengL on 2017/9/17
import pickle
# #1:pickle的使用：序列化
#
#
# dic = {'name': 'alvin', 'age': 23, 'sex': 'male'}
# print(type(dic))  # <class 'dict'>
# j = pickle.dumps(dic)
# print(type(j))  # <class 'bytes'>
#注意pickle文件写入类型必须是字节类型
# f = open('序列化对象_pickle', 'wb')  # 注意是w是写入str,wb是写入bytes,j是'bytes'
# f.write(j)  # -------------------等价于pickle.dump(dic,f)
# f.close()
#
#
# #2：反序列化
# f = open('序列化对象_pickle', 'rb')
# data = pickle.loads(f.read())  # 等价于data=pickle.load(f)
# print(data['age'])

#pickle序列化的文件我们是看不懂的，而JSON我们可以看懂。


#3:序列化一个函数：
# def foo():
#     print("oko")
#
# data = pickle.dumps(foo)
# with open("json_pickle_test", "wb") as f:
#     f.write(data)

# #4:反序列一个函数：
# #对于一个函数，反序列化时也需要有函数的定义，才能在返序列化后正常执行。
# def foo():
#     print("oko")
#
# f = open("json_pickle_test", "rb")
# data = f.read()
# data = pickle.loads(data)
# data()
