def solution(N, stages):
    result = []
    for n in range(1, N + 1):
        users = [stage for stage in stages if stage >= n]
        fail_rate = stages.count(n) / len(users) if users else 0
        result.append((n, fail_rate))

    result.sort(key=lambda x: [x[1], -x[0]], reverse=True)
    return [stage for stage, fail_rate in result]


assert solution(5, [2, 1, 2, 6, 2, 4, 3, 3]) == [3, 4, 2, 1, 5]
assert solution(4, [4, 4, 4, 4, 4]) == [4, 1, 2, 3]
