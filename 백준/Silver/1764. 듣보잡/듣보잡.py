n, m = map(int, input().split())
no_listen, no_see = set(), set()
for i in range(n):
    no_listen.add(input())
for j in range(m):
    no_see.add(input())

result = sorted(no_listen & no_see)
print(len(result))
for name in result:
    print(name)