T = int(input())
for i in range(T):
    R, S = input().split(' ')
    P = ''
    for j in list(S):
        P += j * int(R)
    print(P)