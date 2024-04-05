n = int(input())
times = sorted(list(map(int, input().split())))
result = 0
for i in range(len(times)):
    result += sum(times[0:i+1])
print(result)
