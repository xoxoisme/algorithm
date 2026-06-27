def solution(lottos, win_nums):
    rank = {6:1, 5:2, 4:3, 3:4, 2:5}
    hope, win_nums, cnt = lottos.count(0), win_nums, 0
    for i in range(len(lottos)):
        if lottos[i] in win_nums: cnt += 1
    hope += cnt
    return [rank.get(hope, 6), rank.get(cnt, 6)]