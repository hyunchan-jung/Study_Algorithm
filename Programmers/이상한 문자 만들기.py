def solution(s):
    answer = ''
    idx = 0
    for i in s:
        if i == ' ':
            answer += ' '
            idx = 0
        else:
            answer += i.lower() if idx % 2 else i.upper()
            idx += 1
    return answer


print(solution('try hello world'))
