import sys

info = [list(map(int, sys.stdin.readline().rstrip().split(' '))) for _ in range(int(input()))]
print(' '.join([str(len(list(filter(lambda x: x[0] > i[0] and x[1] > i[1], info))) + 1) for i in info]))
