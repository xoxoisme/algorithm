def solution(answers):
    people = [[1, 2, 3, 4, 5], [2, 1, 2, 3, 2, 4, 2, 5], [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]
    cnt = [0, 0, 0]
    res = []
    for i in range(len(answers)):
        if answers[i] == people[0][i%len(people[0])]: cnt[0] += 1
        if answers[i] == people[1][i%len(people[1])]: cnt[1] += 1
        if answers[i] == people[2][i%len(people[2])]: cnt[2] += 1
    cnt = sorted(enumerate(cnt), key=lambda t: -t[1])
    max_cnt = cnt[0][1]
    for i in range(len(cnt)):
        if cnt[i][1] == max_cnt: res.append(cnt[i][0]+1)
    return res