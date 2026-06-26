def solution(babbling):
    say = ["aya", "ye", "woo", "ma"]
    cnt = 0
    for w in babbling:
        for s in say:
            if s*2 not in w: w = w.replace(s, ' ')
        if w.isspace(): cnt += 1
    return cnt