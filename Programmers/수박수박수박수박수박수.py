def solution(n):
    return ('수박' * ((n // 2) + 1))[:-1] if n % 2 else '수박' * (n // 2)
