N = int(input())
cards = list(map(int, input().split()))
M = int(input())
nums = list(map(int, input().split()))

num_dict = {}
for n in cards:
    if n in num_dict:
        num_dict[n] += 1
    else:
        num_dict[n] = 1

for i in nums:
    if i in num_dict:
        print(num_dict[i], end=' ')
    else:
        print(0, end=' ')