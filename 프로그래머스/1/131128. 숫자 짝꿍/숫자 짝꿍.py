def solution(X, Y):
    result = ''
    xy = set(X) & set(Y)

    if len(xy) == 0:
        return '-1'

    if len(xy) == 1:
        return ''.join(xy)

    for i in xy:
        result += i * min(X.count(i), Y.count(i))

    return ''.join(sorted(result, reverse=True))