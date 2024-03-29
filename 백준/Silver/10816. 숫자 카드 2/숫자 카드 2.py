N = int(input())
cards = sorted(list(map(int, input().split())))
M = int(input())
nums = list(map(int, input().split()))

num_dict = {}
for n in cards:
    if n in num_dict:
        num_dict[n] += 1
    else:
        num_dict[n] = 1


def binary(target, cards, start, end):
    if start > end:
        return 0

    mid = (start + end) // 2

    if target == cards[mid]:
        return num_dict[target]
    elif target < cards[mid]:
        return binary(target, cards, start, mid - 1)
    else:
        return binary(target, cards, mid + 1, end)

for num in nums:
    print(binary(num, cards, 0, len(cards) - 1), end=' ')