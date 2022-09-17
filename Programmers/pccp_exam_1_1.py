def solution(input_string):
    answer = ''

    for alp in sorted(set([alp for alp in input_string if input_string.count(alp) >= 2])):
        n = input_string.count(alp)
        if alp * n in input_string:
            continue
        for i in range(2, n + 1):
            if n % i == 0 and input_string.count(alp * (n//i)) == i:
                answer += alp
                break

    return answer if answer else 'N'


assert solution('edeaaabbccd') == 'de'
