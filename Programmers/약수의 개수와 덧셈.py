def solution(left, right):
    return sum([-n if len([i for i in range(1, n+1) if not n % i]) % 2 else n for n in range(left, right+1)])


assert solution(13, 17) == 43
