def solution(s):
    s = s.split()
    s = sorted(s, key=int)
    s = [s[0], s[len(s)-1]]
    return ' '.join(s)