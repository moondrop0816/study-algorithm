from collections import deque
n = int(input())
balloons = deque(enumerate(map(int, input().split())))
order = []

while balloons:
    idx, paper = balloons.popleft() 
    order.append(idx + 1) 

    if paper > 0: 
        balloons.rotate(-(paper - 1)) 
    elif paper < 0: 
        balloons.rotate(-paper)

print(' '.join(map(str, order)))
