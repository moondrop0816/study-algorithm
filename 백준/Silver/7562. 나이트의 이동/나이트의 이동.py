from collections import deque
t = int(input())

for _ in range(t):
    l = int(input())
    now = list(map(int, input().split())) 
    dest = list(map(int, input().split())) 
    graph = [[0] * l for _ in range(l + 1)]
    visited = [[False] * l for _ in range(l + 1)]

    queue = deque()
    dx = [-2, -2, -1, 1, 2, 2, -1, 1]
    dy = [-1, 1, 2, 2, 1, -1, -2, -2]

    def bfs():
        queue.append(now)
        visited[now[0]][now[1]]

        while queue:
            x, y = queue.popleft()
            if x == dest[0] and y == dest[1]:
                return 0

            for i in range(8):
                nx = x + dx[i]
                ny = y + dy[i]

                if nx < 0 or nx >= l or ny < 0 or ny >= l:
                    continue

                if nx == dest[0] and ny == dest[1]:
                    visited[nx][ny] = True
                    return graph[x][y] + 1

                if visited[nx][ny] == False:
                    queue.append([nx, ny])
                    visited[nx][ny] = True
                    graph[nx][ny] = graph[x][y] + 1

    result = bfs()
    print(result)