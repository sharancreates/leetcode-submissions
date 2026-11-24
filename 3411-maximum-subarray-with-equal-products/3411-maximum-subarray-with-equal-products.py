import math

class Solution:
    def maxLength(self, nums: List[int]) -> int:
        n = len(nums)
        max_len = 0
        
        for i in range(n):
            for j in range(i, n):
                sub = nums[i : j + 1]
                if self.prod(sub) == self.lcm(sub) * self.gcd(sub):
                    max_len = max(max_len, j - i + 1)
                    
        return max_len 

    def lcm(self, arr):
        return math.lcm(*arr)

    def gcd(self, arr):
        return math.gcd(*arr)

    def prod(self, arr):
        return math.prod(arr)