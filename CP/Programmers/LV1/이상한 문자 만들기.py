def solution(s):
    s = list(s)
    c_idx = 0
    for i in range(len(s)):
        if s[i] == ' ':
            c_idx = 0
            continue
        if c_idx%2 == 0: s[i] = s[i].upper()
        else: s[i] = s[i].lower()
        c_idx+=1
    return ''.join(s)
        