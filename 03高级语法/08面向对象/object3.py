#中国的所有省份，用面向对象？
#1：类中的字段。
# class Province:
#     #静态字段：属于类
#     country = "中国"
#     def __init__(self,name):
#         #普通字段：属于对象
#         self.name = name
#
# henan = Province('河南')
# hebei = Province('河北')
# #普通字段：只能通过对象来访问。
# print(hebei.name)
#
# #静态字段：可以直接通过类名访问。
# print(Province.country)
#
# #静态字段也可以通过，对象访问
# print(hebei.country)

#2：类中的方法：
# class Foo:
#         def bar(self):
#             #self：是对象
#             print("bar")
#
#         #静态方法：添加装饰器
#         @staticmethod
#         def sta():#静态方法中self不用再传给方法了。
#             print("123")
#
#         @staticmethod
#         def sta(a1,a2):#静态方法中self不用再传给方法了。
#             print(a1,a2)
#
#         @classmethod
#         def classmd(cls):#类方法需要传入cls参数。（潜规则，参数一般不再写成self，而约定为cls[class缩写]）
#             #cls是类名
#             print("classMethod")




#调用普通方法方式一：最常用的调用普通方法的方式。
# obj = Foo()
# obj.bar()

#调用普通方法方式二：通过类名+另一个对象来调用普通方法。
# obj = Foo()
# Foo.bar(obj)

#调用静态方法：直接通过类名调用。
# Foo.sta(1,2)

#调用类方法：直接通过类名调用
# Foo.classmd()#python会自动为我们把类名作为参数传入



#3：属性：注意对应关系
# class Foo:
#         def __init__(self):
#             #字段的访问：对象.字段===不需要添加括号
#             self.name = "a"
#         #方法的访问：对象.方法()===需要添加括号
#         def bar(self):
#             #self：是对象
#             print("bar")
#
#
#         #属性：同时有字段和方法的特性；定义时像方法，但使用时像属性。
#         #@property：只要执行obj.per
#         @property
#         def per(self):
#             print("123")
#             return 2
#
#         #obj.per = 123;用于设置值
#         @per.setter
#         def per(self,val):
#             print(val)
#
#         @per.deleter
#         def per(self):
#             print("666")
#
#
# obj = Foo()
# obj.per#()，。执行时像方法，不用添加括号。
# #属性：返回值
# print(obj.per)#①：与@property对应
# #给属性赋值
# obj.per  = 45787#②：与@per.setter对应
# print(obj.per)
# del obj.per  #③：与@per.deleter对应


#4：属性的另一种方式
class Foo:
    def f1(self):
        return 123

    def f2(self,val):#注意：必须有一个参数去接受，传过来的123
        print("f2")

    def f3(self):
        print("f3")

    #注意这样的方式
    per = property(fget=f1,fset=f2,fdel=f3,doc="这是一个介绍文档")


obj = Foo()
ret = obj.per
print(ret)
obj.per = 123
del obj.per
