def solution(t, p):
    return len([n for n in range(len(t)) if t[n:n+len(p)] <= p and len(t[n:n+len(p)]) == len(p)]) 