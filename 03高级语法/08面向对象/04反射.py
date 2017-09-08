# #1：反射，处理对象中的成员
# class Foo:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#
#     def show(self):
#         print("name:",self.name)
#         print("age:",self.age)
#
# obj = Foo("feng",19)
# print(obj.name)
# b = "name"
#
# ## 通过"name"获取feng这个值：如何实现？
# #方式一：
# # print(obj.__dict__["name"])
# #
# # #方式二：低级做法
# # if b == "name"：
# #     obj.name
#
# #方式三：通过反射来实现
# b = "name"
# #反射：getattr():去哪里获取什么值
# #A:通过反射获取值
# print(getattr(obj,b))
# #B：通过反射调用方法
# func = getattr(obj,"show")
# func()
#
# #反射：hasattr（）检测有没有某个成员
# print(hasattr(obj,"name"))
#
#
# #反射：setattr(),设置某个值
# # print(obj.k1)
# #
# setattr(obj,"k1","v1")
# print(obj.k1)
#
# #反射：删除某个成员
# delattr(obj,"k1")
# # print(obj.k1)


# #2：通过反射，处理类中的成员。[类也是一个对象]
# class Foo:
#     stat = "123"
#
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#
# r = getattr(Foo,"stat")
# print(r)

# #3:反射：操作模块中的成员;把模块当中一个对象
# import fanshe
#
# # r1 = fanshe.NAME
# # print(r1)
# # fanshe.func()
#
# #通过反射：获取模块中的属性
# r1 = getattr(fanshe,"NAME")
# print(r1)
# #通过反射：获取模块中的方法
# r2 = getattr(fanshe,"func")
# r2()
#
# #通过反射：获取模块中的类
# foo = getattr(fanshe,"Foo")
# print(foo)

