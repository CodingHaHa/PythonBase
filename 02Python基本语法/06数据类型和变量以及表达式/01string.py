#1:字符串的基本操作：
# print("你好Python")#python3默认的编码为Unicode，所以默认是支持中文的。

#2：字符-和字符编码
# print(ord('A'))#获取字符的整数表示
# print(chr(66))#编码转换为对应的字符

#3:字符串和字节互换
print('ABC'.encode('ascii'))#以Unicode表示的str通过encode()方法可以编码为指定的bytes(b'ABC')
print(b'ABC'.decode('ascii'))#如果我们从网络或磁盘上读取了字节流，那么读到的数据就是bytes。要把bytes变为str，就需要用decode()方法：


#4：获取字符数
print (len("你好"))#如果是字符，则获取字符个数
print (len("你好".encode("utf-8")))#如果是字节，则获取字节个数


#5:格式化字符串
msg = """
Name: %s
Age : %d
Job : IT
Salary: 2000
""" % ("fengLian",45)
print(msg)


#6：进行重复操作，也叫乘法操作
print("hello " * 3)#重复打印3次

#7：字符串切片[]:通过索引取值，[:]切片
print("helloworld"[2:])

#8：in，判断一个字符串是不是在另一个字符串里面。
print("el" in "hello")#在就返回一个True。

#9：字符串拼接：+
a = "1234"
b = "4557"
print(a+b)#拼接:12344557

#字符串拼接：join
c = ''.join([a,b])
print(c)#12344557
c = '4--4'.join([a,b])#以前面的字符进行拼接
print(c)

#字符串内置方法
st = 'he\tllokitty {name} is {age}'
print(st.count("l"))#返回字符串出现的个数
print(st.capitalize())#整个首字符大写
print(st.center(50,"-"))#居中
print(st.endswith("ty"))#以什么字符结尾
print(st.startswith("he"))#以什么字符串开始
print(st.expandtabs(tabsize=10))#设置空格个数\t
print(st.find("t"))#找到第一个元素，并将索引值返回
print(st.format(name="fenglian",age="18"))#将字符串中{name}的值进行替换
print(st.format_map({"name":"fenglian","age":"18"}))#和上一个方法效果一样，只是使用map进行映射
# print(st.index("a8"))#查询字符串的索引值，没有改字符串就报错。
print("啊123啊".isalnum())#判断是不是一个包含数字和字母的字符串，若包含特殊字符返回FALSE
print("45".isdecimal())#判断是不是10进制的数字符串
print("4".isdigit())#判断是不是数字
print("56".isnumeric())
print("34abc".isidentifier())#判断是不是不规范的变量标识
print("abc".islower())#判断是不是全小写
print("BAC".isupper())#判断是不是全大写
print(" ".isspace())#判断是不是空格
print("A Bc D".istitle())#是不是首字母大写
print("a Bc D".istitle())#是不是首字母大写
print("aBcDeF".lower())#大写变小写
print("aBcE".upper())#小写变大写
print("aBcD".swapcase())#大写变小写，小写变大写
print("I lov You".ljust(50,"X"))#靠左右边用X字符串补充
print("I lov You".rjust(50,"X"))#靠右左边用X字符串补充
print(" I lov you ".strip())#除去两边空格和换行符
print(" I lov you ".lstrip())#除去左边空格和换行符
print(" I lov you ".rstrip())#除去右边空格和换行符
print(" I lov you ".replace("lov","XXX"))#替换
print(" I lov you ".rfind("o"))#从左向右找，最后一字符串的索引
print(" I lov you ".split(" "))#分割字符串，返回一个列表。
print(" I lov you ".rsplit(" ",1))#从右开始分割字符串，一次。
print("a title test".title())#首字母大写
print(st.encode("utf-8"))#编码

