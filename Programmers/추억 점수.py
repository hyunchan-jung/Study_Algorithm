def solution(name, yearning, photo):
    score_map = {n: y for n, y in zip(name, yearning)}
    return [sum([score_map.get(n, 0) for n in p]) for p in photo]


assert solution(name=['may', 'kein', 'kain', 'radi'],
                yearning=[5, 10, 1, 3],
                photo=[['may', 'kein', 'kain', 'radi'],
                       ['may', 'kein', 'brin', 'deny'],
                       ['kon', 'kain', 'may', 'coni']]) == [19, 15, 6]
