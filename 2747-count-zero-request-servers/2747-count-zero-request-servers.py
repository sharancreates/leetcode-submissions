class Solution:
    def countServers(self, n: int, logs: List[List[int]], x: int, queries: List[int]) -> List[int]:
        logs.sort(key=lambda log: log[1])
        
        sorted_queries = sorted(enumerate(queries), key=lambda q: q[1])
        
        server_counts = [0] * (n + 1)
        unique_servers = 0
        left = 0
        right = 0
        
        arr = [0] * len(queries)
        
        for i, q_val in sorted_queries:
            duration = [q_val - x, q_val]
            
            while right < len(logs) and logs[right][1] <= duration[1]:
                s_id = logs[right][0]
                if server_counts[s_id] == 0:
                    unique_servers += 1
                server_counts[s_id] += 1
                right += 1
                
            while left < len(logs) and logs[left][1] < duration[0]:
                s_id = logs[left][0]
                server_counts[s_id] -= 1
                if server_counts[s_id] == 0:
                    unique_servers -= 1
                left += 1
                
            arr[i] = n - unique_servers
            
        return arr
