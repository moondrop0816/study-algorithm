from collections import deque
n, k = map(int, input().split())
m = 10 ** 5
visited = [0] * (m + 1)

def bfs(start):
    queue = deque([start])
    while deque:
        x = queue.popleft()
        if x == k:
            print(visited[k])
            break
        for i in (x + 1, x - 1, x * 2):
            if 0 <= i <= m and not visited[i]:
                visited[i] = visited[x] + 1
                queue.append(i)
        
bfs(n)
