def solution(board, moves):
    stack = []
    result = 0
    for c in moves:
        for r in range(len(board)):
            cur = board[r][c-1]
            if board[r][c-1] != 0:
                stack.append(board[r][c-1])
                board[r][c-1] = 0
                break
        if len(stack) >= 2 and stack[-1] == stack[-2]:
            del stack[-2:]
            result += 2

    return result