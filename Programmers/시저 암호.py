def solution(s, n):
    alp_lower = 'abcdefghijklmnopqrstuvwxyz'
    alp_upper = alp_lower.upper()
    answer = ''
    for i in s:
        if i.isspace():
            answer += i
        else:
            alp = alp_upper if i.isupper() else alp_lower
            answer += alp[(alp.index(i) + n) % len(alp)]
    return answer


assert solution('a B z', 4) == 'e F d'
