n, m = map(int, input().split())
board = [list(input()) for _ in range(n)]
coloring = []
for a in range(n - 7): 
    for b in range(m - 7):
        w_idx = 0
        b_idx = 0
        for i in range(a, a + 8):
            for j in range(b, b + 8):
                if (i + j) % 2 == 0:
                    if board[i][j] != 'W':
                        w_idx += 1
                    else:
                        b_idx += 1
                else:
                    if board[i][j] != 'W':
                        b_idx += 1
                    else:
                        w_idx += 1
        coloring.append(w_idx)
        coloring.append(b_idx)
print(min(coloring))