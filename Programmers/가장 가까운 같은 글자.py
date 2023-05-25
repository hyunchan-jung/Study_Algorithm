def solution(s):
    answer = []
    index_map = {}
    for idx, v in enumerate(s):
        if v not in index_map:
            answer.append(-1)
        else:
            answer.append(idx - index_map.pop(v))

        index_map[v] = idx

    return answer


assert solution('banana') == [-1, -1, -1, 2, 2, 2]
assert solution('foobar') == [-1, -1, 1, -1, -1, -1]
