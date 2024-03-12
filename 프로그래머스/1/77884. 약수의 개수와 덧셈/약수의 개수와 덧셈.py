def solution(left, right):
    total = 0
    for i in range(left, right+1):
        divisors = set()
        for j in range(1, i+1):
            if i % j == 0:
                divisors.add(j)
                divisors.add(i // j)
        if len(divisors) % 2 == 0:
            total += i
        else:
            total -= i
    return total