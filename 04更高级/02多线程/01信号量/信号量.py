#信号量
import threading,time
class myThread(threading.Thread):
    def run(self):
        #通过信号量获取锁
        if semaphore.acquire():
            print(self.name)
            time.sleep(5)
            #释放信号量
            semaphore.release()

if __name__ == "__main__":
    #创建信号量
    semaphore = threading.Semaphore(5)
    thrs = []
    for i in range(100):
        thrs.append(myThread())

    for t in thrs:
        t.start()

#Python中线程最多1000多个。再多了就会使得效率下将。

