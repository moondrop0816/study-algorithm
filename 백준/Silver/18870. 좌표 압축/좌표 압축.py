n = int(input())
numbers = list(map(int, input().split()))
sort_nums = sorted(set(numbers))
dict = {} 
idx = 0
for i in sort_nums:
    if i in dict:
        pass
    else:
        dict[i] = idx
        idx += 1
for j in range(len(numbers)):
    numbers[j] = dict[numbers[j]]
print(' '.join(map(str, numbers)))