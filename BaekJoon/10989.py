import sys

n_list = [0] * 10001
for _ in range(int(sys.stdin.readline())):
    n_list[int(sys.stdin.readline())] += 1

for i in range(len(n_list)):
    for _ in range(n_list[i]):
        print(i)
