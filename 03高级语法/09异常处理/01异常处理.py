#1：基本的异常处理
while True:
    try:#代码块，用于编写逻辑。
        inp = input("请输入年龄:")
        i = int(inp)
    except Exception as e:
        #如果出错了，会自动执行当前块内容。从e中获取出错信息
        print(e)
        i = 1
    print(i)
