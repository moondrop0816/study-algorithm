N = int(input())
dic = {}
for i in range(N):
    _, extend = input().split('.')
    if extend in dic:
        dic[extend] += 1
    else:
        dic[extend] = 1

for key in sorted(dic.keys()):
    print(key, dic[key])