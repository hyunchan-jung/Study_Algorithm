from itertools import combinations

_, m = map(int, input().split(' '))
card_list = map(int, input().split(' '))
result = 0

for cards in combinations(card_list, 3):
    if result < sum(cards) <= m:
        result = sum(cards)
print(result)
