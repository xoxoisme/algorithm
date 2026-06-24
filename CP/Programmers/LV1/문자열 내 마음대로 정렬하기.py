def solution(strings, n):
    res = []
    sort_strings = sorted(strings)
    seq_strings = sorted((s[n], i) for i, s in enumerate(sort_strings))
    for c, i in seq_strings:
        res.append(sort_strings[i])
    return res