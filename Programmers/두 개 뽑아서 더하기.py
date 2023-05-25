from itertools import combinations


def solution(numbers):
    return sorted(set(map(sum, combinations(numbers, 2))))


assert solution([2, 1, 3, 4, 1]) == [2, 3, 4, 5, 6, 7]
assert solution([5, 0, 2, 7]) == [2, 5, 7, 9, 12]
