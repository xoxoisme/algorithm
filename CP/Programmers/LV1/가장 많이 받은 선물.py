from itertools import combinations

def solution(friends, gifts):
    dict_friends = {f: [0]*len(friends) for f in friends}
    for g in gifts:
        give, get = g.split()
        dict_friends[give][friends.index(get)]+=1
    score = []
    for f in friends:
        give = sum(dict_friends[f])
        get = sum(dict_friends[o][friends.index(f)] for o in friends)
        score.append(give-get)
    res = [0] *len(friends)
    for a, b in combinations(friends, 2):
        ab = dict_friends[a][friends.index(b)]
        ba = dict_friends[b][friends.index(a)]
        if ab > ba: res[friends.index(a)]+=1
        elif ba > ab: res[friends.index(b)]+=1
        else:
            if score[friends.index(a)]>score[friends.index(b)]: res[friends.index(a)]+=1
            elif score[friends.index(b)]>score[friends.index(a)]: res[friends.index(b)]+=1
            else: continue
    return max(res)