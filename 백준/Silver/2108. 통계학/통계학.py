import sys
n = int(input())
nums = sorted(int(sys.stdin.readline()) for _ in range(n))
avg = round(sum(nums) / n) 
mid = nums[len(nums) // 2] 
range = nums[-1] - nums[0] 
mode_dict = {}
for i in nums:
    if i in mode_dict:
        mode_dict[i] += 1
    else:
        mode_dict[i] = 1
mode = list(filter(lambda x: mode_dict[x] == max(mode_dict.values()), mode_dict.keys()))

print(avg)
print(mid)
print(mode[1] if len(mode) > 1 else mode[0])
print(range)