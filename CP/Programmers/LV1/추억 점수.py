def solution(name, yearning, photo):
    d = dict(zip(name, yearning))
    return [sum([d[c] for c in row if c in name]) for row in photo]