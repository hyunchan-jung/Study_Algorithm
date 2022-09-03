dial = dict()
[dial.update({w: n for w in s}) for n, s in enumerate(['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ'], 3)]
print(sum([dial[w] for w in input()]))
