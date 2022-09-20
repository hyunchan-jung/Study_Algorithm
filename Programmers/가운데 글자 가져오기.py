def solution(s):
    n = len(s)
    return s[n//2] if n % 2 else s[n//2:n//2+1]
