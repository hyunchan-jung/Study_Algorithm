for _ in range(int(input())):
    r, s = input().split(' ')
    print(''.join([i * int(r) for i in s]))
