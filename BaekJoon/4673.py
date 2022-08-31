print(*sorted(set(range(1, 10001)) - set([n + sum([int(i) for i in str(n)]) for n in range(1, 10001)])), sep='\n')
