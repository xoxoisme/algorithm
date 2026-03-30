import sys

input = sys.stdin.readline

N, M = map(int, input().split())
graph = [list(input().strip()) for _ in range(N)]
state = [[0] * M for _ in range(N)]

def dfs(x, y):
    if x < 0 or N <= x or y < 0 or M <= y:
        return False

    if state[x][y] == 1:
        return False # 이미 방문한 곳
    if state[x][y] == 2:
        return True # 탈출 가능한 곳
    if state[x][y] == 3:
        return False # 탈출 불가능한 곳
    
    state[x][y] = 1

    if graph[x][y] == 'U':
        nx, ny = x - 1, y
    elif graph[x][y] == 'D':
        nx, ny = x + 1, y
    elif graph[x][y] == 'L':
        nx, ny = x, y - 1
    else:
        nx, ny = x, y + 1
    
    if dfs(nx, ny):
        state[x][y] = 2
        return True
    else:
        state[x][y] = 3
        return False

count = 0
for i in range(N):
    for j in range(M):
        if dfs[i][j]:
            count += 1

print(count)