n = int(input())
result = 0
for i in range(n - 100 if n > 100 else 1, n):
    if i + sum(map(int, str(i))) == n:
        result = i
        break
print(result)
