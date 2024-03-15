def solution(n, lost, reserve):
    set_lost = set(lost)
    set_reserve = set(reserve)
    lost_reserve = set_lost & set_reserve

    set_lost -= lost_reserve
    set_reserve -= lost_reserve

    for i in set_reserve:
        if i-1 in set_lost:
            set_lost.remove(i-1)
        elif i+1 in set_lost:
            set_lost.remove(i+1)
    return n - len(set_lost)