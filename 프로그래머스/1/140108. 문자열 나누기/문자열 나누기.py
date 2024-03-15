def solution(s):
    result = []
    x = ''
    y = ''
    for i in range(len(s)):
        if x == '':
            x += s[i]
        elif x[0] == s[i]:
            x += s[i]
        else:
            y += s[i]

        if len(x) !=0 and len(y) != 0 and len(x) == len(y) or i == len(s) - 1:
            result.append(x+y)
            x = ''
            y = ''

    return len(result)