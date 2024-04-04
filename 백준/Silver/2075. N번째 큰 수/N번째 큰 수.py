from heapq import *
n = int(input())
heap = [] 
for _ in range(n):
    for i in list(map(int, input().split())): 
        if len(heap) < n: 
            heappush(heap, i)
        else: 
            if heap[0] < i: 
                heappop(heap) 
                heappush(heap, i) 
print(heap[0])