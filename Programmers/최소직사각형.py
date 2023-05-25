def solution(sizes):
    return max([min(size) for size in sizes]) * max([max(size) for size in sizes])


assert solution([[60, 50], [30, 70], [60, 30], [80, 40]]) == 4000
