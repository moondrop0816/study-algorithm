from collections import deque
case_num = int(input())
m_ls = []
importance_ls = []

for _ in range(case_num):
    _, m = map(int, input().split())
    m_ls.append(m)
    importance_ls.append(input().split())

def check_order(m, importance_ls):
    deck = deque()
    for i in importance_ls: 
        deck.append(i)
    print_cnt = 0 
    m_import = importance_ls[m] 
    m_idx = m 
    while m_idx >= 0: 
        most_import = max(deck) 
        if deck[0] == most_import:
            print_cnt += 1
            deck.popleft()
            m_idx -= 1
        else:
            if deck[0] == m_import and m_idx == 0:
                m_idx = len(deck) - 1
            else:
                m_idx -= 1
            deck.append(deck.popleft())
    return print_cnt


for i in range(case_num):
    print(check_order(m_ls[i], importance_ls[i]))
