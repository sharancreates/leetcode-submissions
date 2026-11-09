class Solution:
    def busiestServers(self, k: int, arrival: list[int], load: list[int]) -> list[int]:
        request_counts = [0] * k
        available = SortedList(range(k))
        busy = []
        
        for i, start_time in enumerate(arrival):
            while busy and busy[0][0] <= start_time:
                _, server_id = heapq.heappop(busy)
                available.add(server_id)
            
            if not available:
                continue
            
            preferred_id = i % k
            idx = available.bisect_left(preferred_id)
            
            if idx == len(available):
                idx = 0
                
            chosen_server = available.pop(idx)
            
            request_counts[chosen_server] += 1
            heapq.heappush(busy, (start_time + load[i], chosen_server))
            
        max_requests = max(request_counts)
        return [server_id for server_id, count in enumerate(request_counts) if count == max_requests]
