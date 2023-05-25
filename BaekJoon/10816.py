from sys import stdin

stdin.readline()
a = dict()
for i in stdin.readline().strip().split(' '):
    a[i] = a.get(i, 0) + 1

stdin.readline()
print(' '.join([str(a[i]) if i in a else '0' for i in stdin.readline().strip().split(' ')]))
