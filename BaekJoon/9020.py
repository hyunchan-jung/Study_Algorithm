def is_prime(n):
    if n == 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


for _ in range(int(input())):
    num = int(input())
    n1 = n2 = num // 2
    while n1 > 0:
        if is_prime(n1) and is_prime(n2):
            print(n1, n2)
            break
        else:
            n1 -= 1
            n2 += 1
