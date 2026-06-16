from collections import deque

def solution(begin, target, words):
    
    visited = set()
    queue = deque()
    queue.append((begin, 0))
    
    while queue:
        cur_word, cnt = queue.popleft()
        
        if cur_word == target:
            return cnt
        
        for word in words:
            if word not in visited and check(cur_word, word):
                visited.add(word)
                queue.append((word, cnt+1))
    return 0

def check(cur_word, word):
    cnt = 0
    for i in range(len(word)):
        if cur_word[i] != word[i]:
            cnt += 1
        if (cnt > 1):
            return False
    return True