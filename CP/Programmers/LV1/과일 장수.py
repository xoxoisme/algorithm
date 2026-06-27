def solution(k, m, score):
    score.sort(reverse=True)
    sort_list = [score[i:i+m] for i in range(0, len(score), m)]
    res = 0
    for i in range(len(score)//m):
        res += min(sort_list[i])*m
    return res