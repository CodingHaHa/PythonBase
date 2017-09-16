#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by fengL on 2017/9/16

#

# #python2中默认使用的编码为ASCII
# import sys
# print sys.getdefaultencoding()#ascii
# #所以在python2中直接打印中文报错：而添加# -*- coding: utf-8 -*-后就可以了。
# print("中文")

# #python3中默认使用的编码为ASCII
import sys
print( sys.getdefaultencoding())#utf-8
#所以在python2中直接打印中文报错：而添加# -*- coding: utf-8 -*-后就可以了。
print("中文")



