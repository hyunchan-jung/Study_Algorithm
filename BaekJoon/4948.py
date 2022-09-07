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


prime_numbers = get_prime_numbers(2, 123456 * 2)
while True:
    n = int(input())
    if n == 0:
        break
    print(len([i for i in prime_numbers if n < i <= n * 2]))
