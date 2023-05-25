piece = list(map(int, input().split(' ')))
print(' '.join([str(i - j) for i, j in zip([1, 1, 2, 2, 2, 8], piece)]))
