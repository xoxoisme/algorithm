def solution(arr, divisor):
    res = [n for n in sorted(arr) if n%divisor == 0]
    return res if res else [-1]