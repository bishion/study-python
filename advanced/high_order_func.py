from functools import reduce

print(abs(-34))
f = abs
print(f(-23))


def add(x, y, f):
    return f(x) + f(y)


print(add(-3, -5, abs))

r = map(abs, [-1, -2, -3, -6, 10])
print(list(r))


def fn(x, y):
    return x * 10 + y


print(reduce(fn, [1, 3, 5, 7, 9]))


def char2num(s):
    return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]


print(reduce(fn, map(char2num, "123456")))


def str2num(ss):
    def fn2(x, y):
        return x * 10 + y

    def char2num2(s):
        return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]

    return reduce(fn2, map(char2num2, ss))


print(str2num("231"))


def str2int(s):
    return reduce(lambda x, y: x * 10 + y, map(char2num, s))


print(str2int("22231"))
