def solution(n, m, section):
    cnt = 0
    cur = 0
    for s in section:
        if s > cur:
            cnt += 1
            cur = s+m-1
    return cnt