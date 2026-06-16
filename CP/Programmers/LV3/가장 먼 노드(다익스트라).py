import heapq

def solution(n, edge):
    
    graph = [[] for _ in range(n+1)]
    for s, e in edge:
        graph[s].append((e, 1))
        graph[e].append((s, 1))
        
    def dijkstra(graph, start):
        dsts = [float('inf')] * (n+1)
        dsts[start] = 0
        pq = [(0, start)]
        
        while pq:
            cur_dst, cur_node = heapq.heappop(pq)
        
            if cur_dst > dsts[cur_node]:
                continue
            
            for neighbor, weight in graph[cur_node]:
                dst = cur_dst + weight
            
                if dst < dsts[neighbor]:
                    dsts[neighbor] = dst
                    heapq.heappush(pq, (dst, neighbor))
        return dsts
        
    dsts = dijkstra(graph, 1)
    
    return sum(1 for d in dsts[1:] if d == max(dsts[1:]))

# 1번으로부터 최단 경로 이동(간선 많은 거)
# 양방향
# ---
# 그래프 생성
# 1번이 기준
# distances 처음빼고 다 최대값 - float('inf')
# deque - 우선순위 큐

# pq 반복
#     - 지금 거리가 현재 노드보다 작으면 건너뛰기
#     그래프 내 이웃, 거리 반복
#         - 현재까지 온 거리+각 노드의 거리
#         distances에 있는 거리보다 작으면
# 	        - distances에 넣기
# 	        - 해당 노드 heap 넣기

# (grpah, 1) 시작
# 최대값만 카운트(중복 가능)