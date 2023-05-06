from string import ascii_lowercase


def solution(s, skip, index):
    answer = ''
    ascii_strings = ''.join(i for i in ascii_lowercase if i not in skip)

    for alp in s:
        idx = ascii_strings.index(alp)
        answer += ascii_strings[(idx + index) % len(ascii_strings)]

    return answer
