#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by fengL on 2017/9/17

def hello():
    print("hello")

#我们可以自己调用。
# hello()#测试代码

#只有在本py文件中执行时，下面的条件才会满足。
if __name__ == "__main__":
    print(__name__)#__main__
    hello()
else:
    print(__name__)#foo,当在其他模块调用这个模块时，__name__就是模块名