import sys
n, m = map(int, input().split())
t = [int(sys.stdin.readline()) for _ in range(n)]
start, end = min(t), max(t) * m
result = end

while start <= end:
    total = 0
    mid = (start + end) // 2

    for i in range(n):
        total += mid // t[i]

    if total >= m:
        end = mid - 1
        result = min(mid, result)
    else:
        start = mid + 1
print(result)