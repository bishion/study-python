from collections import Iterator

result = isinstance((x for x in range(10)), Iterator)
print(result)

it = iter([1, 2, 3, 4, 5])
while True:
    try:
        x = next(it)
        print(x)
    except StopIteration:
        break
