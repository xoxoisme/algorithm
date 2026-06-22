def solution(n, m):
    max_divisor = max(md for md in range(1, min(n, m)+1) if n%md == 0 and m%md == 0)
    return [max_divisor, n*m//max_divisor]
