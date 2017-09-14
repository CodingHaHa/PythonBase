# #1死锁：
# import threading,time
#
# class myThread(threading.Thread):
#     def doA(self):
#         lockA.acquire()
#         print(self.name,"gotlockA",time.ctime())
#         time.sleep(3)
#         lockB.acquire()
#         print(self.name,"gotlockB",time.ctime())
#         lockB.release()
#         lockA.release()
#
#     def doB(self):
#         lockB.acquire()
#         print(self.name,"gotlockB",time.ctime())
#         time.sleep(2)
#         lockA.acquire()
#         print(self.name,"gotlockA",time.ctime())
#         lockA.release()
#         lockB.release()
#     def run(self):
#         self.doA()
#         self.doB()
# if __name__=="__main__":
#
#     lockA=threading.Lock()
#     lockB=threading.Lock()
#     threads=[]
#     for i in range(5):
#         threads.append(myThread())
#     for t in threads:
#         t.start()
#     for t in threads:
#         t.join()#等待线程结束，后面再讲。



#2应用L
import time

import threading

class Account:
    def __init__(self, _id, balance):
        self.id = _id
        self.balance = balance
        self.lock = threading.RLock()

    def withdraw(self, amount):

        with self.lock:
            self.balance -= amount

    def deposit(self, amount):
        with self.lock:
            self.balance += amount


    def drawcash(self, amount):#lock.acquire中嵌套lock.acquire的场景

        with self.lock:
            interest=0.05
            count=amount+amount*interest

            self.withdraw(count)


def transfer(_from, to, amount):

    #锁不可以加在这里 因为其他的其它线程执行的其它方法在不加锁的情况下数据同样是不安全的
     _from.withdraw(amount)

     to.deposit(amount)



alex = Account('alex',1000)
yuan = Account('yuan',1000)

t1=threading.Thread(target = transfer, args = (alex,yuan, 100))
t1.start()

t2=threading.Thread(target = transfer, args = (yuan,alex, 200))
t2.start()

t1.join()
t2.join()

print('>>>',alex.balance)
print('>>>',yuan.balance)