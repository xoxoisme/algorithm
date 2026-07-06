def solution(n):
    cnt = 0
    for i in range(1, n+1):
        sum_j = 0
        for j in range(i, n+1):
            sum_j+=j
            if sum_j == n:
                cnt+=1
                break
            elif sum_j > n: break
    return cnt