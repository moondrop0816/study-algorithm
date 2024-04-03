n = int(input())
towers = list(enumerate(map(int, input().split())))
result = [0 for _ in range(n)]
stack = []

for idx, height in towers:
    while stack:
        top_idx, top_height = stack[-1]
        if top_height >= height:
            result[idx] = top_idx + 1
            break
        else:
            stack.pop()
    stack.append((idx, height))

print(*result)
