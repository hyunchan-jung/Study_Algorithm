n, i = int(input()), 1
while n > i:
    n -= i
    i += 1
print(f'{n}/{i - n + 1}' if i % 2 == 0 else f'{i - n + 1}/{n}')
