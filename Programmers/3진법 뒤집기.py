def solution(n):
    n_3 = ''
    while n:
        n_3 += str(n % 3)
        n //= 3
    return int(n_3, 3)


assert solution(125) == 229
