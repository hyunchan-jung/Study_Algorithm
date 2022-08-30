_, x = map(int, input().split(' '))
print(' '.join([str(i) for i in map(int, input().split(' ')) if i < x]))
