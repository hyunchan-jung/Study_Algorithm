from calendar import monthrange

weekday = 'THU,FRI,SAT,SUN,MON,TUE,WED'.split(',')


def solution(a, b):
    b += sum([monthrange(2016, i)[1] for i in range(1, a)])
    return weekday[b % 7]


assert solution(5, 24) == 'TUE'
