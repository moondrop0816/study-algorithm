n = int(input())
m = int(input())
s = input()
target = 'I'+'I'.join('O' * n)+'I'
cnt = 0
for i in range(m):
    if s[i:i+len(target)] == target:
        cnt += 1

print(cnt)