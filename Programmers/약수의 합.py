def solution(n):
    return sum([i for i in range(1, n//2+1) if not n % i]) + n
