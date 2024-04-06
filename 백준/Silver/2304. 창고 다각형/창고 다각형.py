n = int(input())

info = [0] * 1001
max_height = 0
max_height_idx = 0
end_idx = 0

for i in range(n):
    w, h = map(int, input().split())
    info[w] = h
    if max_height < h:
        max_height = h
        max_height_idx = w
    end_idx = max(end_idx, w)

stack = []
result = 0

for i in range(0, max_height_idx + 1):
    if not stack:
        stack.append(info[i])
    else:
        if stack[-1] < info[i]:
            stack.pop()
            stack.append(info[i])
    result += stack[-1]

stack = []
for j in range(end_idx, max_height_idx, -1):
    if not stack:
        stack.append(info[j])
    else:
        if stack[-1] < info[j]:
            stack.pop()
            stack.append(info[j])
    result += stack[-1]

print(result)