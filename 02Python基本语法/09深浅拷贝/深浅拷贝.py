#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by fengL on 2017/9/2

#1:操作独立的两个list，不会相互影响
# s = [1,"feng","lian"]
# s1 = [1,"feng","lian"]
# s1[0] = 2#修改第二个list不会影响第一个list
# print(s)
# print(s1)

#2:copy
# s = [1,"feng","lian"]#当列表中的元素是不可变时，对拷贝出来的list进行修改，不会影响原始的list
# s1 = s.copy()
# print(s)
# print(s1)
# s1[0] = 3
# print(s)
# print(s1)

#修改拷贝后list中的可变对象，就会有影响
# s = [[1,2],"ali","baidu"]
# s2 = s.copy()
# print(s2)
# s2[1]="libai"#修改不可变对象，不会产生影响
# print(s)
# print(s2)
# s2[0][0] = 44#修改内部的list后，会产生影响。因为list是可变对象
# print(s)
# print(s2)

#浅拷贝：只会拷贝地址，如果某个地址是指向一个可变对象，那么当修改该对象时，就会产生影响。

#3：=和copy的区别：
#=赋值操作：直接将一个变量的地址拷贝给另一个变量，这样造成两个变量同时指向同一个地址，修改他们任何一个的值，都会影响到另一个对象。
#copy方法：对于不变对象会重新开辟内存，对于可变对象则直接拷贝地址。
#此二者是不同的。

#4：浅拷贝用处：少，例如，银行原卡+副卡（它们共享同一个金额）


#5：深度拷贝：引入拷贝模块
import  copy
s = [[1,2],"ali","baidu"]
s2 = copy.deepcopy(s )
print(s2)
s2[0][1]=77#深度拷贝，修改就不会影响前面的值
print(s)
print(s2)



