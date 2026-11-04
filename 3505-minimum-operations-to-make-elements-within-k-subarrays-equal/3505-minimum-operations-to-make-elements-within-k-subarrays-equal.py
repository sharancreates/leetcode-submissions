import heapq

class Solution:
    def minOperations(self, nums: list[int], x: int, k: int) -> int:
        n = len(nums)
        
        # cost[i] will store the minimum operations to make all elements in nums[i : i + x] equal
        cost = [0] * (n - x + 1)
        
        # Max-heap for the left half, Min-heap for the right half
        # Python's heapq is a min-heap, so we store negative values for the max-heap
        left_heap = []
        right_heap = []
        
        left_sum = 0
        right_sum = 0
        
        # Track elements that need to be lazily deleted
        to_remove = {}
        
        left_target_size = (x + 1) // 2
        left_active_size = 0
        right_active_size = 0
        
        def add(val):
            nonlocal left_sum, right_sum, left_active_size, right_active_size
            if not left_heap or val <= -left_heap[0]:
                heapq.heappush(left_heap, -val)
                left_sum += val
                left_active_size += 1
            else:
                heapq.heappush(right_heap, val)
                right_sum += val
                right_active_size += 1
            balance()
            
        def remove(val):
            nonlocal left_sum, right_sum, left_active_size, right_active_size
            to_remove[val] = to_remove.get(val, 0) + 1
            if val <= -left_heap[0]:
                left_sum -= val
                left_active_size -= 1
            else:
                right_sum -= val
                right_active_size -= 1
            balance()

        def balance():
            nonlocal left_sum, right_sum, left_active_size, right_active_size
            # Clean tops of the heaps if they contain elements marked for removal
            while left_heap and to_remove.get(-left_heap[0], 0) > 0:
                val = -heapq.heappop(left_heap)
                to_remove[val] -= 1
            while right_heap and to_remove.get(right_heap[0], 0) > 0:
                val = heapq.heappop(right_heap)
                to_remove[val] -= 1
                
            # Shift elements if left heap has too many elements
            while left_active_size > left_target_size:
                val = -heapq.heappop(left_heap)
                if to_remove.get(val, 0) > 0:
                    to_remove[val] -= 1
                else:
                    left_sum -= val
                    left_active_size -= 1
                    heapq.heappush(right_heap, val)
                    right_sum += val
                    right_active_size += 1
                    
            # Shift elements if left heap needs more elements
            while left_active_size < left_target_size and right_heap:
                val = heapq.heappop(right_heap)
                if to_remove.get(val, 0) > 0:
                    to_remove[val] -= 1
                else:
                    right_sum -= val
                    right_active_size -= 1
                    heapq.heappush(left_heap, -val)
                    left_sum += val
                    left_active_size += 1
                    
            # Double check heap tops after shifts
            while left_heap and to_remove.get(-left_heap[0], 0) > 0:
                val = -heapq.heappop(left_heap)
                to_remove[val] -= 1
            while right_heap and to_remove.get(right_heap[0], 0) > 0:
                val = heapq.heappop(right_heap)
                to_remove[val] -= 1

        def get_cost():
            median = -left_heap[0]
            l_cost = median * left_active_size - left_sum
            r_cost = right_sum - median * right_active_size
            return l_cost + r_cost

        # Initialize the first window
        for i in range(x):
            add(nums[i])
        cost[0] = get_cost()
        
        # Slide window across the array
        for i in range(x, n):
            remove(nums[i - x])
            add(nums[i])
            cost[i - x + 1] = get_cost()
            
        # DP Optimization: Space reduced to O(k) per index tracking
        INF = float('inf')
        dp = [INF] * (k + 1)
        dp[0] = 0  # 0 cost to form 0 subarrays
        
        # history stores the dp states up to index i
        dp_history = [[INF] * (k + 1) for _ in range(n + 1)]
        dp_history[0][0] = 0
        
        for i in range(1, n + 1):
            for j in range(k + 1):
                dp_history[i][j] = dp_history[i - 1][j]
                
            for j in range(1, k + 1):
                if i >= x and dp_history[i - x][j - 1] != INF:
                    dp_history[i][j] = min(dp_history[i][j], dp_history[i - x][j - 1] + cost[i - x])
                    
        return dp_history[n][k]
