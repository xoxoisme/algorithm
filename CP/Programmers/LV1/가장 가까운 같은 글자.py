def solution(s):
    res = [-1]
    for i in range(1, len(s)):
        near = s.rfind(s[i], 0, i)
        if near != -1: res.append(i-near)
        else: res.append(-1)
    return res