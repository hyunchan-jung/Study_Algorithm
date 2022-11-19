from itertools import combinations


def solution(number):
    return len(list(filter(lambda x: sum(x) == 0, combinations(number, 3))))


assert solution([-2, 3, 0, 2, -5]) == 2
assert solution([-3, -2, -1, 0, 1, 2, 3]) == 5
