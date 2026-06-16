from collections import deque

def solution(maps):
    rows, cols = len(maps), len(maps[0])
    visited = [[False] * cols for row in maps]
    visited[0][0] = True
    
    direct = [(1, 0), (-1, 0), (0, -1), (0, 1)] # 아래, 위, 왼쪽, 오른쪽
    queue = deque([])
    queue.append((1, 0, 0))
    
    while queue:
        cnt, y, x = queue.popleft()
        
        if x == cols-1 and y == rows-1 :
            return cnt;
        
        for dy, dx in direct:
            nx = x + dx
            ny = y + dy
            if (0 <= nx < cols and 0 <= ny < rows and visited[ny][nx] == False and maps[ny][nx] == 1):
                queue.append((cnt + 1, ny, nx))
                visited[ny][nx] = True    
    return -1