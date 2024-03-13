def solution(sizes):
    width = map(lambda arr: arr[1] if arr[1] > arr[0] else arr[0], sizes)
    height = map(lambda arr: arr[0] if arr[1] > arr[0] else arr[1], sizes)
    
    return max(width) * max(height)
