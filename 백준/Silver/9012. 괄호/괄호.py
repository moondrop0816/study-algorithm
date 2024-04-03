t = int(input())
str_ls = [input() for _ in range(t)]

def check_vps(str):
    stack = [] 
    for char in str: 
        if char == '(': 
            stack.append(char)
        elif char == ')': 
            if not stack: 
                return False
            stack.pop() 
    return not stack

for str in str_ls:
    print('YES' if check_vps(str) else 'NO')




