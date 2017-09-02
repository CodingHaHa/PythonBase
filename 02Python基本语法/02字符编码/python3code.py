print("中国")
#由于python3默认的字符编码就是Unicode，所以，可以直接使用中文。
s = "你好"
# s_to_unicode = s.decode("utf-8")#python 3中只有unicode str，所以把decode方法去掉了
unicode_to_gbk = s .encode("gbk")#编码
print(s)
print(unicode_to_gbk)