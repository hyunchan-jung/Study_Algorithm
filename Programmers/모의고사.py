def solution(answers):
    n1 = [1, 2, 3, 4, 5]
    n2 = [2, 1, 2, 3, 2, 4, 2, 5]
    n3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    counts = [0, 0, 0]

    for n, answer in enumerate(answers):
        counts[0] += int(n1[n % len(n1)] == answer)
        counts[1] += int(n2[n % len(n2)] == answer)
        counts[2] += int(n3[n % len(n3)] == answer)

    return [n+1 for n, cnt in enumerate(counts) if cnt == max(counts)]


assert solution([1, 2, 3, 4, 5]) == [1]
assert solution([1, 3, 2, 4, 2]) == [1, 2, 3]
