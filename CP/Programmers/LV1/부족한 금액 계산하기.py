def solution(price, money, count):
    price_sum = sum([price*n for n in range(1, count+1)])
    return 0 if price_sum <= money else price_sum-money
    