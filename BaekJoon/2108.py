import sys
from collections import Counter

n = int(sys.stdin.readline())
n_list = sorted([int(sys.stdin.readline()) for _ in range(n)])
counter = Counter(n_list).most_common()
counter = [i for i in counter if i[1] == counter[0][1]]
print(round(sum(n_list) / n))
print(n_list[n//2])
print(counter[0][0] if len(counter) == 1 else sorted([i[0] for i in counter])[1])
print(max(n_list) - min(n_list))
