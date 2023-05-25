import sys

word_list = set(sys.stdin.readline().strip() for _ in range(int(input())))
print(*sorted(word_list, key=lambda x: (len(x), x)), sep='\n')
