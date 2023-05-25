import sys

loc_list = [list(map(int, sys.stdin.readline().split(' '))) for _ in range(int(input()))]
for loc in sorted(loc_list, key=lambda x: (x[1], x[0])):
    print(*loc)
