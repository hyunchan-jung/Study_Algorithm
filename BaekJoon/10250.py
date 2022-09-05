for _ in range(int(input())):
    h, w, n = map(int, input().split(' '))
    floor = h if n % h == 0 else n % h
    room = n // h if n % h == 0 else n // h + 1
    print(floor * 100 + room)
