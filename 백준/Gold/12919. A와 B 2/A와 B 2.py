s = list(input())
t = list(input())
def text_check(t):
    if t == s:
        print(1)
        exit(0)
    if len(t) == 0:
        return 0
    if t[-1] == 'A':
        text_check(t[:-1])
    if t[0] == 'B':
        text_check(t[1:][::-1])

text_check(t)
print(0)