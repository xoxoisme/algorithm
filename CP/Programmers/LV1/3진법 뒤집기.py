def solution(n):
    reverse_3n = to_base_3(n)
    return int(reverse_3n, 3)

def to_base_3(n):
    if n == 0: return "0"
    digits = []
    while n > 0:
        digits.append(str(n%3))
        n//=3
    return ''.join(digits)