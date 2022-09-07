n = int(input())
div_n = 2
while n != 1:
    if n % div_n == 0:
        n //= div_n
        print(div_n)
    else:
        div_n += 1
