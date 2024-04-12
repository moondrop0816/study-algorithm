import sys
input = sys.stdin.readline
n = int(input())
meeting = sorted((tuple(map(int, input().split())) for _ in range(n)), key=lambda x: (x[1], x[0]))
cnt = 1
endtime = meeting[0][1]
for i in range(1, n):
    if meeting[i][0] >= endtime:
        cnt += 1
        endtime = meeting[i][1]

print(cnt)