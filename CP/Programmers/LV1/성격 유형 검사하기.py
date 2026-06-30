def solution(survey, choices):
    index = {'R':0, 'C': 0, 'J': 0, 'A': 0, 'T': 0, 'F': 0, 'M': 0, 'N': 0}
    score = [3, 2, 1, 0, 1, 2, 3]
    for c in range(len(choices)):
        if choices[c] > 3:
            s = survey[c][1]
            index[s] += score[choices[c]-1]
        else:
            s = survey[c][0]
            index[s] += score[choices[c]-1]
    res = []
    key = list(index.keys())
    for i in range(len(index)//2):
        if index[key[i]] >= index[key[i+4]]: res.append(key[i])
        else: res.append(key[i+4])
    return ''.join(res)