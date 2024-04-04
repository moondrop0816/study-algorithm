from heapq import *
import sys
n = int(input())
x_ls = [int(sys.stdin.readline()) for _ in range(n)]
heap = []
for x in x_ls:
    if x == 0:
        if len(heap) == 0:
            print(0)
        else:
            _, x = heappop(heap)
            print(x)
    else:
        heappush(heap, (abs(x), x))