n = int(input())

memo = {0: 0, 1: 1}
def fibo2(n):
    if n in memo:
        return memo[n]
    memo[n] = fibo2(n-1) + fibo2(n-2)
    return memo[n]

print(fibo2(n))