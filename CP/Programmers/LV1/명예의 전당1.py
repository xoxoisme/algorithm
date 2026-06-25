import heapq

def solution(k, score):
    res =[]
    hp = []
    for i in range(len(score)):
        if len(hp) < k: heapq.heappush(hp, score[i])
        else:
            if score[i] > hp[0]:
                heapq.heappop(hp)
                heapq.heappush(hp, score[i])
        res.append(hp[0])
    return res
        