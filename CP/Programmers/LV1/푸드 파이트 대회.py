def solution(food):
    res = []
    for i, n in enumerate(food):
        res.extend([str(i)]*(n//2))
    reversed_res = list(reversed(res))
    return ''.join(res+['0']+reversed_res)