def solution(n):
    cnt, m = bin(n)[2:].count('1'), n+1
    while bin(m)[2:].count('1') != cnt: m+=1
    return m