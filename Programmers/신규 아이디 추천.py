import re


def solution(new_id):
    # step 1
    new_id = new_id.lower()

    # step 2
    new_id = re.sub('[^a-z0-9\-\_\.]', '', new_id)

    # step 3
    new_id = re.sub('\.{2,}', '.', new_id)

    # step 4
    new_id = new_id.strip('.')

    # step 5
    new_id = 'a' if new_id == '' else new_id

    # step 6 and step 4
    new_id = new_id[:15]
    new_id = new_id.strip('.')

    # step 7
    new_id = new_id.ljust(3, new_id[-1])

    return new_id


assert solution("...!@BaT#*..y.abcdefghijklm") == "bat.y.abcdefghi"
assert solution("z-+.^.") == "z--"
assert solution("=.=") == "aaa"
assert solution("123_.def") == "123_.def"
assert solution("abcdefghijklmn.p") == "abcdefghijklmn"
