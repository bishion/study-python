print("Hello world", "Hello")

if True:
    print("True")
else:
    print("False")  # 缩进不一致会导致运行错误

total = 0 + \
        1 + \
        2
print(total)

paragraph = """这是一个段落,
可以由多行组成"""

a = b = c = 10
print(a + b + c)

b = float(a)
print(b)


def hello():
    print("Hello World -- from function")

hello()