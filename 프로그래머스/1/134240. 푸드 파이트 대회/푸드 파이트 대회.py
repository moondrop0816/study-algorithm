def solution(food):
    left = ''
    for i in range(1, len(food)):
        for j in range(food[i] // 2):
            left += str(i)
    right = left[::-1]
    left += '0'
    return left + right
        