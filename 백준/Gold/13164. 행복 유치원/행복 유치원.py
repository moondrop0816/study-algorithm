n, k = map(int, input().split())
arr = list(map(int, input().split()))
cost = []
for i in range(1, len(arr)):
    cost.append(arr[i] - arr[i - 1]) 
cost.sort() 
ans = 0
for i in range(n - k): 
    ans += cost[i]
print(ans)