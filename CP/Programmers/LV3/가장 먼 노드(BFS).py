from collections import deque

def solution(n, edge):
    
    graph = [[] for _ in range(n+1)]
    for a, b in edge:
        graph[a].append(b)
        graph[b].append(a)
        
    distances = [-1] * (n+1)
    distances[1] = 0
    
    queue = deque([1])
    while queue:
        cur = queue.popleft()
        for next in graph[cur]:
            if distances[next] == -1:
                distances[next] = distances[cur] + 1
                queue.append(next)
                
    max_dist = max(distances)
    return distances.count(max_dist)