def solution(n, m, section):
    answer = 0
    last = 0

    for s in section:
        if s <= last:
            continue

        answer += 1
        last = s + m - 1

    return answer


assert solution(8, 4, [2, 3, 6]) == 2
assert solution(5, 4, [1, 3]) == 1
assert solution(4, 1, [1, 2, 3, 4]) == 4
