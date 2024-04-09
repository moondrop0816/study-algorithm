import sys
input = sys.stdin.readline

n = int(input())
building = 0
stack = []
for i in range(n):
    x, y = map(int, input().split())

    while stack and stack[-1] > y:
        building += 1
        stack.pop()
    if stack and stack[-1] == y:
        continue
    stack.append(y)

while stack:
    if stack[-1] > 0:
        building += 1
    stack.pop()

print(building)
