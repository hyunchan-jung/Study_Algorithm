def solution(board, moves):
    stack = []
    cnt = 0

    for col in moves:
        for i in range(len(board)):
            if board[i][col-1] != 0:
                stack.append(board[i][col-1])
                board[i][col-1] = 0

                if len(stack) > 1:
                    if stack[-1] == stack[-2]:
                        stack.pop()
                        stack.pop()
                        cnt += 2
                break

    return cnt


assert solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]], [1,5,3,5,1,2,1,4]) == 4
