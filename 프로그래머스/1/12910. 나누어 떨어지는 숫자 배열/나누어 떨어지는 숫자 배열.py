def solution(arr, divisor):
    result = list(filter(lambda el: el % divisor == 0, arr))
    if len(result) == 0:
        result.append(-1)
    result.sort()
    return result
