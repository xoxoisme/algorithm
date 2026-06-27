def solution(s, skip, index):
    res = []
    alphabet = [c for c in "abcdefghijklmnopqrstuvwxyz" if c not in set(skip)]
    for c in s:
        res.append(alphabet[(alphabet.index(c)+index)%len(alphabet)])
    return ''.join(res)