def solution(N, stages):
    res = []
    n = len(stages)
    for i in range(1, N+1):
        cnt = stages.count(i)
        if n == 0: res.append(0)
        else: res.append(cnt/n)
        n -= cnt
    res = [(i+1, j) for i, j in enumerate(res)]
    res = sorted(res, key = lambda x: (-x[1], x[0]))
    return [t[0] for t in res]