x, n = [int(input()) for _ in range(2)]
for _ in range(n):
    a, b = map(int, input().split(' '))
    x -= a * b
print('Yes' if x == 0 else 'No')
