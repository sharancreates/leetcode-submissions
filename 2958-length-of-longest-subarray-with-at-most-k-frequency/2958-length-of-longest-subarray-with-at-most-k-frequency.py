class Solution:
    def maxSubarrayLength(self, nums: list[int], k: int) -> int:
        frequency = {}
        left = 0
        v_count = 0  
        for right in range(len(nums)):
            incoming = nums[right]
            frequency[incoming] = frequency.get(incoming, 0) + 1
       
            if frequency[incoming] == k + 1:
                v_count += 1
                
            if v_count > 0:
                outgoing = nums[left]
                
                if frequency[outgoing] == k + 1:
                    v_count -= 1
                    
                frequency[outgoing] -= 1
                left += 1  
                
        return len(nums) - left
