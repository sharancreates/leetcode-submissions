import heapq

class Solution:
    def shortestPath(self, n: int, edges: list[list[int]], labels: str, k: int) -> int:
        adj = [[] for _ in range(n)]
        for u, v, w in edges:
            adj[u].append((v, w))
    
        dist = [[float('inf')] * (k + 1) for _ in range(n)]
        
        pq = [(0, 0, 1)]
        dist[0][1] = 0
        
        while pq:
            d, u, count = heapq.heappop(pq)
            
            if u == n - 1:
                return d
            
            if d > dist[u][count]:
                continue
                
            for v, w in adj[u]:
                if labels[v] == labels[u]:
                    new_count = count + 1
                else:
                    new_count = 1
                
                if new_count > k:
                    continue
                
                if d + w < dist[v][new_count]:
                    dist[v][new_count] = d + w
                    heapq.heappush(pq, (d + w, v, new_count))
                    
        return -1
