n = int(input())
cnt = 0
while n % 5 != 0:
    n -= 3
    cnt += 1
    if n < 3:
        break
print(cnt + n // 5 if n % 5 == 0 else -1)
