#!/usr/bin/python3
f = open("/tmp/foo.txt", 'r')
line = f.read()
print(line)
f.close()

f = open("/tmp/foo.txt", 'r')
line = f.readline()
print(line)
f.close()

f = open("/tmp/foo.txt", 'r')
lines = f.readlines()
for line in lines:
    print(line, end='')
print(f.isatty())
f.close()
