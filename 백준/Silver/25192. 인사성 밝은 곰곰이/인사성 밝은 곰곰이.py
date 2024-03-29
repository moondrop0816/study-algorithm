N = int(input()) 
ls = set()
emoji = 0
for _ in range(N):
    log = input()
    if log == 'ENTER':
        emoji += len(ls)
        ls.clear()
    else:
        ls.add(log)
emoji += len(ls)
print(emoji)