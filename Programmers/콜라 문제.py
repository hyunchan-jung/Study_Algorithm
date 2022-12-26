def solution(a, b, n):
    result = 0

    while n >= a:
        cnt = n // a * a
        n += cnt // a * b - cnt
        result += cnt // a * b

    return result


assert solution(2, 1, 20) == 19
assert solution(3, 1, 20) == 9
