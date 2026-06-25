def solution(number, limit, power):
    res_list = [len([j for j in range(1, i+1) if i%j == 0]) for i in range(1, number+1)]
    return sum([i if i <= limit else power for i in res_list])