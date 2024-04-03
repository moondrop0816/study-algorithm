str = input()
explode = list(input())
stack = []
for s in str:
    stack.append(s)
    if len(stack) >= len(explode) and stack[-len(explode):] == explode:
        del stack[-len(explode):]

if not stack:
    print('FRULA')
else:
    print(''.join(stack))