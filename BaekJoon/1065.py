cnt = 0
for n in range(1, int(input()) + 1):
    if n < 100:
        cnt += 1
        continue

    n = str(n)
    if len(set([int(n[i]) - int(n[i - 1]) for i in range(1, len(n))])) == 1:
        cnt += 1

print(cnt)
