n = int(input())
road = list(map(int, input().split()))
oil = list(map(int, input().split()))
cost = 0
for i in range(len(oil)-1):
    if i != 0 and oil[i-1] < oil[i]:
        continue
    if oil[i] >= oil[i+1]:
        cost += oil[i] * road[i]
    elif oil[i] < oil[i+1]:
        cost += (oil[i] * road[i]) + (oil[i] * road[i+1])
print(cost)
