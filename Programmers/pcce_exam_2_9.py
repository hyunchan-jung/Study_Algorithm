def solution(serial):
    answer = ''
    answer += 'male/' if serial[:2] == '01' else 'female/'
    answer += ['operation', 'sales', 'develop', 'finance', 'law', 'research'][int(serial[3])] + '/'
    answer += str(int(serial[4:6])) + 'team/'
    answer += 'valid' if sum(map(int, serial[:6])) % 13 == int(serial[6:]) else 'invalid'
    return answer


assert solution('01100103') == 'male/operation/1team/valid'
