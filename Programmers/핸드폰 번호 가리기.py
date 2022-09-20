def solution(phone_number):
    return '*' * (len(phone_number) - 4) + phone_number[-4:]


assert solution('027778888') == '*****8888'
