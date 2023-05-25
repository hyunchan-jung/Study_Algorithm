def solution(s):
    return len(s) in (4, 6) and s.isnumeric()


assert not solution('a234')
