def get_prime_numbers(n_min=2, n_max=1000000):
    n_list = [False, False] + [True] * (n_max - 1)
    for i in range(2, n_max + 1):
        if not n_list[i]:
            continue

        for j in range(i * 2, n_max + 1, i):
            n_list[j] = False

    return [idx for idx, n in enumerate(n_list) if n and idx >= n_min]


m, n = [int(input()) for _ in range(2)]
prime_numbers = get_prime_numbers(m, n)
print(sum(prime_numbers), min(prime_numbers), sep='\n') if prime_numbers else print(-1)
