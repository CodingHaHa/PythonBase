# #1：我们之前写的程序都是在一个线程里面顺序执行的
# import time
# begin = time.time()
# def foo():
#     print("foo")
#     #sleep时候cpu是不会工作的
#     time.sleep(1)
#
# def bar():
#     print("bar")
#     time.sleep(2)
#
# foo()
# bar()
# end = time.time()
# print(end-begin)


#2：多个线程;使用线程需要引入一个模块：threading
import  threading
import time
begin = time.time()
def foo(n):
    print("foo",n)
    #sleep时候cpu是不会工作的
    time.sleep(1)
    print("end foo...")

def bar(n):
    print("bar",n)
    time.sleep(2)
    print("end far...")

#使用线程，就是为了执行任务。
#创建线程：target:指定要执行的函数名，args:用于指定函数的参数。
t1 = threading.Thread(target=foo,args=(1,))
t2 = threading.Thread(target=bar,args=(10,))
#这里创建了两个线程，还有一个主线程。

#让线程跑起来。
t1.start()
t2.start()
print("....in the main....")

#主线程等待t1线程执行完毕后才会继续执行
t1.join()
#主线程等待t2线程执行完毕后才会继续执行
t2.join()
end = time.time()
print(end-begin)


