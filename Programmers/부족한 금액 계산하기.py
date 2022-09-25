def solution(price, money, count):
    money -= sum([price*cnt for cnt in range(1, count+1)])
    return 0 if money > 0 else -money


print(solution(3, 20, 4))
