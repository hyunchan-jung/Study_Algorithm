ALP_NUM = {
    alp: str(n)
    for n, alp
    in enumerate('zero,one,two,three,four,five,six,seven,eight,nine'.split(','))
}


def solution(s):
    for alp, n in ALP_NUM.items():
        s = s.replace(alp, n)
    return int(s)


assert solution('one4seveneight') == 1478
