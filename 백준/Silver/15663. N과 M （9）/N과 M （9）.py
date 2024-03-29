N, M = map(int, input().split())
num_list = sorted(list(map(int, input().split())))
s = []
visited = [False] * N

def dfs():
    if len(s) == M:
        print(' '.join((map(str, s))))
        return
    remember_me = 0
    for i in range(N):
        if not visited[i] and remember_me != num_list[i]:
            visited[i] = True
            s.append(num_list[i])
            remember_me = num_list[i]
            dfs()
            s.pop()
            visited[i] = False

dfs()