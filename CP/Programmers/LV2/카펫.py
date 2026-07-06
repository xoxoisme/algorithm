def solution(brown, yellow):
    for b in range(brown//4, brown//2):
        w, h = b, (brown-(b*2))//2+2
        if w >= h and w*h == brown+yellow: return [w, h]