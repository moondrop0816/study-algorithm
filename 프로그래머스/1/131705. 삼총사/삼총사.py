import itertools

def solution(number):
    nCr = itertools.combinations(number, 3)
    return len(list(filter(lambda el: sum(el) == 0, nCr)))