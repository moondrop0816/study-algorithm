from collections import deque
def bfs(x,y):
    q.append((x, y))
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    visited[x][y] = 1
    while q:
        x, y = q.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < n and 0 <= ny < n and a[nx][ny] == a[x][y] and not visited[nx][ny]:
                visited[nx][ny] = 1
                q.append((nx, ny))

n = int(input())
a = [list(input()) for _ in range(n)]
q = deque()

visited = [[0] * n for _ in range(n)]
cnt1 = 0
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            bfs(i, j)
            cnt1 += 1

for i in range(n):
    for j in range(n):
        if a[i][j] == 'G':
            a[i][j] = 'R'

visited = [[0] * n for _ in range(n)]
cnt2 = 0
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            bfs(i, j)
            cnt2 += 1

print(cnt1, cnt2)