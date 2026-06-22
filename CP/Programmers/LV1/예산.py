def solution(d, budget):
    res = 0
    cur = 0
    for n in sorted(d):
        cur += n
        if cur <= budget:
            res+=1
    return res