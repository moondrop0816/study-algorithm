n = int(input())
numbers = list(map(int, input().split()))
sort_nums = sorted(set(numbers))
dict = {sort_nums[i] : i for i in range(len(sort_nums))} 
for j in range(len(numbers)):
    numbers[j] = dict[numbers[j]]
print(' '.join(map(str, numbers)))