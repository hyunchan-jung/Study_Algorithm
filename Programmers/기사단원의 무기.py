def solution(number, limit, power):
    cnt_list = [0] * (number + 1)
    for i in range(1, number + 1):
        for j in range(i, number + 1, i):
            cnt_list[j] += 1

    answer = 0
    for n in range(1, number + 1):
        answer += power if cnt_list[n] > limit else cnt_list[n]

    return answer


assert solution(5, 3, 2) == 10
assert solution(10, 3, 2) == 21
