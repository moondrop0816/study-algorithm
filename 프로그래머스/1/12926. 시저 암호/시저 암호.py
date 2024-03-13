def solution(s, n):
    upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    lower = 'abcdefghijklmnopqrstuvwxyz'
    result = ''
    
    for i in range(len(s)):
        if s[i] == ' ': 
            result += ' '
        elif s[i].isupper():
            result += upper[(upper.index(s[i]) + n) % 26]
        else:
            result += lower[(lower.index(s[i]) + n) % 26]
    return result