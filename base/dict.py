var1 = dict([('shape', 123), ('guido', 4127), ('jack', 4098)])
print(var1)

for k, v in var1.items():
    print(k, v)

for i, v in enumerate(var1):
    print(i, v)

names = {"guo": 91, "bizi": 12, "bishion": 99}
print(names["guo"])

num_set = set([1, 2, 3, 4, 4, 1])
print(num_set)

num_set = [1, 2, 3, 4, 4, 1]
num_set.sort()
print(num_set)