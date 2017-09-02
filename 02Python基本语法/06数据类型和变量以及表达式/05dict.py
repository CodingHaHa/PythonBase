#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by fengL on 2017/8/31

#1:dict（字典）的基本使用：
d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
print(d["Michael"])#根据key从dict中获取对应的值。

#2:dict的查找速度很快，其查找原理和字典一样的。？
#为何快？给定一个名字，比如'Michael'，dict在内部就可以直接计算出Michael对应的存放成绩的“页码”，也就是95这个数字存放的内存地址，直接取出来，所以速度非常快。
#这种key-value存储方式，在放进去的时候，必须根据key算出value的存放位置，这样，取的时候才能根据key直接拿到value。

#3:通过key来创建值：
d['Adam'] = 67
print(d["Adam"])

#4:由于一个key只能对应一个value，所以，多次对一个key放入value，后面的值会把前面的值冲掉：
d['Jack'] = 90
print(d['Jack'])
d['Jack'] = 190#会把之前的值覆盖掉
print(d['Jack'])

#5：如果key不存在，dict就会报错：KeyError

#6：通过dict提供的get方法，如果key不存在，可以返回None，或者自己指定的value：
print(d.get('Thomas'))
#注意：返回None的时候Python的交互式命令行不显示结果。


#如果没有对应的key,就给该key设置一个默认值。
print(d.get('Thomas', -1))

#7:删除一个key:pop(key);对应的value也会从dict中删除：
print(d.pop('Bob'))
print(d)

#8:注意，dict内部存放的顺序和key放入的顺序是没有关系的。


#9:dict.setdefault:如果有键 就不再进行修改了；键不存在就新增键值对;并返回相应的值
a = {"a":"a"}
print(a["a"])

a.setdefault("a",53)
print(a["a"])


#10：items():获取所有的元组
a = {"a":"a","b":"b"}
print()

#11：keys()：获取所有的key
print(a.keys())

#12:values()：获取所有的值
print(a.values())

#上面3个函数返回的类型不是list,要想其对应的list，需要进行转换
print(list(a.items()))

#13:update（）更新，扩展
dic1 = {"age":"12","name":"ss","b":"111"}#若有键重复，则进行值的覆盖
dic2 = {"a":42,"b":55}
dic2.update(dic1)
print(dic2)

#14：删除：将字典全部删除
del dic1
# print(dic1)#没有改dic1字典对象了，所以报错。

#15：clear():清空字典，把内容删除，变量还保留
dic2.clear()
print(dic2)

#16:formkeys：以第一个元素的每一个作为key,后一个元素作为值
dic3 = dict.fromkeys(["host","port","dns"],"value---")
print(dic3)
dic3 = dict.fromkeys(["host","port","dns"],["value---","ssss"])#{'host': ['value---', 'ssss'], 'port': ['value---', 'ssss'], 'dns': ['value---', 'ssss']}
print(dic3)


#17:字典嵌套：
vv_site = {
    "美国":{
        "旧金山":"很有钱",
        "纽约":"很犯法"
    }
    ,
    "中国":{
        "北京":"很大",
        "成都":"也很大"

    }
}
print(vv_site)
#进行修改
vv_site["美国"]["纽约"] = "大大大"
print(vv_site)

#18：排序：字典是根据key进行排序的
dic = {5:"11",2:"ss",88:"44"}
print(sorted(dic))
print(sorted(dic.values()))

#19:字典的遍历：
for i in dic:
    print(i,dic.get(i),dic[i])#默认打印的是键

# for i,v in dic.items():#这里有一个转换，效率不高
#     print(i,v)

"""
dict有以下几个特点：
    查找和插入的速度极快，不会随着key的增加而变慢；
    需要占用大量的内存，内存浪费多。
    而list相反：

    查找和插入的时间随着元素的增加而增加；
    占用空间小，浪费内存很少。
    所以，dict是用空间来换取时间的一种方法。

    dict可以用在需要高速查找的很多地方，在Python代码中几乎无处不在，正确使用dict非常重要，需要牢记的第一条就是dict的key必须是不可变对象。
    这是因为dict根据key来计算value的存储位置，如果每次计算相同的key得出的结果不同，那dict内部就完全混乱了。这个通过key计算位置的算法称为哈希算法（Hash）。
    要保证hash的正确性，作为key的对象就不能变。在Python中，字符串、整数等都是不可变的，因此，可以放心地作为key。而list是可变的，就不能作为key：
"""