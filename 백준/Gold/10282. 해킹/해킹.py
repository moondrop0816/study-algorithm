from heapq import *
import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n, d, c = map(int, input().split())
    graph = [[] for _ in range(n+1)]
    for _ in range(d):
        a, b, s = map(int, input().split())
        graph[b].append([a, s])
    time = [1e9] * (n + 1)
    heap = []
    time[c] = 0
    heappush(heap, [0, c])

    while heap:
        cur_time, cur_node = heappop(heap)
        if time[cur_node] < cur_time:
            continue
        for next_node, next_time in graph[cur_node]:
            if time[next_node] > cur_time + next_time:
                time[next_node] = cur_time + next_time
                heappush(heap, [cur_time + next_time, next_node])
    
    cnt = 0
    result = 0
    for i in time:
        if i != 1e9:
            cnt += 1
            result = max(result, i)
    
    print(cnt, result)
