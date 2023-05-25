from itertools import combinations


def get_prime_numbers(n):
    prime_numbers = [False, False] + ([True] * (n - 1))
    for i in range(2, n+1):
        if not prime_numbers[i]:
            continue

        for j in range(i+i, n+1, i):
            prime_numbers[j] = False

    return prime_numbers


def solution(nums):
    numbers = [sum(i) for i in combinations(nums, 3)]
    max_n = max(numbers)
    prime_numbers = get_prime_numbers(max_n)

    return len([i for i in numbers if prime_numbers[i]])


assert solution([1, 2, 3, 4]) == 1
assert solution([1, 2, 7, 6, 4]) == 4
