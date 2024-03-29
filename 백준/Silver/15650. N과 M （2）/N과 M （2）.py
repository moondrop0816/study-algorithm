from itertools import combinations
N, M = map(int, input().split())
ls = list(combinations(range(1, N+1), M))

for i in ls:
    for j in i:
        print(j)