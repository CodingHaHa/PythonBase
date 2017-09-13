# class Foo:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#     def show(self):
#         print(self.name,":",self.age)
#
# obj = Foo()#obj对象，也是Foo类的实例（实例化）
#
# #这里创建了三个Foo类的实例。
# # obj1 = Foo()
# # obj2 = Foo()
# # obj3 = Foo()
#
# #单例目的：就是永远使用同一份对象。
# #1:单例模式简介：
# v = None
# if v:#如果v对象已经存在，直接调用show方法
#     v.show()
# else:#如果v对象不存在，先创建v对象然后再调用show方法
#     v = Foo("feng",123)
#     v.show()

#2：实现单例模式的例子：
class Foo:
    #①：定义一个静态字段（用于保存类的实例对象）
    __v = None

    #②：使用@classmethod注解创建获取实例的类方法
    @classmethod
    def get_instance(cls):
        #③：判断是否存在实例对象：若存在就直接返回该对象。
        if cls.__v:
            return cls.__v
        else:
            #若不存在就先创建实例对象然后再返回该对象。
            cls.__v = Foo()
            return cls.__v

#不要再继续使用类名()的方式来创建对象了
obj1 = Foo.get_instance()
obj2 = Foo.get_instance()
print(obj1)
print(obj2)