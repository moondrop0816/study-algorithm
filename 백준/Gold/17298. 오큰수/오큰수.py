n = int(input())
num_ls = list(map(int, input().split()))
result = [-1 for _ in range(n)]
stack = [] 
for i in range(n): 
    while stack and num_ls[i] > num_ls[stack[-1]]: 
        result[stack[-1]] = num_ls[i] 
        stack.pop() 
    stack.append(i) 
print(*result)

