def solution(n):
    prime = [False, False] + ([True] * (n - 1))

    for i in range(2, n+1):
        if not prime[i]:
            continue

        for j in range(i+i, n+1, i):
            prime[j] = False

    return prime.count(True)


assert solution(10) == 4
assert solution(5) == 3
