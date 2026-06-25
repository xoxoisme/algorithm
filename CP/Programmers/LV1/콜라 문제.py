def solution(a, b, n):
    res, r = 0, 0
    while n >= a:
        n, r = n//a*b, n%a
        res += n
        n += r
    return res