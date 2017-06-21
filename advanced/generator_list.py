g = (x * x for x in range(1, 10))
print(g)
for x in g:
    print(x)


def fib(max_value):
    n, a, b = 0, 0, 1
    while n < max_value:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'


f = fib(10)
print(f)
for x in f:
    print(x, end=' ')


def triangles(lines):
    n, line = 0, [1]
    while n < lines:
        line = [1] + [line[x - 1] + line[x] for x in range(1, len(line))] + [1]
        n = n + 1
        yield line


g = triangles(6)
for x in g:
    print(x)

line = [1] + [2]
print(line)
