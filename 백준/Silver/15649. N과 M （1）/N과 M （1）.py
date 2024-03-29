from itertools import permutations
N, M = map(int, input().split())
ls = list(permutations(range(1, N + 1), M))

for i in ls:
    for j in i:
        print(j, end=' ')