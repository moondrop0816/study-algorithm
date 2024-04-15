import sys
input = sys.stdin.readline
n = int(input())
r = int(input())
student = list(map(int, input().split()))
nominee = {}
for i in student:
    if len(nominee) < n:
        if i in nominee:
            nominee[i] += 1
        else:
            nominee[i] = 1
    else:
        if i in nominee:
            nominee[i] += 1
        else:
            MIN = min(nominee.values())
            for key in nominee.keys():
                if nominee[key] == MIN:
                    del nominee[key]
                    break
            nominee[i] = 1

for i in sorted(nominee.keys()):
    print(i, end=' ')