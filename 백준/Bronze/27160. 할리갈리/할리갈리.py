N = int(input())
fruits = {"STRAWBERRY": 0, "BANANA": 0, "LIME":0, "PLUM": 0}
for _ in range(N):
    S, X = input().split()
    fruits[S] += int(X)
    
if 5 in fruits.values():
    print('YES')
else:
    print('NO')