from itertools import combinations
n, s = map(int, input().split())
num = list(map(int, input().split()))
ls = []
for i in range(1, n + 1):
    ls.extend(list(combinations(num, i)))
cnt = 0
for i in ls:
    if sum(i) == s:
        cnt += 1
print(cnt)
