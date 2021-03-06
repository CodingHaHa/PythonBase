#1:列表的基本使用：
classmates = ['Michael', 'Bob', 'Tracy']
print (classmates)

#2：获取列表的长度
print(len(classmates))

#3:用索引来访问list中每一个位置的元素，记得索引是从0开始的：
print(classmates[0])
print(classmates[1])
print(classmates[2])
# print(classmates[3])#超出列表长度，会报一个IndexError异常。


#4：取最后一个元素，除了计算索引位置外，还可以用-1做索引，直接获取最后一个元素；以此类推，可以获取倒数第2个、倒数第3个：
print(classmates[-1])
print(classmates[-2])
print(classmates[-3])

#5：list是一个可变的有序表，所以，可以往list中追加元素到末尾：
classmates.append('Adam')
print(classmates)

#6:可以把元素插入到指定的位置
classmates.insert(1, 'Jack')
print(classmates)

#7:删除list末尾的元素，用pop()方法：
pop = classmates.pop()
print(pop)
print(classmates)

#8:删除指定位置的元素，用pop(i)方法，其中i是索引位置
pop = classmates.pop(1)
print(pop)
print(classmates)

#9:把某个元素替换成别的元素，可以直接赋值给对应的索引位置
classmates[1] = 'Sarah'
print(classmates)

#10:list里面的元素的数据类型也可以不同
L = ['Apple', 123, True]
print(L)

#11:list元素也可以是另一个list
s = ['python', 'java', ['asp', 'php'], 'scheme']
len(s)#要注意s只有4个元素，其中s[2]又是一个list，如果拆开写就更容易理解了

#12:如果一个list中一个元素也没有，就是一个空的list，它的长度为0：
L = []
print(len(L))

#13：增：切片：
s = ['python', 'java', 'asp', 'php', 'scheme']
print(s[1:2])#['java']
print(s[1:4])#['java', 'asp', 'php']
print(s[1:])#['java', 'asp', 'php', 'scheme']，取到最后一个元素
print(s[1:-1])#['java', 'asp', 'php']，取到倒数第二个元素
print(s[1::2])#['java', 'php']，取到最后一个元素，（步长为2）
print(s[1:-1:2])#['java', 'php']，取到最后一个元素，（步长为2）

#14：count:统计出现的次数
count = ["to","be","to","not"].count("to")
print(count)

#15:extend方法：扩展列表：
a = [1,3,2]
b = [7,8,6]
a.extend(b)#
print(a)#a被b扩展了，元素多了。
print(b)

#16：index方法：获取某个元素所在的索引
a = ["a","b","c","d"]
print(a.index("c"))

#17:reverse:反转顺序：
a = ["a","b","c","d"]
a.reverse()#返回的还是a列表，它内部元素的顺序被颠倒了。
print(a)

#18：sort排序
a = [3,8,9,10]
a.sort()
print(a)

#19 type :查询类型
print(type(a) is list)