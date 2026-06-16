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