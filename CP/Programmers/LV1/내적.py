def solution(a, b):
    res = 0
    for i, j in zip(a, b):
        res += i*j
    return res