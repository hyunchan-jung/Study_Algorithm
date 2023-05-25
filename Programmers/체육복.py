"""
여분 체육복을 가진 학생이 체육복을 도난당한 경우를 제외
오름차순으로 정렬하기 때문에 앞번호 학생부터 빌려준다
"""

def solution(n, lost, reserve):
    lost.sort()

    for l in lost.copy():
        if l in reserve:
            lost.remove(l)
            reserve.remove(l)

    for l in lost.copy():
        if l - 1 in reserve:
            lost.remove(l)
            reserve.remove(l - 1)
        elif l + 1 in reserve:
            lost.remove(l)
            reserve.remove(l + 1)

    return n - len(lost)


assert solution(5, [2, 4], [1, 3, 5]) == 5
assert solution(5, [2, 4], [3]) == 4
assert solution(4, [3, 1, 2], [2, 4, 3]) == 3
assert solution(3, [3], [1]) == 2
