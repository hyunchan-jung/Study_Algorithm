def solution(food):
    answer = ''

    for i, count in enumerate(food):
        if count < 2:
            continue

        answer += str(i) * (count // 2)

    answer = answer + '0' + answer[::-1]
    return answer


assert solution([1, 3, 4, 6]) == '1223330333221'
assert solution([1, 7, 1, 2]) == '111303111'
