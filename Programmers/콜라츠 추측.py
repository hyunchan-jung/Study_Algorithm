def solution(n):
    cnt = 0
    while n != 1 and cnt <= 500:
        cnt += 1
        n = (n * 3 + 1) if n % 2 else (n // 2)
    return cnt if not cnt > 500 else -1


assert solution(626331) == -1
