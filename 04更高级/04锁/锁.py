import threading,time
# #1：不加锁
# def addNum():
#     global num
#
#     time.sleep(0.1)
#     temp = num
#     print("--get num:",num)
#     num = temp -1
#
# num = 100
# thread_list = []
# for i in range(100):
#     t = threading.Thread(target=addNum)
#     t.start()
#     thread_list.append(t)
#
# for t in thread_list:
#      t.join()
#
# print("final num:" ,num)



#2加锁：
#①：获取锁
# r = threading.Lock()
# def addNum():
#     global num
#
#     time.sleep(0.1)
#     #②：添加锁（将临界区代码放到锁内部）
#     r.acquire()
#     temp = num
#     print("--get num:",num)
#     num = temp -1
#     #③：释放锁
#     r.release()
#
# num = 100
# thread_list = []
# for i in range(100):
#     t = threading.Thread(target=addNum)
#     t.start()
#     thread_list.append(t)
#
# for t in thread_list:
#      t.join()
#
# print("final num:" ,num)

#3：如果Python解释器没有GIL：结果还是如同2中一样吗？
#还是一样的，因为都加了锁。

