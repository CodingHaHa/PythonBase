#1：Python的多继承
# class F1:
#     def a(self):
#         print("F1.a")
#
# class F2:
#     def a(self):
#         print("F2.a")
#
# # class S(F1,F2):
# class S(F2,F1):
#     pass
#
# obj = S()
# obj.a()#多继承选择多个父类共有方法，先继承哪个父类，就调用该父类的方法。



#2：多继承中出现的问题：如何选择父类中的相应方法。
# (无交叉)
# class G:
#     def a1(self):
#         print("G.a")
#
# class GF(G):
#     def a1(self):
#         print("GF.a")
#
# class F1(GF):
#     def a1(self):
#         print("F1.a")
#
# class F2:
#     def a(self):
#         print("F2.a")
#
# # class S(F1,F2):
# class S(F1,F2):
#     pass
#
# obj = S()
# obj.a()

#（有交叉）：
# class Base:
#     def a(self):
#         print("Base.a")
#
# class GF1(Base):
#     def a1(self):
#         print("GF1.a")
#
# class GF2(Base):
#     def a1(self):
#         print("GF2.a")
#
# class F1(GF1):
#     def a1(self):
#         print("F1.a")
#
# class F2(GF2):
#     def a1(self):
#         print("F2.a")
#
# # class S(F1,F2):
# class S(F1,F2):
#     pass
#
# obj = S()
# obj.a()


#3：困难点
# class BaseRequest():
#     pass
#
# class RequestHandler(BaseRequest):
#
#     def server_forever(self):
#         #self:就是obj
#         print("RequestHandler.server_forever")
#         #问题：下面语句执行哪个类的process_request方法呢？Son的
#         self.process_request()#self是Son的实例，所以它还是会调用obj中的process_request方法。
#
#     def process_request(self):
#         print("RequestHandler.process_request")
#
# class Minx:
#     def process_request(self):
#         print("Minx.process_request")
#
# class Son(Minx,RequestHandler):
#     pass
#
# obj = Son()
# obj.server_forever()

#针对构造方法：
class BaseRequest:
    def __init__(self):
        print("Basic.__int__")

class RequestHandler:
    def __init__(self):
        print("RequestHandler.__int__")
        #调用父类的构造器
        # BaseRequest.__init__(self)
        super(Son,self).__init__()

class Minx:
    # def __init__(self):
    #     print("Minx.__int__")
    pass

class Son(Minx,RequestHandler):
    # def __init__(self):
    #     print("Son.init")
    def a(self):
        print("Minx")


obj = Son()
#说明：
    # 如果子类重写了__init__()方法那么调用子类自己的，否则找父类；
    # 如果是多继承，那么从左往右找父类，父类没有重写__init__()方法则继续找父类。
