def solution(ingredient):
    answer = 0
    stack = []
    ingredient = list(reversed(ingredient))

    for _ in range(len(ingredient)):
        if not ingredient:
            break

        stack.append(ingredient.pop())
        if stack[-4:] == [1, 2, 3, 1]:
            del stack[-4:]
            answer += 1

    return answer
