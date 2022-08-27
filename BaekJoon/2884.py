h, m = map(int, input().split(' '))
h = (h + (m - 45) // 60) % 24
m = (m - 45) % 60
print(h, m)
