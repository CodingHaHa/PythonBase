#1:创建一队列
import  queue
# d = queue.Queue()
# #插入数据到队列后面
# d.put("小米")
# d.put("大猫")
# d.put("品牌")
# #取数据：从队列前面获取数据
# print(d.get())
# print(d.get())
# print(d.get())
# print(d.get())


#2：列表是线程不安全的
# import threading,time
# li=[1,2,3,4,5]
#
# def pri():
#     while li:
#         a=li[-1]
#         print(a)
#         time.sleep(1)
#         try:
#             li.remove(a)
#         except:
#             print('----',a)
#
# t1=threading.Thread(target=pri,args=())
# t1.start()
# t2=threading.Thread(target=pri,args=())
# t2.start()




#3：设置队列长度
d = queue.Queue(2)#这里设置的长度是2，默认是0表示无限大（0或负数都表示无限大）
#放入数据 的参数：
# d.put("小米",0)#这里添加0，不会报错，因为队列还没有满
d.put("小米")
d.put("大猫")
#当想要插入第3个数据时，就会将线程给阻塞住。
# d.put("品牌")
# d.put("品牌",1)#第二个参数默认为1，表示如果队列空间已经被占满了，那么就让线程阻塞
# d.put("品牌",0)#第二个参数默认为0，表示如果队列空间已经被占满了，那么就抛出queue.Full异常。


print(d.get())
print(d.get())
#获取的参数：
#如果获取个数超过了放入数据的个数，那么线程也会被阻塞
# print(d.get())
#设置参数：0表示如果队列空间为空了，那么就抛出queue.Empty异常。
# print(d.get(0))
#设置参数：1表示如果队列空间为空了，那么线程也会被阻塞
# print(d.get(1))


#4：一个例子
#实现一个线程不断生成一个随机数到一个队列中(考虑使用Queue这个模块)
# 实现一个线程从上面的队列里面不断的取出奇数
# 实现另外一个线程从上面的队列里面不断取出偶数
# import random,threading,time
# from queue import Queue
# #Producer thread
# class Producer(threading.Thread):
#   def __init__(self, t_name, queue):
#     threading.Thread.__init__(self,name=t_name)
#     self.data=queue
#   def run(self):
#     for i in range(10):  #随机产生10个数字 ，可以修改为任意大小
#       randomnum=random.randint(1,99)
#       print ("%s: %s is producing %d to the queue!" % (time.ctime(), self.getName(), randomnum))
#       self.data.put(randomnum) #将数据依次存入队列
#       time.sleep(1)
#     print ("%s: %s finished!" %(time.ctime(), self.getName()))
#
# #Consumer thread
# class Consumer_even(threading.Thread):
#   def __init__(self,t_name,queue):
#     threading.Thread.__init__(self,name=t_name)
#     self.data=queue
#   def run(self):
#     while 1:
#       try:
#         val_even = self.data.get(1,5) #get(self, block=True, timeout=None) ,1就是阻塞等待,5是超时5秒
#         if val_even%2==0:
#           print ("%s: %s is consuming. %d in the queue is consumed!" % (time.ctime(),self.getName(),val_even))
#           time.sleep(2)
#         else:
#           self.data.put(val_even)
#           time.sleep(2)
#       except:   #等待输入，超过5秒 就报异常
#         print ("%s: %s finished!" %(time.ctime(),self.getName()))
#         break
# class Consumer_odd(threading.Thread):
#   def __init__(self,t_name,queue):
#     threading.Thread.__init__(self, name=t_name)
#     self.data=queue
#   def run(self):
#     while 1:
#       try:
#         val_odd = self.data.get(1,5)
#         if val_odd%2!=0:
#           print ("%s: %s is consuming. %d in the queue is consumed!" % (time.ctime(), self.getName(), val_odd))
#           time.sleep(2)
#         else:
#           self.data.put(val_odd)
#           time.sleep(2)
#       except:
#         print ("%s: %s finished!" % (time.ctime(), self.getName()))
#         break
# #Main thread
# def main():
#   queue = Queue()
#   producer = Producer('Pro.', queue)
#   consumer_even = Consumer_even('Con_even.', queue)
#   consumer_odd = Consumer_odd('Con_odd.',queue)
#   producer.start()
#   consumer_even.start()
#   consumer_odd.start()
#   producer.join()
#   consumer_even.join()
#   consumer_odd.join()
#   print ('All threads terminate!')
#
# if __name__ == '__main__':
#   main()