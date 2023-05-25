def func(s, l, r, cnt=1):
    if l >= r:
        return 1, cnt
    elif s[l] != s[r]:
        return 0, cnt
    return func(s, l+1, r-1, cnt+1)


for _ in range(int(input())):
    w = input()
    print(*func(w, 0, len(w) - 1))
