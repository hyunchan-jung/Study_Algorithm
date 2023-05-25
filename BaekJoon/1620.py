from sys import stdin

n, m = map(int, input().split(' '))
s = {i: stdin.readline().strip() for i in range(1, n+1)}
s_ = {v: k for k, v in s.items()}

for _ in range(m):
    i = stdin.readline().strip()
    print(s[int(i)] if i.isdigit() else s_[i])
