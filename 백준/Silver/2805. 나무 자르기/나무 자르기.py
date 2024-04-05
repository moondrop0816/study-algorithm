n, m = map(int, input().split())
trees = sorted(list(map(int, input().split())))
start, end = 1, max(trees) 
while start <= end: 
    temp = 0 
    mid = (start + end) // 2 
    for i in trees:
        if i >= mid: 
            temp += i - mid 
    if temp >= m: 
        start = mid + 1
    else: 
        end = mid - 1
print(end) 