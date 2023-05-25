def solution(d, budget):
    d.sort()

    while sum(d) > budget:
        d.pop()
    return len(d)


assert solution([1, 3, 2, 5, 4], 9) == 3
