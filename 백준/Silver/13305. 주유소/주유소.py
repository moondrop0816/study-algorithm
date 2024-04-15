import sys
input = sys.stdin.readline
n = int(input())
road = list(map(int, input().split()))
oil = list(map(int, input().split()))
min_cost = 1e9
result = 0
for i in range(len(oil)-1):
    if oil[i] < min_cost:
        min_cost = oil[i]
    result += min_cost * road[i]
print(result)
