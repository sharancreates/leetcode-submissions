class Solution:
    def minSwaps(self, nums: list[int]) -> int:
        n = len(nums)
        def get_digit_sum(num: int) -> int:
            d_sum = 0
            while num > 0:
                d_sum += num % 10
                num //= 10
            return d_sum
        
        arr = [(nums[i], i) for i in range(n)]
        
        arr.sort(key=lambda x: (get_digit_sum(x[0]), x[0]))
        
        visited = [False] * n
        swaps = 0
        
        for i in range(n):
            if visited[i] or arr[i][1] == i:
                continue
                
            cycle_size = 0
            curr = i
            
            while not visited[curr]:
                visited[curr] = True
                curr = arr[curr][1]
                cycle_size += 1
                
            if cycle_size > 1:
                swaps += (cycle_size - 1)
                
        return swaps
