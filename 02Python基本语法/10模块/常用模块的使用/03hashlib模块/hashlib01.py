#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by fengL on 2017/9/17

import hashlib

# #1:md5加密
# m = hashlib.md5()
# print(m)
# #此时需要一个byte
# m.update("abc".encode("utf8"))
# #hex表示16进制的
# print(m.hexdigest())
#
# #由于之前已经进行了加密，现在的加密是在之前的
# m.update("feng".encode("utf8"))
# print(m.hexdigest())
#
# #其实是对两个字符进行拼接后进行的转换。
# m2 = hashlib.md5()
# m2.update("abcfeng".encode("utf8"))
# print(m2.hexdigest())


#2:sha加密方式，逐渐进行升级
s = hashlib.sha256()
s.update("feng".encode("utf8"))
print(s.hexdigest())

#破解：撞库。

import hashlib

# ######## md5 ########

hash = hashlib.md5()
hash.update('admin')
print(hash.hexdigest())

# ######## sha1 ########

hash = hashlib.sha1()
hash.update('admin')
print(hash.hexdigest())

# ######## sha256 ########

hash = hashlib.sha256()
hash.update('admin')
print(hash.hexdigest())

# ######## sha384 ########

hash = hashlib.sha384()
hash.update('admin')
print(hash.hexdigest())

# ######## sha512 ########

hash = hashlib.sha512()
hash.update('admin')
print(hash.hexdigest())



import hmac
h = hmac.new(b'天王盖地虎', b'宝塔镇河妖')
print(h.hexdigest())

#以上加密算法虽然依然非常厉害，但时候存在缺陷，即：通过撞库可以反解。所以，有必要对加密算法中添加自定义key再来做加密。