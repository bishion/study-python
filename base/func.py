print(abs(1.2))

print(max(2, 3, 5, 6, 12, 1.2))


def my_abs(x):
    if x > 0:
        return x
    else:
        return -x


print(my_abs(-11))


def power(x, n=3):
    return x ** n


print(power(4))

print(power(4, n=3))


def calc(*numbers):
    total = 0
    for n in numbers:
        total = total + n ** 2
    return total


print(calc(1, 2, 3, 4, 5, 6, 6))

arr = [1, 2, 3, 4]
print(calc(*arr))
print(24 * 3600 * 100)


def person(name, age, **kw):
    print("name:", name, "age:", age, "other:", kw)


person("guo", 18, city="shanghai")
person("guo", 18)


def person(name, age, *, city='beijing', job):
    print(name, age, city, job)


person("guo", 18, job="coder")


def fact(n):
    if n == 1:
        return 1
    return n * fact(n - 1)


print(fact(10))


def fact1(n):
    return fact_iter(n, 1)


def fact_iter(num, product):
    if num == 1:
        return product
    return fact_iter(num - 1, num * product)

print(fact1(10))
