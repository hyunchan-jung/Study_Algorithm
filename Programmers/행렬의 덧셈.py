def solution(arr1, arr2):
    return [list(map(sum, zip(*arr))) for arr in zip(arr1, arr2)]


assert solution([[1, 2], [2, 3]], [[3, 4], [5, 6]]) == [[4, 6], [7, 9]]
