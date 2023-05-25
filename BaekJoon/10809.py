s = input()
print(' '.join([str(s.index(i)) if i in s else '-1' for i in 'abcdefghijklmnopqrstuvwxyz']))
