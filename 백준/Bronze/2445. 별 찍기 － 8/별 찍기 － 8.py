n = int(input())
for i in range(1, n+1):
    half=''
    half += '*' * i
    half += ' ' * (n-i)
    print(half + half[::-1])
for j in range(1, n):
    half = ''
    half += '*' * (n - j)
    half += ' ' * j
    print(half + half[::-1])