def solution(signals):
    pattern = []
    for s in signals:
        ptr = 'G'*s[0]+'Y'*s[1]+'R'*s[2]
        pattern.append([ptr])
    min_s = [sum(s) for s in signals]
    time = 1
    for s in min_s: time*= s
    def check_y(time):
        check = []
        for ptr in pattern:
            for p in ptr:
                check.append(p[time%len(p)])
            if len(check) == len(signals) and set(check) == {'Y'}: return True
        return False
    for t in range(1, time+1):
        if check_y(t): break
        else: t = -1
    return t+1 if t != -1 else t
        