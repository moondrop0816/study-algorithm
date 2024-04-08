import sys
input = sys.stdin.readline

def dfs(idx):
    global cnt 
    stack = [idx]
    while stack:
        current = stack.pop()
        if visited[current] != 0:
            continue
        visited[current] = cnt
        cnt += 1
        for i in graph[current]:
            if not visited[i]:
                stack.append(i)

n, m, r = map(int, input().split())
graph = [[] for _ in range(n + 1)] 
visited = [0] * (n + 1) 
cnt = 1 

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b) 
    graph[b].append(a)

for i in range(n + 1):
    graph[i].sort(reverse=True)

dfs(r) 

for i in range(1, n + 1): 
    print(visited[i])