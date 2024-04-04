from heapq import *
n, m = map(int, input().split())
cards = []
for num in list(map(int, input().split())):
    heappush(cards, num)
for i in range(m):
    x = heappop(cards)
    y = heappop(cards)
    heappush(cards, x + y)
    heappush(cards, x + y)
print(sum(cards))