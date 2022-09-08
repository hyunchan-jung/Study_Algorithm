def func(n):
    return n if n <= 1 else func(n - 1) + func(n - 2)


print(func(int(input())))
