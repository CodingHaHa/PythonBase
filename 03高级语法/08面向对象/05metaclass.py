# #1:类也是对象
# class Foo:
#     def func(self):
#         print(123)
#
# #这样是创建一个Foo类的对象
# obj = Foo()
# #=============================
# def function(self):
#     print(123)
#
# #这样也是定义一个类，
# # Foo = type("Foo",(object,),{"func":function})
# #使用lamba表达式，替换function函数的定义
# Foo = type("Foo",(object,),{"func":lambda x:123})
# #这样也是创建一个Foo类的对象
# obj = Foo()



#2:定义我们自己的type类：
class MyType(type):

    #这里的self指代的是：Foo（类）对象。
    def __init__(self,*args,**kwargs):
        print(123)
        pass

    #这里的self指代的是：Foo（类）对象。
    def __call__(self, *args, **kwargs):
        print("159")

#当解释器，识别到Foo时就会执行
class Foo(object,metaclass=MyType):
    def __init__(self):
        pass

    #这里才是真正创建obj对象的真实位置。
    def __new__(cls, *args, **kwargs):
        pass

    def func(self):
        print("hello wupeiqi")

obj = Foo()
