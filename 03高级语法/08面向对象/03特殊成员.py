#特殊成员
#1：__call__(self, *args, **kwargs)方法。
# class Foo:
#     def __init__(self):
#         print("init")
#
#     #当对象后面添加了括号，就会执行这个方法。
#     def __call__(self, *args, **kwargs):
#         print("call")


# obj = Foo()
# #对象后面添加括号，会去执行，类中的 __call__(self, *args, **kwargs):方法
# obj()

#前面两句话，和下面一样的。
# Foo()()


#2:int（）转换的结果
#__str__方法，用于打印内容。
# s = "123"
# s = str("123")
# i = int(s)
# print(i,type(i))
#
# class Foo:
#     def __init__(self):
#         pass
#
#     #用于使用int(obj),进行转换时，调用该方法，并且该方法的返回值作为int（）转换的结果。
#     def __int__(self):
#         return 1
#
#     #当使用str(obj),进行转换时，调用该方法，并且该方法的返回值作为str（）转换的结果。
#     def __str__(self):
#         return "feng"
#
#
# obj = Foo()
# print(obj)#打印对象时，就会默认执行__str__方法；该语句其实执行的是，print(str(obj))

# #自动执行对象的__int__方法，并且该方法的返回值，作为转换结果
# print(int(obj))#使用int来进行转换时，内部会执行一个特殊方法，该特殊方法的返回值作为转换的结果；__int__方法
# #同样的__str__()方法
# print(str(obj))


#3：__add__()方法
# class Foo:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#
#     #当两个对象相加时，自动执行第一个对象的__add__()方法
#     def __add__(self, other):
#         # self=obj1 => obj1 = Foo("feng",19)
#         # other = obj2 =>  obj2 = Foo("lian",10)
#
#         #我们可以自定义返回的内容
#         # return self.age + other.age
#         return  Foo("obj3",self.age + other.age)
#
#
# obj1 = Foo("feng",19)
# obj2 = Foo("lian",10)
#
# #当两个对象相加时，自动执行第一个对象的__add__()方法，并且将第二个对象当中参数传入
# r = obj1+obj2
# print(r)


#4：__dict__()方法，将对象中封装的所有内容，通过字典的形式返回
# class Foo:
#     """
#         当前类是干嘛的，注释
#     """
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#
#
# obj = Foo("feng",19)
# #在对象上调用__dict__会将对象中封装的 内容，通过字典的形式返回。
# d = obj.__dict__
# print(d)
#
# #在类上调用__dict__
# ret = Foo.__dict__
# print(ret)


# #5：__getitem__（）方法让对象支持通过索引来取值
# class Foo:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#
#     #获取
#     def __getitem__(self, item):
#         # return item+10
#         #如果item是基本类型：int,str,索引获取
#         #如果item是slice对象：切片
#         print(item,type(item))
#         if type(item) == slice:
#             print("希望做切片处理")
#             print(item.start)#开始位置
#             print(item.stop)#结束位置
#             print(item.step)#步长
#
#         else:
#             print("希望做索引处理")
#     #设置
#     def __setitem__(self, key, value):
#         print(key,value)
#
#     #删除
#     def __delitem__(self, key):
#         print(key)
#
# li = Foo("feng",20)
# r= li[8] #自动执行li对象的类中的__getitem__方法，把8当中参数传递给这个__getitem__方法
# print(r)
#
# li[100] = 123 #自动执行对应li对象的类中的__setitem__()方法；赋值
#
# del li[999] #自动执行对应li对象的类中的__delitem__()方法；删除
#
# li[2:4:2]#切片处理
# li[234]#索引处理



#6：for循环：迭代器
class Foo:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    #如果类中有__iter__()方法，对象就是一个可迭代对象
    #对象.__iter__()的返回值：迭代器 。
    #for循环，迭代器，next
    #for循环，可迭代对象，对象.__iter__(),迭代器，next方法。
    def __iter__(self):
        # return [11,22,33]
        return iter([11,22,33])



#一般的可迭代对象。
# li = [11,22,33]
# for item in li:
#         print(item)

li = Foo("feng",15)
#A：执行li对象的类F类中的__iter__()方法,获取其返回值。
#B:循环上一步返回的对象。
for i in li:
    print(i)

#这里要分情况：
#①：i,迭代器：next方法。
for item in i:
    print(item)

#②：可迭代对象，执行对象的__iter__()方法，获取迭代器，让后在进行循环，next方法。。
for item in i:
    print(item)