def solution(s):
    answer = ''
    words = s.split(' ')
    for word in words:
        if len(word) > 0:
            answer += word[0].upper() + word[1:].lower() + ' '
        else:
            answer += ' '
    return answer[:-1]
