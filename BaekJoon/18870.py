input()
loc_list = list(map(int, input().split(' ')))
loc_dict = {n: idx for idx, n in enumerate(sorted(set(loc_list)))}
print(*[loc_dict[i] for i in loc_list])
