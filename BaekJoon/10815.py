_, my_cards = input(), dict().fromkeys(sorted(map(int, input().split(' '))))
_, compare_cards = input(), map(int, input().split(' '))

for card in compare_cards:
    if card in my_cards:
        print(1, end=' ')
    else:
        print(0, end=' ')
