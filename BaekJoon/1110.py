n = int(input())
nn, cycle = str(n), 0
while True:
    nn = '0' + nn if len(nn) == 1 else nn
    nn = nn[1] + str(sum(map(int, nn)))[-1]
    cycle += 1
    if int(nn) == n:
        break
print(cycle)
