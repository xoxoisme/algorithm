import heapq

def solution(N, road, K):
    graph = [[] for _ in range(N+1)]
    
    for s, e, w in road:
        graph[s].append((e, w))
        graph[e].append((s, w))
    
    def dijkstra(graph, start):
        distances = [float('inf')] * (N+1)
        distances[start] = 0
        pq = [(0, start)]
        
        while pq:
            cur_dst, cur_node = heapq.heappop(pq)
            if cur_dst > distances[cur_node]:
                continue
            
            for neighbor, weight in graph[cur_node]:
                dst = cur_dst+weight
                
                if dst < distances[neighbor]:
                    distances[neighbor] = dst
                    heapq.heappush(pq, (dst, neighbor))
        return distances
    
    distances = dijkstra(graph, 1)
    
    return len([d for d in distances[1:] if d <= K])