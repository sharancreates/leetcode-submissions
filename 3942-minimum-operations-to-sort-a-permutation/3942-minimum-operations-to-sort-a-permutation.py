class Solution:
    def minOperations(self, nums: list[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0
        
        idx = nums.index(0)
        
        is_increasing = True
        for i in range(n):
            if nums[(idx + i) % n] != i:
                is_increasing = False
                break
                
        if is_increasing:
            if idx == 0:
                return 0
            return min(idx, n - idx + 2)
        
        is_decreasing = True
        for i in range(n):
            if nums[(idx - i + n) % n] != i:
                is_decreasing = False
                break
                
        if is_decreasing:
            return min(idx + 2, n - idx)
            
        return -1
