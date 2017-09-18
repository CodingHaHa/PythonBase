# #!/usr/bin/env python
# # -*- coding: utf-8 -*-
# # Created by fengL on 2017/9/18
#
# login_status = False
#
# def login():
#     if login_status:
#         username = input("username:")
#         password = input("passwd:")
#         if user == username and password = password:
#             print("welcome.....")
#             home()
#             login_status = True
#     else:
#         pass
#
# #使用装饰器：在各个方法上，都添加上login装饰器，那么就不用访问网站中的每个地方都进要输入用户名和密码进行登录。
# @login
# def home():
#     print("welcome to home page")
#
# @login
# def book():
#     print("welcome to book page")