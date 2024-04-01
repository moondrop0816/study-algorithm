arr = [list(map(int, input().split())) for _ in range(9)]
max_dict = {}
for i in range(len(arr)):
    max_dict[i] = max(arr[i])
max = max(max_dict.values())
for i in max_dict.keys():
    if not max in arr[i] :
        continue
    else:
        print(max)
        print(i + 1, arr[i].index(max) + 1)
        exit()

