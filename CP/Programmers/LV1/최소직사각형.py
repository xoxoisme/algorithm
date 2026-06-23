def solution(sizes):
    sort_sizes = sorted([sorted(p) for p in sizes])
    weight = max([m[0] for m in sort_sizes])
    height = max([h[1] for h in sort_sizes])
    return weight*height