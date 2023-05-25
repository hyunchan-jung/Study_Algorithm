def solution(s):
    answer = 0

    x_cnt = 0
    other_cnt = 0
    for alp in s:
        if x_cnt == other_cnt:
            answer += 1
            x = alp

        if alp == x:
            x_cnt += 1
        else:
            other_cnt += 1

    return answer
