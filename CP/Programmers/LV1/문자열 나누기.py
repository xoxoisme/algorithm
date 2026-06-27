def solution(s):
    c, r=0, 0
    for ch in s:
        if c==0:
            x=ch
            c+=1
            r+=1
        else:
            if ch==x: c+=1
            else: c-=1
    return r