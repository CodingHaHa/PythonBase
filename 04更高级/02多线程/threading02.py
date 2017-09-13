# #1：简单的多线程程序
# from time import ctime,sleep
# def music(func):
#     for i in range(2):
#         print("I was listening to %s. %s" % (func,ctime()))
#         sleep(1)
#
# def move(func):
#     for i in range(2):
#         print("I was at the %s ! %s" % ( func,ctime()))
#         sleep(5)
#
# if __name__ == "__main__":
#     music(u"七里香")
#     move(u"世界陌路")

#2：又一个多线程例子：
from time import ctime,sleep
import threading
def music(func):
    for i in range(2):
        print("I was listening to %s. %s" % (func,ctime()))
        sleep(1)
        print("end listening %s"  % ctime() )

def move(func):
    for i in range(2):
        print("I was at the %s ! %s" % ( func,ctime()))
        sleep(5)
        print("end watching %s" % ctime())

threads = []
t1 = threading.Thread(target=music,args=("七里香",))
threads.append(t1)
t2 = threading.Thread(target=move,args=("求生之路",))
threads.append(t2)

if __name__ == "__main__":
    for t in threads:
        t.start()
    print("all over %s" % ctime())



