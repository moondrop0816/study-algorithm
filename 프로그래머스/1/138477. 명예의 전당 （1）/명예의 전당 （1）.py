def solution(k, score):
    result = []
    for i in range(len(score)):
        if i == 0: 
            stage = [score[0]]
        else: 
            stage = sorted(score[:i+1], reverse=True)
            
        if len(stage) < k:
            result.append(stage[-1])
        else:
            result.append(stage[k-1])
    return result
