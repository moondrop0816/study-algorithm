S = input()
newSet = set()
for i in range(len(S)):
    for j in range(len(S)):
        j = j + i
        newSet.add(S[i:j+1])
print(len(newSet))