import sys

chess = list()
chess_w = ('WBWBWBWB' + 'BWBWBWBW') * 4
chess_b = ('BWBWBWBW' + 'WBWBWBWB') * 4
n, m = map(int, input().split(' '))
for _ in range(n):
    chess.append(sys.stdin.readline().strip())

result = 32
for i in range(n - 7):
    for j in range(m - 7):
        crop = ''.join([k[j:j + 8] for k in chess[i:i + 8]])
        cnt = min(map(lambda x: [i == j for i, j in zip(crop, x)].count(False), [chess_w, chess_b]))
        if cnt < result:
            result = cnt
print(result)
