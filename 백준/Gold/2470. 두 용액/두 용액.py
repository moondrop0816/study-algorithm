n = int(input())
liquid = list(map(int, input().split())) 
liquid.sort() 

left = 0 
right = n-1 

result = abs(liquid[left] + liquid[right]) 
final = [liquid[left], liquid[right]] 

while left < right: 
    left_val = liquid[left]
    right_val = liquid[right]

    sum = left_val + right_val 

    if abs(sum) < result: 
        result = abs(sum) 
        final = [left_val, right_val] 
        if result == 0: 
            break
    if sum < 0: 
        left += 1 
    else: 
        right -= 1 
print(final[0], final[1]) 
