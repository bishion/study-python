#!/usr/bin/env python3
arr = range(1, 10, 2)
it = iter(arr)
print(next(it))

print(next(it))

for x in it:
    print(x, end=' ')
