def get_prime_numbers(n_min=2, n_max=1000000):
    bool_list = [False, False] + [True] * (n_max - 1)
    n_list = list()
    for i in range(2, n_max + 1):
        if not bool_list[i]:
            continue

        if i >= n_min:
            n_list.append(i)

        for j in range(i * 2, n_max + 1, i):
            bool_list[j] = False

    return n_list


for n in get_prime_numbers(*list(map(int, input().split(' ')))):
    print(n)
