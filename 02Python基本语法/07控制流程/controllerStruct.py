#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by fengL on 2017/9/1

#1:if-else
if 2<3:
    print("true")
elif 3>1:
    print("false")
elif 4 == 4:
    print(" 4 == 4")
else:
    print("overs")

#2:for:
for x in range(1,3):
    print(x)
    if x == 2:
        break#如果这里执行了break，那么就不会在继续执行后续的else语句。
else:#这里的else会在for循环正常执行完毕后再，执行
    print("for over")