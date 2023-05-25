dice = list(map(int, input().split(' ')))
dice = sorted(dice, key=lambda x: dice.count(x), reverse=True)
cnt = dice.count(dice[0])
print(10000 + (dice[0] * 1000) if cnt == 3 else 1000 + (dice[0] * 100) if cnt == 2 else max(dice) * 100)
