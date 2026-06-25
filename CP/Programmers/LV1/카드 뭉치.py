from collections import deque

def solution(cards1, cards2, goal):
    dq1, dq2 = deque(cards1), deque(cards2)
    for c in goal:
        if dq1 and dq1[0] == c: dq1.popleft()
        elif dq2 and dq2[0] == c: dq2.popleft()
        else: return "No"
    return "Yes"