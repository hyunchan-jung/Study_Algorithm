for _ in range(int(input())):
    n, score = 1, 0
    for s in input():
        if s == 'O':
            score += n
            n += 1
        else:
            n = 1
    print(score)
