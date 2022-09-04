n, i, j = int(input()), 1, 0
while n > i:
    j += 1
    i += 6 * j
print(j + 1)
