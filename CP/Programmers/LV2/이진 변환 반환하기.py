def solution(s):
    cnt, roop = 0, 0
    while s != '1':
        cnt+=s.count('0')
        roop+=1
        s=s.replace('0', '')
        s = bin(len(s))[2:]
    return [roop, cnt]