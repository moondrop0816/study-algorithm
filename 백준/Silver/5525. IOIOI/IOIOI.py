n = int(input())
m = int(input())
s = input()
count, idx, result = 0, 0, 0
while idx < (m-1):
    if s[idx:idx+3] == 'IOI':
        idx += 2
        count += 1
        if count == n:
            result += 1
            count -=1
    else:
        idx += 1
        count = 0

print(result)