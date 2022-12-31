def solution(lottos, win_nums):
    match_cnt = 6 - len(set(win_nums) - set(lottos))
    zero_cnt = lottos.count(0)

    min_rank = 6 - match_cnt + 1
    max_rank = 6 - (match_cnt + zero_cnt) + 1

    answer = [6 if i > 6 else i for i in (max_rank, min_rank)]

    return answer


assert solution([44, 1, 0, 0, 31, 25], [31, 10, 45, 1, 6, 19]) == [3, 5]
assert solution([0, 0, 0, 0, 0, 0], [38, 19, 20, 40, 15, 25]) == [1, 6]
assert solution([45, 4, 35, 20, 3, 9], [20, 9, 3, 45, 4, 35]) == [1, 1]
