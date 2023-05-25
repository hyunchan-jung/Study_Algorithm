cnt = 0
for _ in range(int(input())):
    s = input()
    cnt += 1 if False not in [w * s.count(w) in s for w in set(s)] else 0
print(cnt)
