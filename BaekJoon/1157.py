from collections import Counter

counter = Counter(input().upper())
w, n = counter.most_common(1)[0]
print(w if list(counter.values()).count(n) == 1 else '?')
