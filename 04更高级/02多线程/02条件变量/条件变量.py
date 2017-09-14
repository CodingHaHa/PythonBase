#条件变量
import threading,time
from random import randint
#生产者
class Producer(threading.Thread):
    def run(self):
        global L
        while True:
            val=randint(0,100)
            print('生产者',self.name,":Append"+str(val),L)
            #使用条件变量。
            if lock_con.acquire():
                L.append(val)
                lock_con.notify()
                lock_con.release()
            time.sleep(3)

#消费者
class Consumer(threading.Thread):
    def run(self):
        global L
        while True:
                lock_con.acquire()#而是在这理开始执行
                if len(L)==0:
                    lock_con.wait()
                    print("ok")#被唤醒后不会继续从这里执行
                print('消费者',self.name,":Delete"+str(L[0]),L)
                del L[0]
                lock_con.release()
                time.sleep(0.25)

if __name__=="__main__":

    L=[]
    #使用同一个条件
    lock_con=threading.Condition()
    threads=[]
    for i in range(5):
        threads.append(Producer())
    threads.append(Consumer())
    for t in threads:
        t.start()
    for t in threads:
        t.join()