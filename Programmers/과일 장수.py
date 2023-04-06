def solution(k, m, score):
    answer = 0
    score.sort(reverse=True)

    for i in range(0, len(score), m):
        box = score[i:i+m]
        if len(box) == m:
            answer += min(box) * m

    return answer


assert solution(3, 4, [1, 2, 3, 1, 2, 3, 1]) == 8
assert solution(4, 3, [4, 1, 2, 2, 4, 4, 4, 4, 1, 2, 4, 2]) == 33
