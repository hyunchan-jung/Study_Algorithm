def get_prime_numbers(n_end):
    n_list = [False, False] + [True] * (n_end - 1)
    for i in range(2, n_end + 1):
        if not n_list[i]:
            continue

        for j in range(i * 2, n_end + 1, i):
            n_list[j] = False

    return [idx for idx, n in enumerate(n_list) if n]


prime_numbers = get_prime_numbers(1000)
input()
print(len([i for i in map(int, input().split(' ')) if i in prime_numbers]))
