from heapq import *
n = int(input())
heap = [int(input()) for _ in range(n)]
heapify(heap)
result = 0
while len(heap) > 1:
    x = heappop(heap)
    y = heappop(heap)
    heappush(heap, x + y)
    result += x + y
print(result)
