n = int(input())
n_ls = []
for i in range(n):
    n_ls.append(input())
m = int(input())
m_ls = []
for i in range(m):
    m_ls.append(input())
idx = n_ls.index('?')
prev = idx-1
next = idx+1
for word in m_ls:
    if word in n_ls: continue 
    if idx == 0: 
        if len(n_ls) == 1: print(word)
        elif word[len(word)-1] == n_ls[next][0]:
            print(word)
    elif idx == len(n_ls) - 1: 
        if word[0] == n_ls[prev][len(n_ls[prev])-1]:
            print(word)
    else: 
        if word[0] == n_ls[prev][len(n_ls[prev]) - 1] and word[len(word)-1] == n_ls[next][0]:
            print(word)