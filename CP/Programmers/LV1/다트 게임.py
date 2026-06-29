import re

def solution(dartResult):
    point = re.findall(r'\d+', dartResult)
    bonus_rule = {'S': 1, 'D': 2, 'T': 3}
    bonus = [bonus_rule[b] for b in re.findall(r'[A-Z]', dartResult)]
    option = [o if o else '0' for o in re.findall(r'\d[A-Z]([*#]?)', dartResult)]
    res = 0
    for i in range(2, -1, -1):
        star, acha = 1, 1
        if option[i] == '*': star*=2
        if i != 2 and option[i+1] == '*': star*=2
        if option[i] == '#': acha = -1
        game = int(point[i])**bonus[i]*star*acha
        res+=game
    return res