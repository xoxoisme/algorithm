from collections import Counter

def solution(X, Y):
    mn, mx = (X, Y) if X <= Y else (Y, X)
    mn, mx = list(map(int, str(mn))), list(map(int, str(mx)))
    mx_counter = Counter(mx)
    res = []
    for i in mn:
        if mx_counter[i] > 0:
            res.append(i)
            mx_counter[i] -= 1
    res.sort(reverse=True)
    if res and res[0] == 0: res = [0]
    elif not res: res = [-1]
    return ''.join(map(str, res))