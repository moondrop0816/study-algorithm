n = int(input())
room = [list(input()) for _ in range(n)]
w, h = 0, 0
for i in range(n):
    temp_w = ''
    temp_h = ''
    for j in range(n):
        # 가로
        if room[i][j] == '.':
            temp_w += '.'
        else:
            if len(temp_w) >= 2:
                w += 1
            temp_w = ''

        # 세로
        if room[j][i] == '.':
            temp_h += '.'
        else:
            if len(temp_h) >= 2:
                h += 1
            temp_h = ''

    if len(temp_w) >= 2:
        w += 1
    if len(temp_h) >= 2:
        h += 1

print(w, h)