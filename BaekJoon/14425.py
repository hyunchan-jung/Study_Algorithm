from sys import stdin

n, m = map(int, input().split(' '))
s = dict().fromkeys(set([stdin.readline() for _ in range(n)]))
cnt = 0
for _ in range(m):
    if stdin.readline() in s:
        cnt += 1
print(cnt)
