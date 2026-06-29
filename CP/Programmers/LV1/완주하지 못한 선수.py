def solution(participant, completion):
    p_dict = {}
    for i, p in enumerate(participant):
        p_dict.setdefault(p, []).append(i)
    res = []
    for c in completion:
        if c in p_dict:
            p_dict[c].pop(0)
    for p, n in p_dict.items():
        if n: return p
    return 0