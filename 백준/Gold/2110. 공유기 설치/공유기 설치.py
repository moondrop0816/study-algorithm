import sys
n, c = map(int, input().split())
x = sorted(int(sys.stdin.readline()) for _ in range(n))
start = 1
end = x[-1] - x[0]
result = 0

while start <= end:
    mid = (start + end) // 2 
    count = 1 
    current = x[0]

    for i in range(1, len(x)):
        if x[i] >= current + mid:
            count += 1
            current = x[i]

    if count >= c:
        start = mid + 1
        result = mid
    else:
        end = mid - 1


print(result)
