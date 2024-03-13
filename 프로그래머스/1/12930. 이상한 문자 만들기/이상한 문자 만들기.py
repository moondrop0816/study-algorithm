def solution(s):
    arr = s.split(' ')
    for wordIdx in range(len(arr)):
        result = ''
        for idx in range(len(arr[wordIdx])):
            if idx % 2 == 0 : 
                result += arr[wordIdx][idx].upper()
            else:
                result += arr[wordIdx][idx].lower()
        arr[wordIdx] = result
    return ' '.join(arr)