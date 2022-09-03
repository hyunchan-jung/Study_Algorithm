w = input()
for i in ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']:
    w = w.replace(i, ' ')
print(len(w))
