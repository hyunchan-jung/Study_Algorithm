def solution(n, arr1, arr2):
    answer = []

    for v1, v2 in zip(arr1, arr2):
        v1, v2 = map(lambda x: bin(x)[2:].zfill(n), [v1, v2])
        result = [
            str(int(i) or int(j)).replace('1', '#').replace('0', ' ')
            for i, j
            in zip(v1, v2)
        ]
        answer.append(''.join(result))

    return answer


assert solution(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28]) == \
       ['#####', '# # #', '### #', '#  ##', '#####']
