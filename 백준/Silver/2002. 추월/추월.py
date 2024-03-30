n = int(input())
enter, out = {}, []
cnt = 0
for i in range(n):
    enter[input()] = i
for _ in range(n):
    out.append(input())

for j in range(n):
    for k in range(j+1, n):
        if enter[out[j]] > enter[out[k]]:
            cnt += 1
            break

print(cnt)