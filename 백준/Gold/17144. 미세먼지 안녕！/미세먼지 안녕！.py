import sys
input = sys.stdin.readline

def dust_spread():
    temp = [[0] * c for _ in range(r)]
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    for i in range(r):
        for j in range(c):
            current = dust[i][j]
            temp[i][j] += current
            if current != -1 and current != 0:
                data = current // 5
                for k in range(4):
                    nx = i + dx[k]
                    ny = j + dy[k]
                    if 0 <= nx < r and 0 <= ny < c and dust[nx][ny] != -1:
                        temp[nx][ny] += data
                        temp[i][j] -= data
    return temp

def dust_rotate():
    for x in range(air1 - 1, 0, -1):
        dust[x][0] = dust[x - 1][0]

    for y in range(c - 1):
        dust[0][y] = dust[0][y + 1]

    for x in range(air1):
        dust[x][-1] = dust[x + 1][-1]

    for y in range(c - 1, 0, -1):
        dust[air1][y] = dust[air1][y - 1]


    for x in range(air2 + 1, r - 1):
        dust[x][0] = dust[x + 1][0]

    for y in range(c - 1):
        dust[-1][y] = dust[-1][y + 1]

    for x in range(r - 1, air2, -1):
        dust[x][-1] = dust[x - 1][-1]

    for y in range(c - 1, 0, -1):
        dust[air2][y] = dust[air2][y - 1]

    dust[air1][1] = 0
    dust[air2][1] = 0


r, c, t = map(int, input().split())
dust = [list(map(int, input().split())) for _ in range(r)]
for i in range(r):
    if dust[i][0] == -1:
        air1, air2 = i, i+1
        break

for i in range(t):
    dust = dust_spread()
    dust_rotate()

result = 0
for i in dust:
    result += sum(i)

print(result + 2)