def solution(arr, divisor):
    return sorted([i for i in arr if not i % divisor]) or [-1]


assert solution([5, 9, 7, 10], 5) == [5, 10]
