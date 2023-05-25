h, m = map(int, input().split(' '))
cook_m = int(input())
h = (h + (m + cook_m) // 60) % 24
m = (m + cook_m) % 60
print(h, m)
