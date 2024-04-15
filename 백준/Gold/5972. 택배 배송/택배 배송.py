from heapq import *
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append([b, c])
    graph[b].append([a, c])
cost = [1e9 for _ in range(n + 1)]
heap = []
cost[1] = 0
heappush(heap, [0, 1])

while heap:
    cur_cost, cur_node = heappop(heap)
    if cost[cur_node] < cur_cost:
        continue
    for next_node, next_cost in graph[cur_node]:
        if cost[next_node] > cur_cost + next_cost:
            cost[next_node] = cur_cost + next_cost
            heappush(heap, [cur_cost + next_cost, next_node])

print(cost[n])