from collections import Counter


def solution(X, Y):
    answer = ''
    x_cnt = Counter(X)
    y_cnt = Counter(Y)
    nums = x_cnt.keys() & y_cnt.keys()
    if not nums:
        return '-1'

    for num in sorted(nums, reverse=True):
        x_num = x_cnt[num]
        y_num = y_cnt[num]
        answer += num * x_num if x_num < y_num else num * y_num

    return answer.lstrip('0') or '0'
