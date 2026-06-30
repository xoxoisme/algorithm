def solution(board, moves):
    stack = []
    cnt = 0
    for m in moves:
        for d in range(len(board)):
            if board[d][m-1] != 0:
                if stack and stack[-1] == board[d][m-1]:
                    board[d][m-1] = 0
                    cnt+=2
                    stack.pop()
                    break
                else:
                    stack.append(board[d][m-1])
                    board[d][m-1] = 0
                    break
    return cnt