#成员修饰符：
#一：字段
# class Foo:
#
#      #私有静态字段
#     __v = "123"
#
#     def __init__(self,name,age):
#         self.name  = name
#         # self.age = age
#         #__私有的:外界就不能访问了
#         #普通字段
#         self.__age = age
#
#     #该函数内部可以访问，可以通过公用的方法去访问。
#     def show(self):
#         return self.__age
#
#     #静态方法
#     @staticmethod
#     def stat():
#         return Foo.__v
#
# obj = Foo("febg",19)
# print(obj.name)
# # print(obj.__age)#AttributeError: 'Foo' object has no attribute  '__age' 私有变量外部无法直接访问。
# print(obj.show())#通过公用的方法可以访问到。
#
# #静态私有字段，外部也是不能访问的
# # print(obj.__v)
#
# #通过静态方法来服务私有静态字段。
# print(obj.stat())


#方法：
class Foo:
    #私有方法：__方法名
    def __f1(self):
        return 123


    def f2(self):
        #通过一个公用方法去调用私有方法。
        return self.__f1()

obj = Foo()
# ret = obj.__f1()#AttributeError: 'Foo' object has no attribute '__f1';外部不能直接访问私有方法

#通过调用公用方法，在这个公用方法内部去调用私有方法。
ret = obj.f2()

print(ret)


#继承时对于私有成员，时不会被子类继承的。
