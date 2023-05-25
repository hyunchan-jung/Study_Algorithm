def solution(a, b):
    return sum(range(min((a, b)), max((a, b))+1))


assert solution(5, 3) == 12
