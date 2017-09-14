#1：实例一：
# import threading,time
# class Boss(threading.Thread):
#     def run(self):
#         print("BOSS：今晚大家都要加班到22:00。")
#         event.isSet() or event.set()
#         time.sleep(5)
#         print("BOSS：<22:00>可以下班了。")
#         event.isSet() or event.set()
# class Worker(threading.Thread):
#     def run(self):
#         event.wait()
#         print("Worker：哎……命苦啊！")
#         time.sleep(0.25)
#         event.clear()
#         event.wait()
#         print("Worker：OhYeah!")
# if __name__=="__main__":
#     event=threading.Event()
#     threads=[]
#     for i in range(5):
#         threads.append(Worker())
#     threads.append(Boss())
#     for t in threads:
#         t.start()
#     for t in threads:
#         t.join()

#2：实例二：
import threading,time
import random
def light():
    if not event.isSet():
        event.set() #wait就不阻塞 #绿灯状态
    count = 0
    while True:
        if count < 10:
            print('\033[42;1m--green light on---\033[0m')
        elif count <13:
            print('\033[43;1m--yellow light on---\033[0m')
        elif count <20:
            if event.isSet():
                event.clear()
            print('\033[41;1m--red light on---\033[0m')
        else:
            count = 0
            event.set() #打开绿灯
        time.sleep(1)
        count +=1
def car(n):
    while 1:
        time.sleep(random.randrange(10))
        if  event.isSet(): #绿灯
            print("car [%s] is running.." % n)
        else:
            print("car [%s] is waiting for the red light.." %n)
if __name__ == '__main__':
    event = threading.Event()
    Light = threading.Thread(target=light)
    Light.start()
    for i in range(3):
        t = threading.Thread(target=car,args=(i,))
        t.start()