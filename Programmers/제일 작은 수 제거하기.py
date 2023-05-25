def solution(arr):
    arr.remove(min(arr))
    return arr or [-1]


assert solution([4, 3, 2, 1]) == [4, 3, 2]
assert solution([10]) == [-1]
