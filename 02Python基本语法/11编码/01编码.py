#在win上不能以r模式打开，但是在Linux上就可以
# f = open("txt.txt","r")
#解决中文乱码，添加,encoding="utf8")
# f = open("txt.txt","r",encoding="utf8")
# print(f.read())

# print("中国馆")
# print(["中国馆"])

s = "中国"
print(type(s))
print(len(s))

s = u"中国"
print(type(s))
print(len(s))