def solution(left, right):
    res = 0
    for n in range(left, right+1):
        divisors_len = len([i for i in range(1, n+1) if n%i == 0])
        if divisors_len%2 == 0: res+=n
        else: res-=n
    return res