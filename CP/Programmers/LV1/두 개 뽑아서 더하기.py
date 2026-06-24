from itertools import combinations

def solution(numbers):
    return sorted({sum(combo) for combo in combinations(numbers, 2)})