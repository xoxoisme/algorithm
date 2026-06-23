def solution(s, n):
    res=[]
    for c in s:
        if c.isalpha():
            base = ord('A') if c.isupper() else ord('a')
            res.append(chr((ord(c)-base+n)%26+base))
        else: res.append(c)
    return ''.join(res)