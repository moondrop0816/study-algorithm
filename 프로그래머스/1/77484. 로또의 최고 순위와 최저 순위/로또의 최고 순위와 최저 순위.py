def solution(lottos, win_nums):
    rank = [6,6,5,4,3,2,1]
    correctNum = len(list(filter(lambda el: el in win_nums, lottos)))
    return [rank[correctNum + lottos.count(0)], rank[correctNum]]