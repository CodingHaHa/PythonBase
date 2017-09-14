#创建线程的第二种方式：通过创建一个类，继承threading.Thread类的方式
import threading
import time

class MyThread(threading.Thread):
    def __init__(self,num):
        threading.Thread.__init__(self)
        self.num = num

    #在重写父类的run方法：在run方法里面定义每个线程运行的函数。
    def run(self):
        print("running on number:%s" % self.num)


if __name__ == "__main__":
    #创建我们自定义的线程。
    t1 =  MyThread(1)
    t2 =  MyThread(2)
    t1.start()
    t2.start()


