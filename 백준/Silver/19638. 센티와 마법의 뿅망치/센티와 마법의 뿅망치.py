from heapq import *
import sys
n, h, t = map(int, input().split())
titan_h = [-int(sys.stdin.readline()) for _ in range(n)]
heapify(titan_h)
cnt = 0
for i in range(t):
    if -titan_h[0] == 1 or -titan_h[0] < h: 
        break 
    else: 
        heapreplace(titan_h, -(-titan_h[0] // 2)) 
        cnt += 1 

if -titan_h[0] >= h: 
    print('NO', -titan_h[0], sep='\n')
else: 
    print('YES', cnt, sep='\n')