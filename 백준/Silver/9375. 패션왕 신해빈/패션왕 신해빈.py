import sys
case = int(input())
for _ in range(case):
    n = int(input())
    clothes = {}
    for _ in range(n):
        name, type = sys.stdin.readline().rstrip().split()

        if type in clothes:
            clothes[type] += 1
        else:
            clothes[type] = 1
    result = 1
    for i in clothes:
        result *= (clothes[i] + 1)
    print(result - 1)