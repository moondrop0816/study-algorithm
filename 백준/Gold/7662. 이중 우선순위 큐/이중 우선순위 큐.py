# I는 q에 요소 추가
# D 1 = 최댓값 삭제
# D -1 = 최솟값 삭제
# 한가지 방향. pop으로 0번째 요소만 제거할 수 있음.
# 최댓값이자 최솟값을 어떻게 정리할수있을지? = 힙 두개 사용
# 두개의 값을 공유해야한다.
import sys
from heapq import *
t = int(input())
for _ in range(t):
    k = int(input())
    max_q = []
    min_q = []
    check = [1] * k

    for i in range(k):
        type, num = sys.stdin.readline().split()
        if type == 'D':
            if num == '-1':
                if min_q:
                    check[heappop(min_q)[1]] = 0
            elif num == '1':
                if max_q:
                    check[heappop(max_q)[1]] = 0
        else:
            heappush(max_q, (-int(num), i))
            heappush(min_q, (int(num), i))

        while min_q and check[min_q[0][1]] == 0:
            heappop(min_q)
        while max_q and check[max_q[0][1]] == 0:
            heappop(max_q)

    if min_q == []:
        print("EMPTY")
    else:
        print(-max_q[0][0], min_q[0][0])