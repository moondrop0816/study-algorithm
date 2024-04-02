switch_num = int(input())
switch_state = list(map(int, input().split()))
student = int(input())
student_info = [list(map(int, input().split())) for _ in range(student)]

for i in range(student):
    num = student_info[i][1]
    if student_info[i][0] == 1:
        for j in range(switch_num):
            if (j+1) % num == 0:
                switch_state[j] = abs(switch_state[j] - 1)
            else: continue
    else:
        j = 0
        while num - (j+2) >= 0 and num + j < switch_num:
            if switch_state[num - (j+2)] != switch_state[num + j]:
                break
            else:
                switch_state[num - (j+2)] = abs(switch_state[num - (j+2)] - 1)
                switch_state[num + j] = abs(switch_state[num + j] - 1)
                j += 1
        switch_state[num-1] = abs(switch_state[num-1] - 1)
result = ''
for i in range(switch_num):
    result += f"{switch_state[i]} "
    if (i + 1) % 20 == 0:
        result += '\n'
print(result)