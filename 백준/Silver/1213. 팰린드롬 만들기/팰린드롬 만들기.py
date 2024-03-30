str = sorted(input())
letter_dic = {}
start = ''
mid = ''
for i in str:
    if i in letter_dic: letter_dic[i] += 1
    else: letter_dic[i] = 1

if len(list(filter(lambda x: x % 2 == 1,letter_dic.values()))) >= 2:
    print("I'm Sorry Hansoo")
    exit()

for key, value in letter_dic.items():
    if value % 2 != 0:
        mid += key
        start += key * (value // 2)
    else:
        start += key * (value // 2)

print(start + mid + start[::-1])