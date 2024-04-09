from heapq import *
t = int(input())
for _ in range(t):
    k = int(input())
    nums = list(map(int, input().split()))
    heapify(nums)
    total = 0
    while len(nums) > 1:
        x = heappop(nums)
        y = heappop(nums)
        total += x + y
        heappush(nums, x + y)
    print(total)
