def solution(t, p):
    answer = 0

    len_p = len(p)
    for i in range(len(t)):
        value = t[i:i + len_p]
        if (len(value) == len_p and
                int(value) <= int(p)):
            answer += 1

    return answer


assert solution('3141592', '271') == 2
assert solution('500220839878', '7') == 8
assert solution('10203', '15') == 3
