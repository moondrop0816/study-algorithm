S = input()
arr = []
for i in range(len(S)):
    for j in range(len(S)):
        j = j + i
        arr.append(S[i:j+1])
newSet = set(arr)
print(len(newSet))