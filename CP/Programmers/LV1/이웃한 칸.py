def solution(board, h, w):
    drc = [(-1, 0), (0, -1), (1, 0), (0, 1)]
    cnt = 0
    for mh, mw in drc:
        if 0<=h+mh<len(board) and 0<=w+mw<len(board[0]) and board[h+mh][w+mw] == board[h][w]: cnt += 1
    return cnt