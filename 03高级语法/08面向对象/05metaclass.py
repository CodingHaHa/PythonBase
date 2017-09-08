# #1:类也是对象：所有类都默认继承object
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
# # Foo = type("Foo",(object,),{"func":function})#参数一：类名，参数二：表示继承object,参数三：定义函数
# #使用lamba表达式，替换function函数的定义
# Foo = type("Foo",(object,),{"func":lambda x:123})
# #这样也是创建一个Foo类的对象
# obj = Foo()



#2:定义我们自己的type类：tpye中的__init__()方法是用C语言实现的。我们不能看到源码
class MyType(type):

    #这里的self指代的是：Foo（类）对象。
    def __init__(self,*args,**kwargs):
        print(123)
        pass

    #这里的self指代的是：Foo（类）对象。
    def __call__(self, *args, **kwargs):
        print("159")

#当解释器，识别到Foo时就会执行MyType类的__init__()方法。
class Foo(object,metaclass=MyType):#metaclass用于指定使用我们自定义的MyType类，来创建类名Foo对象
    def __init__(self):
        pass

    #这里才是真正创建obj对象的真实位置。
    def __new__(cls, *args, **kwargs):
        print("对象")#这里创建obj对象
        pass

    def func(self):
        print("hello wupeiqi")

obj = Foo()
