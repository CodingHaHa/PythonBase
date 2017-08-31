#!-*- coding:utf-8 -*-
print("中国")
#默认在python2下直接执行上面的语句，会出现下面的异常。因为python2默认的字符编码是ASCII，不支持中文的。
#SyntaxError: Non-ASCII character '\xe4' in file H:/MyLearnNotes/Python/PythonBase/02Python�����﷨/02�ַ�����/python2code.py on line 1, but no encoding declared; see http://python.org/dev/peps/pep-0263/ for details

#为了解决这个编码问题：需要直接指定在程序的第一行写   #!-*- coding:utf-8 -*-
#有时：发现即使指定了编码，还是不能在win下的看到正确的字符，why?
#  因为win默认编码为gbk，这是出现win的编码上的。


