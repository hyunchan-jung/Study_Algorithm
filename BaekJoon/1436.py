n = int(input())
num, n_title = 666, 0
while n_title != n:
    if '666' in str(num):
        n_title += 1
        if n_title == n:
            print(num)
            break
    num += 1
