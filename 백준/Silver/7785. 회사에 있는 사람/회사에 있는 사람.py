import sys
n = int(sys.stdin.readline())
name_list = {}
result = ''
for i in range(n):
    name, state = sys.stdin.readline().split()
    if state == 'enter':
        name_list[name] = state
    else:
        del name_list[name]
for i in sorted(name_list.keys(), reverse=True):
    result += i + '\n'
print(result)