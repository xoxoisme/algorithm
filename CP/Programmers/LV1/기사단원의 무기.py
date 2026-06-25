def solution(number, limit, power):
    def cnt_div(i):
        cnt = 0
        for j in range(1, int(i**0.5)+1):
            if i%j == 0:
                cnt+= 2 if j != i//j else 1
        return cnt
    res_list = [cnt_div(i) for i in range(1, number+1)]
    return sum([i if i <= limit else power for i in res_list])