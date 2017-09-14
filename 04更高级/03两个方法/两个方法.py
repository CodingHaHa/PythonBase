# #1：join方法：
# from time import ctime,sleep
# import threading
# def music(func):
#     for i in range(2):
#         print("I was listening to %s. %s" % (func,ctime()))
#         sleep(1)
#         print("end listening %s"  % ctime() )
#
# def move(func):
#     for i in range(2):
#         print("I was at the %s ! %s" % ( func,ctime()))
#         sleep(5)
#         print("end watching %s" % ctime())
#
# threads = []
# t1 = threading.Thread(target=music,args=("七里香",))
# threads.append(t1)
# t2 = threading.Thread(target=move,args=("求生之路",))
# threads.append(t2)
#
# if __name__ == "__main__":
#     for t in threads:
#         t.start()
#     t.join()#此处主线程调用了t.join()方法，导致主线程阻塞，直到t线程执行完毕。
#     print("all over %s" % ctime())

#2：setDaemon方法：
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
        t.setDaemon(True)#把主线程设置为t子线程的守护线程，这时候，要是主线程执行结束了，就不管子线程是否完成，一并和主线程退出.
        t.start()
    print("all over %s" % ctime())