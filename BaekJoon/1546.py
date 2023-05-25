n = int(input())
n_list = list(map(int, input().split(' ')))
print(sum([i / max(n_list) * 100 for i in n_list]) / n)
