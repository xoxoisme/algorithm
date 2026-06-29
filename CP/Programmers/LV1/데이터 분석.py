def solution(data, ext, val_ext, sort_by):
    opt = {'code': 0, 'date': 1, 'maximum': 2, 'remain': 3}
    res = []
    for row in data:
        if row[opt[ext]] < val_ext: res.append(row)
    res.sort(key=lambda x: x[opt[sort_by]])
    return res