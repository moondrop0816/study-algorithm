def solution(a, b, n):
    total_coke = 0 
    
    while n >= a:
        total_coke += (n // a) * b 
        n = (n % a) + (n // a) * b
        
    return total_coke

