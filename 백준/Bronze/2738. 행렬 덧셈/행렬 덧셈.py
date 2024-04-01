n, m = map(int, input().split())
arr1 = [list(map(int, input().split())) for _ in range(n)]
arr2 = [list(map(int, input().split())) for _ in range(n)]
result = ''
for i in range(n):
    for j in range(m):
        result += f"{arr1[i][j] + arr2[i][j]} "
    print(result)
    result = ''